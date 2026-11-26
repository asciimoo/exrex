# -*- coding: utf-8 -*-
import re
import unittest

from exrex import simplify


class SimplifyRepeatTest(unittest.TestCase):

    def assert_same(self, regex, texts):
        s = simplify(regex)
        for text in texts:
            self.assertEqual(
                re.match('(?:%s)$' % regex, text) is not None,
                re.match('(?:%s)$' % s, text) is not None,
                '%r -> %r, text %r' % (regex, s, text))

    def test_repeated_sequence(self):
        texts = ('', 'a', 'ab', 'abb', 'abab', 'ababab', 'abc', 'c', 'ac')
        for regex in ('(?:ab)+', '(?:ab)*', '(?:ab){2}', '(?:ab){1,2}',
                      '(?:ab)+?', '(?:ab)?c', '((?:ab)+)', '(?:(?:ab))+'):
            self.assert_same(regex, texts)

    def test_nested_repeat(self):
        texts = ('', 'a', 'aa', 'aaa', 'aaaa', 'aaaaaa', 'abc', 'abcbc', 'bc')
        for regex in ('(?:a{2}){3}', '(?:a*)?', '(?:a{2})+', '(?:a??)?',
                      '(?:a(?:bc)+)?', '(?:a+?)*'):
            self.assert_same(regex, texts)

    def test_repeated_branch_in_capture(self):
        texts = ('', 'a', 'bc', 'abc', 'bca', 'abcc', 'bcc')
        for regex in ('((?:a|bc)*)', '((?:a|bc)+?)', '(?:a|bc){2}'):
            self.assert_same(regex, texts)

    def test_atoms_are_not_wrapped(self):
        for regex in ('a+', '[ab]*', '(ab)+', '.*?', '(?:a)+'):
            self.assertFalse('(?:' in simplify(regex), regex)


if __name__ == '__main__':
    unittest.main()
