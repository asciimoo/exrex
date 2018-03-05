EXREX
=====

Irregular methods for regular expressions.

Exrex is a command line tool and python module that generates all - or random - matching strings to a given regular expression and more.
It's pure python, without external dependencies.

There are regular expressions with infinite matching strings (eg.: `[a-z]+`), in these cases exrex limits the maximum length of the infinite parts.

Exrex uses generators, so the memory usage does not depend on the number of matching strings.

[![Version](https://img.shields.io/pypi/v/exrex.svg)](https://crate.io/packages/exrex/)   [![Downloads](https://img.shields.io/pypi/dm/exrex.svg)](https://crate.io/packages/exrex/)

*Features*

 * Generating all matching strings
 * Generating a random matching string
 * Counting the number of matching strings
 * Simplification of regular expressions


### Installation


To install exrex, simply:

```bash
$ pip install exrex
```

or

```bash
$ easy_install exrex
```


Usage
=====

### as python module

```python
>>> import exrex

>>> exrex.getone('(ex)r\\1')
'exrex'

>>> list(exrex.generate('((hai){2}|world!)'))
['haihai', 'world!']

>>> exrex.getone('\d{4}-\d{4}-\d{4}-[0-9]{4}')
'3096-7886-2834-5671'

>>> exrex.getone('(1[0-2]|0[1-9])(:[0-5]\d){2} (A|P)M')
'09:31:40 AM'

>>> exrex.count('[01]{0,9}')
1023

>>> print '\n'.join(exrex.generate('This is (a (code|cake|test)|an (apple|elf|output))\.'))
This is a code.
This is a cake.
This is a test.
This is an apple.
This is an elf.
This is an output.

>>> print exrex.simplify('(ab|ac|ad)')
(a[bcd])
```

### Command line usage

```
> exrex --help
usage: exrex.py [-h] [-o FILE] [-l] [-d DELIMITER] [-v] REGEX

exrex - regular expression string generator

positional arguments:
  REGEX                 REGEX string

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --output FILE
                        Output file - default is STDOUT
  -l N, --limit N       Max limit for range size - default is 20
  -c, --count           Count matching strings
  -m N, --max-number N  Max number of strings - default is -1
  -r, --random          Returns a random string that matches to the regex
  -s, --simplify        Simplifies a regular expression
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter - default is \n
  -v, --verbose         Verbose mode
```

Examples:

```
$ exrex '[asdfg]'
a
s
d
f
g

$ exrex -r '(0[1-9]|1[012])-\d{2}'
09-85

$ exrex '[01]{10}' -c
1024

```

### Bugs

Bugs or suggestions? Visit the [issue tracker](https://github.com/asciimoo/exrex/issues).


### Documentation

http://exrex.readthedocs.org/en/latest/

### TODO

 * Command line switches to change default character sets/ranges/range limits (eg. for '.','\s'..) (40%)
 * Extend categories (`re.sre_parse.CATEGORIES`) (30%)
 * Improve setup.py
 * More verbose code
 * Documentation
 * Optimizations
 * Generation of `n` different random matching string
 * Memory usage reduction (100%?) - generators
 * Count the number of matching strings - (100%?)
 * Unicode support (100%)
 * Handle grouprefs (100%)
 * Python3 compatibility (100%) ( >= python3.3)


### License

```
exrex is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

exrex is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with exrex. If not, see < http://www.gnu.org/licenses/ >.

(C) 2012- by Adam Tauber, <asciimoo@gmail.com>
```

### Fun/arts

 * Boat: `exrex '( {20}(\| *\\|-{22}|\|)|\.={50}| (  ){0,5}\\\.| {12}~{39})'`
 * Eyes: `exrex '(o|O|0)(_)(o|O|0)'`

### Similar projects

 * [randexp.js](http://fent.github.com/randexp.js/)
 * [regldg](http://regldg.com/)
 * [regex-genex](https://github.com/audreyt/regex-genex)

### Profiling

 * `python -m cProfile exrex.py '[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]' -o /dev/null`
 * `python -m cProfile exrex.py '[0-9]{6}' -o /dev/null`

