# -*- coding: utf-8 -*-
import re
import unittest

from exrex import simplify


class SimplifyClassTest(unittest.TestCase):

    def test_escapes_in_class(self):
        texts = ['', 'a]', 'z'] + [chr(c) for c in range(128)]
        for regex in (r'[a\]]', r'[^\]]', r'[^\\]', r'[^\^]', r'[a\-z]',
                      r'[+\-/]', r'[\^a]', r'[\\\]]', r'[!-\]]', r'[\]-a]',
                      r'[^\]\\]', r'[\[a]', r'[\w\-.]', r'[-a]', r'a|-|c'):
            s = simplify(regex)
            for text in texts:
                self.assertEqual(
                    re.match('(?:%s)$' % regex, text) is not None,
                    re.match('(?:%s)$' % s, text) is not None,
                    '%r -> %r, text %r' % (regex, s, text))

    def test_special_chars_stay_unescaped_in_class(self):
        self.assertEqual(simplify('[.*+?(){}|$]'), '[.*+?(){}|$]')


if __name__ == '__main__':
    unittest.main()
