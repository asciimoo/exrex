# -*- coding: utf-8 -*-
import re
import unittest

from exrex import simplify


class SimplifyGroupingTest(unittest.TestCase):

    def test_common_prefix_inside_capture(self):
        # Issue #56: the alternation must stay grouped under the prefix.
        s = simplify('^(prefix/1|prefix/23)$')
        for text in ('prefix/1', 'prefix/23'):
            m = re.match(s, text)
            self.assertTrue(m is not None, text)
            self.assertEqual(m.group(1), text)
        for text in ('23', 'prefix/', 'prefix/2', 'prefix/123'):
            self.assertTrue(re.match(s, text) is None, text)

    def test_suffix_after_capture_precedence(self):
        s = simplify('^(pre/1|pre/23)end$')
        for text in ('pre/1end', 'pre/23end'):
            self.assertTrue(re.match(s, text) is not None, text)
        for text in ('23end', 'pre/1', 'pre/23', 'end'):
            self.assertTrue(re.match(s, text) is None, text)

    def test_capture_and_backreference_numbering(self):
        s = simplify(r'^(k/(x)\2|k/(y)\3)$')
        self.assertEqual(re.compile(s).groups, 3)
        m = re.match(s, 'k/xx')
        self.assertTrue(m is not None)
        self.assertEqual(m.groups(), ('k/xx', 'x', None))
        m = re.match(s, 'k/yy')
        self.assertTrue(m is not None)
        self.assertEqual(m.groups(), ('k/yy', None, 'y'))
        for text in ('k/xy', 'k/yx', 'yy', 'xx'):
            self.assertTrue(re.match(s, text) is None, text)

    def test_bare_alternation_still_simplifies(self):
        s = simplify('^(ab|ac|ad)$')
        self.assertEqual(re.compile(s).groups, 1)
        for text in ('ab', 'ac', 'ad'):
            m = re.match(s, text)
            self.assertTrue(m is not None, text)
            self.assertEqual(m.group(1), text)
        for text in ('a', 'ae', 'b'):
            self.assertTrue(re.match(s, text) is None, text)


if __name__ == '__main__':
    unittest.main()
