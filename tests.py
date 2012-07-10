

from exrex import generate, count


RS = {'[ab][cd]': ['ac', 'ad', 'bc', 'bd']
     ,'[12]{1,2}': ['1', '2', '11', '12', '21', '22']
     ,'((hai){2}|world)!': ['haihai!', 'world!']
     ,'[ab]{1,3}': ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
     ,'\d': map(str, range(0, 10))
     ,'a[b]?(c){0,1}': ['a', 'ac', 'ab', 'abc']
     ,'(a(b(c(d(e(f))))))': ['abcdef']
     ,'(a(b(c(d(e(f){1,2}))))){1,2}': ['abcdef', 'abcdeff', 'abcdefabcdef', 'abcdefabcdeff', 'abcdeffabcdef', 'abcdeffabcdeff']
     }

def gen_test():
    for regex, result in RS.items():
        assert list(generate(regex)) == result

def count_test():
    for regex, result in RS.items():
        assert count(regex) == len(result)


if __name__ == '__main__':
    gen_test()
    print('[!] generation test passed')
    count_test()
    print('[!] length test passed')
