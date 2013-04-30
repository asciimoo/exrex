#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of exrex.
#
# exrex is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# exrex is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with exrex. If not, see < http://www.gnu.org/licenses/ >.
#
# (C) 2012- by Adam Tauber, <asciimoo@gmail.com>

from exrex import generate, count, getone, CATEGORIES
import re
from sys import exit

RS = {'[ab][cd]': ['ac', 'ad', 'bc', 'bd']
     ,'[12]{1,2}': ['1', '2', '11', '12', '21', '22']
     ,'((hai){2}|world)!': ['haihai!', 'world!']
     ,'[ab]{1,3}': ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
     ,'\d': list(map(str, range(0, 10)))
     ,'a[b]?(c){0,1}': ['a', 'ac', 'ab', 'abc']
     ,'(a(b(c(d(e(f))))))': ['abcdef']
     ,'(a(b(c(d(e(f){1,2}))))){1,2}': ['abcdef', 'abcdeff', 'abcdefabcdef', 'abcdefabcdeff', 'abcdeffabcdef', 'abcdeffabcdeff']
     ,'[^a]': [x for x in CATEGORIES['category_any'] if x != 'a']
     ,'[^asdf]': [x for x in CATEGORIES['category_any'] if x not in 'asdf']
     ,'asdf': ['asdf']
     ,'[áíő]': [u'á', u'í', u'ő']
     ,'(a|b)(1|2)\\1\\2\\1\\2': ['a1a1a1', 'a2a2a2', 'b1b1b1', 'b2b2b2']
     }

BIGS = ['^a*$'
       ,'^[a-zA-Z]+$'
       ,'^(foo){3,}$'
       ,'^([^/]+)(.*)$'
       ,'^[^/]+(.*)$'
       ,'^([^/]+).*$'
       ,'^[^asdf]+$'
       ,'^([^0-9]{2,}|(a|s|d|f|g)+|[a-z]+)+$'
       ,'^([^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]|asdf)+$'
       ,'^(1[0-2]|0[1-9])(:[0-5]\d){2} (A|P)M$'
       ]

def gen_test():
    for regex, result in RS.items():
        try:
            assert list(generate(regex)) == result
        except:
            print('[E] Assertion error! "%s"\n\t%r != %r' % (regex, list(generate(regex)), result))
            return -1
    return 0

def count_test():
    for regex, result in RS.items():
        c = count(regex)
        l = len(result)
        try:
            assert c == l
        except:
            print('[E] Assertion error! "%s"\n\t%d != %d' % (regex.decode('utf-8'), c, l))
            return -1
    return 0

def getone_test(tries):
    for regex,_ in RS.items():
        for _ in range(tries):
            try:
                s = getone(regex)
                assert re.match(regex, s.encode('utf-8'), re.U)
            except Exception:
                print('[E] Assertion error! "%s"\n\t%s not match' % (regex.decode('utf-8'), s))
                return -1
    for regex in BIGS:
        for _ in range(tries):
            try:
                s = getone(regex)
                assert re.match(regex, s.encode('utf-8'), re.U)
            except:
                print('[E] Assertion error! "%s"\n\t%s not match' % (regex.decode('utf-8'), s))
                return -1
    return 0


if __name__ == '__main__':
    errors = gen_test()
    if errors == 0:
        print('[+] generation test passed')
    else:
        print('[-] generation test failed')
        exit(errors)
    errors = count_test()
    if errors == 0:
        print('[+] length test passed')
    else:
        print('[-] length test failed')
        exit(errors)
    errors = getone_test(200)
    if errors == 0:
        print('[+] random generation test passed')
    else:
        print('[-] random generation test failed')
        exit(errors)
