

from exrex import generate, count, getone, CATEGORIES
from re import match

RS = {'[ab][cd]': ['ac', 'ad', 'bc', 'bd']
     ,'[12]{1,2}': ['1', '2', '11', '12', '21', '22']
     ,'((hai){2}|world)!': ['haihai!', 'world!']
     ,'[ab]{1,3}': ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
     ,'\d': map(str, range(0, 10))
     ,'a[b]?(c){0,1}': ['a', 'ac', 'ab', 'abc']
     ,'(a(b(c(d(e(f))))))': ['abcdef']
     ,'(a(b(c(d(e(f){1,2}))))){1,2}': ['abcdef', 'abcdeff', 'abcdefabcdef', 'abcdeffabcdeff']
     ,'[^a]': [x for x in CATEGORIES['category_any'] if x != 'a']
     ,'[^asdf]': [x for x in CATEGORIES['category_any'] if x not in 'asdf']
     ,'asdf': ['asdf']
     }

BIGS = ['^a*$'
       ,'^[a-zA-Z]+$'
       ,'^(foo){3,}$'
       ,'([^/]+)(.*)'
       ,'[^/]+(.*)'
       ,'([^/]+).*'
       ,'[^asdf]+'
       ,'([^0-9]{2,}|(a|s|d|f|g)+|[a-z]+)+'
       ,'([^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]|asdf)+'
       ]

def gen_test():
    err = 0
    for regex, result in RS.items():
        try:
            assert list(generate(regex)) == result
        except:
            err += 1
            print '[E] Assertion error! "%s"\n\t%r != %r' % (regex, list(generate(regex)), result)
    return err

def count_test():
    err = 0
    for regex, result in RS.items():
        c = count(regex)
        l = len(result)
        try:
            assert c == l
        except:
            err += 1
            print '[E] Assertion error! "%s"\n\t%d != %d' % (regex, c, l)
    return err

def getone_test(tries):
    err = 0
    for regex,_ in RS.items():
        for _ in xrange(tries):
            try:
                s = getone(regex)
                assert match(regex, s)
            except:
                err += 1
                print '[E] Assertion error! "%s"\n\t%s not match' % (regex, s)
    for regex in BIGS:
        for _ in xrange(tries):
            try:
                s = getone(regex)
                assert match(regex, s)
            except:
                err += 1
                print '[E] Assertion error! "%s"\n\t%s not match' % (regex, s)
    return err


if __name__ == '__main__':
    errors = gen_test()
    if errors == 0:
        print('[+] generation test passed')
    else:
        print('[-] generation test failed\n\t%d errors' % errors)
    errors = count_test()
    if errors == 0:
        print('[+] length test passed')
    else:
        print('[-] length test failed\n\t%d errors' % errors)
    errors = getone_test(200)
    if errors == 0:
        print('[+] random generation test passed')
    else:
        print('[-] random generation test failed\n\t%d errors' % errors)
