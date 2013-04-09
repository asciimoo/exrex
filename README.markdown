EXREX
=====

Exrex is a command line tool and python module that generates all - or random - matching strings to a given regular expression.
It is pure python, without external dependencies.

There are regular expressions with infinite matching strings (eg.: `[a-z]+`), in these cases exrex limits the maximum length of the infinite parts.

Exrex uses generators, so the memory usage does not depend on the number of matching strings.

### Installation


To install exrex, simply:

```bash
$ pip install exrex
```

or

```bash
$ easy_install exrex
```

### Bugs

Bugs or suggestions? Visit the [issue tracker](https://github.com/asciimoo/exrex/issues).

USAGE
=====

### as python module

```python
>>> import exrex

>>> [x for x in exrex.generate('((hai){2}|world)!')]
['haihai!', 'world!']

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
```

### Command line usage

```
> python -m exrex --help
usage: exrex.py [-h] [-o FILE] [-l] [-d DELIMITER] [-v] REGEX

exrex - regular expression string generator

positional arguments:
  REGEX                 REGEX string

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --output FILE
                        Output file - default is STDOUT
  -l, --limit           Max limit for range size - default is 20
  -c, --count           Count matching strings
  -r, --random          Returns a random string that matches to the regex
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter - default is \n
  -v, --verbose         Verbose mode
```

Examples:
```
$ python -m exrex '[asdfg]'
a
s
d
f
g

$ python -m exrex -r '(0[1-9]|1[012])-\d{2}'
09-85

$ python -m exrex '[01]{10}' -c
1024
```

Documentation
=============

http://exrex.readthedocs.org/en/latest/

TODO
====

 * Python3 compatibility (100%)
 * Memory usage reduction (100%?) - generators
 * Count the number of matching strings - (100%?)
 * Command line switches to change default character sets/ranges/range limits (eg. for '.','\s'..) (40%)
 * Extend categories (re.sre_parse.CATEGORIES) (30%)
 * Handle grouprefs (eg.: \1 ) (0%)
 * Improve setup.py
 * More verbose code
 * Documentation


License
=======

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
Fun/arts
========

 * Boat: `python -m exrex '( {20}(\| *\\|-{22}|\|)|\.={50}| (  ){0,5}\\\.| {12}~{39})'`
 * Eyes: `python -m exrex '(o|O|0)(_)(o|O|0)'`

Similar projects
================
 * [randexp.js](http://fent.github.com/randexp.js/)

Profiling
=============

 * `python -m cProfile exrex.py '[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]' -o /dev/null`
 * `python -m cProfile exrex.py '[0-9]{6}' -o /dev/null`

