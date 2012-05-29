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
from itertools import product, imap, chain, tee

CATEGORIES = {'category_space'  : sre_parse.WHITESPACE
             ,'category_digit'  : sre_parse.DIGITS
             ,'category_any'    : [chr(x) for x in range(32, 123)]
             }

def comb(g, i):
    for c in g:
        g2,i = tee(i)
        for c2 in g2:
            yield c+c2

def mappend(g, c):
    for cc in g:
        yield cc+c

def _in(d):
    ret = []
    for i in d:
        if i[0] == 'range':
            ret.extend(imap(chr, range(i[1][0], i[1][1]+1)))
        elif i[0] == 'literal':
            ret.append(chr(i[1]))
    return ret

def _p(d):
    """docstring for _p"""
    ret = ['']
    params = []
    index = -1
    for i in d:
        index+=1
        if i[0] == 'in':
            ret = comb(ret, _in(i[1]))
        elif i[0] == 'literal':
            ret = mappend(ret, chr(i[1]))
        elif i[0] == 'category':
            ret = comb(ret, CATEGORIES.get(i[1], ['']))
        elif i[0] == 'any':
            ret = comb(ret, CATEGORIES['category_any'])
        elif i[0] == 'max_repeat':
            #TODO !! t_ret
            t_ret = list(ret)
            chars = filter(None, _p(list(i[1][2])))
            ran = xrange(i[1][0], i[1][1]+1)
            ret = (r+''.join(piece) for r in t_ret for rep in ran for piece in product(chars, repeat=rep))
        elif i[0] == 'branch':
            subs = chain.from_iterable(_p(list(x)) for x in i[1][1])
            ret = comb(ret, subs)
        elif i[0] == 'subpattern':
            l = i[1:]
            subs = chain.from_iterable(_p(list(x[1])) for x in l)
            ret = comb(ret, subs)

    return ret


def parse(s):
    """docstring for parse"""
    r = sre_parse.parse(s)
    #print r
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
    # '.+'
    # 'asdf.{1,4}qwer{2,5}'
    # 'a(b)?(c)?(d)?'
    # 'a[b][c][d]?[e]?
    args = argparser()
    for s in parse(args['regex']):
        try:
            args['output'].write(s+args['delimiter'])
        except:
            break

if __name__ == '__main__':
    __main__()
