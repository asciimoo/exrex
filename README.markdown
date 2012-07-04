EXREX
=====

### Description

Exrex is a tool and python module that generates all matching strings to a given regular expression.

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
```

### Using as python module

Examples:

```python
>>> import exrex
>>> [x for x in exrex.generate('((hai){2}|world)!')]
['haihai!', 'world!']
>>> list(exrex.generate('[ab]{1,3}'))
['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
>>> print '\n'.join(exrex.generate('This is (a (code|cake|test)|an (apple|elf|output))\.'))
This is a code.
This is a cake.
This is a test.
This is an apple.
This is an elf.
This is an output.
```

### TODO

 * Count the number of matching strings (20%) - buggy
 * Command line switches to change default character sets/ranges/range limits (eg. for '.','\s'..) (20%)
 * Memory usage reduction (100%) - fully generatorized


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

