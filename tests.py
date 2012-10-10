

from exrex import generate, count, getone, CATEGORIES
from re import match

RS = {'[ab][cd]': ['ac', 'ad', 'bc', 'bd']
     ,'[12]{1,2}': ['1', '2', '11', '12', '21', '22']
     ,'((hai){2}|world)!': ['haihai!', 'world!']
     ,'[ab]{1,3}': ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
     ,'\d': map(str, range(0, 10))
     ,'a[b]?(c){0,1}': ['a', 'ac', 'ab', 'abc']
     ,'(a(b(c(d(e(f))))))': ['abcdef']
     ,'(a(b(c(d(e(f){1,2}))))){1,2}': ['abcdef', 'abcdeff', 'abcdefabcdef', 'abcdefabcdeff', 'abcdeffabcdef', 'abcdeffabcdeff']
     ,'[^a]': [x for x in CATEGORIES['category_any'] if x != 'a']
     ,'[^asdf]': [x for x in CATEGORIES['category_any'] if x not in 'asdf']
     }

BIGS = ['^a*$'
       ,'^[a-zA-Z]+$'
       ,'^(foo){3,}$'
       ]

def gen_test():
    for regex, result in RS.items():
        assert list(generate(regex)) == result

def count_test():
    for regex, result in RS.items():
        assert count(regex) == len(result)

def getone_test():
    for regex,_ in RS.items():
        assert match(regex, getone(regex))
    for regex in BIGS:
        assert match(regex, getone(regex))


if __name__ == '__main__':
    gen_test()
    print('[+] generation test passed')
    count_test()
    print('[+] length test passed')
    getone_test()
    print('[+] random generation test passed')
