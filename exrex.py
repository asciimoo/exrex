#!/usr/bin/env python

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

from re import sre_parse
from itertools import product, imap, chain

CATEGORIES = {'category_space'  : sre_parse.WHITESPACE
             ,'category_digit'  : sre_parse.DIGITS
             ,'category_any'    : [chr(x) for x in range(32, 123)]
             }

def _p(d, append=False):
    """docstring for _p"""
    #print d
    ret = ['']
    ranges = []
    if not isinstance(d, list):
        print '[!] not a list: %r' % d
        yield None
    if not len(d):
        print '[!] empty list'
        yield None
    l = ''
    for i in d:
        if len(ranges) and i[0] != 'range':
            if len(ret):
                ret = (r+char for r in ret for char in ranges)
            else:
                ret = ranges
            ranges = []

        if i[0] == 'literal':
            # TODO
            if append:
                if ret[0] == '':
                    ret[0] = chr(i[1])
                else:
                    ret.append(chr(i[1]))
            else:
                c = chr(i[1])
                ret = [r+c for r in ret]
        elif i[0] == 'subpattern':
            l = i[1:]
            ret = (r+piece for r in ret for sub in l for piece in _p(list(sub[1])))
        elif i[0] == 'in':
            l = list(i[1])
            ret = (r+''.join(piece) for r in ret for piece in _p(l, True))
        elif i[0] == 'range':
            ranges.extend(imap(chr, xrange(i[1][0], i[1][1]+1)))
        elif i[0] == 'max_repeat':
            tmp_ret = list(ret)
            chars = filter(None, _p(list(i[1][2])))
            ran = range(i[1][0], i[1][1]+1)
            ret = (r+''.join(piece) for r in tmp_ret for rep in ran for piece in product(chars, repeat=rep))
        elif i[0] == 'category':
            cat = CATEGORIES.get(i[1], [''])
            ret = (r+c for r in ret for c in cat)
        elif i[0] == 'branch':
            subs = chain.from_iterable(_p(list(x)) for x in i[1][1])
            ret = (r+s for r in ret for s in subs)
        elif i[0] == 'any':
            ret = (r+c for r in ret for c in CATEGORIES['category_any'])

    if len(ranges):
        if len(ret) and ret[0] != '':
            ret = (r+char for r in ret for char in ranges)
        else:
            ret = ranges
    #print ret
    for r in ret:
        yield r


def parse(s):
    """docstring for parse"""
    r = sre_parse.parse(s)
    print r
    return _p(list(r))


def argparser():
    import argparse
    from sys import stdout
    argp = argparse.ArgumentParser(description='exrex - regular expression string generator')
    argp.add_argument('-o', '--output'
                     ,help      = 'Output file - default is STDOUT'
                     ,metavar   = 'FILE'
                     ,default   = stdout
                     ,type      = argparse.FileType('w')
                     )
    argp.add_argument('-d', '--delimiter'
                     ,help      = 'Delimiter - default is \\n'
                     ,default   = '\n'
                     )
    argp.add_argument('-v', '--verbose'
                     ,action    = 'count'
                     ,help      = 'Verbosity level - default is 3'
                     ,default   = 3
                     )
    argp.add_argument('regex'
                     ,metavar   = 'REGEX'
                     ,help      = 'REGEX string'
                     )
    return vars(argp.parse_args())

def __main__():
    # 'as(d|f)qw(e|r|s)[a-zA-Z]{2,3}'
    # 'as(QWE|Z([XC]|Y|U)V){2,3}asdf'
    # '.?'
    args = argparser()
    for s in parse(args['regex']):
        try:
            args['output'].write(s+args['delimiter'])
        except:
            break

if __name__ == '__main__':
    __main__()
