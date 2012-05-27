EXREX
=====

### Description

Exrex is a tool and python module that generates all matching strings to a given regular expression.

### Command line usage

```
> python exrex.py --help
usage: exrex.py [-h] [-o FILE] [-d DELIMITER] [-v] REGEX

exrex - regular expression string generator

positional arguments:
  REGEX                 REGEX string

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --output FILE
                        Output file - default is STDOUT
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter - default is \n
  -v, --verbose         Verbosity level - default is 3
```

### Using as python module

Example:

```python
>>> import exrex
>>> [x for x in exrex.parse('((hai){2}|world)!')]
['haihai!', 'world!']
>>> [x for x in exrex.parse('[ab]{1,3}')]
['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
```

### TODO

 * Memory usage reduction (!generators!) (80%)
 * Count the number of matching strings (0%)
 * Command line switches to change default character sets/ranges (eg. for '.','\s'..) (0%)


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

