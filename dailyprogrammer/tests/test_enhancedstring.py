#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_enhancedstring.py

Unit tests for module :mod:`plugins.enhancedstring` (source_).
"""

import unittest

from plugins import enhancedstring


class TestEnhancedString(unittest.TestCase):
    """Unit tests for class :func:`plugins.enhancedstring.EnhancedString`."""


    def test___init__(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.__init__`

        **Tested:**

        - The attributes of an enhanced string are correct after initialization.
        """
        str_ = enhancedstring.EnhancedString('test123')
        self.assertEqual(str_.str_, 'test123')


    def test___str__(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.__str__`

        **Tested:**

        - The returned string is correct.
        """
        str_ = enhancedstring.EnhancedString('test123')
        self.assertEqual(str_.__str__(), 'test123')


    def test_remove(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.remove`

        **Tested:**

        - The passed characters are correctly removed from the enhanced string.
        """
        str_ = enhancedstring.EnhancedString('abcdaabbccddaaabbbcccddd')
        str_.remove('bc')
        self.assertEqual(str(str_), 'adaaddaaaddd')


    def test_align(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.align`

        **Tested:**

        - Center alignment works properly.
        - Right alignment works properly.
        - Left alignment workds properly.
        """
        str_ = enhancedstring.EnhancedString('a\nbcd\nefghi')
        str_.align('^')
        self.assertEqual(str(str_), '  a\n bcd\nefghi')
        str_.align('>')
        self.assertEqual(str(str_), '    a\n  bcd\nefghi')
        str_.align('<')
        self.assertEqual(str(str_), 'a\nbcd\nefghi')
