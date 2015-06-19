#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_asciiart.py

Unit tests for module :mod:`plugins.asciiart` (source_).
"""

import unittest

from plugins import asciiart


class TestTextTriangle(unittest.TestCase):
    """Unit tests for class :func:`plugins.asciiart.TextTriangle`."""


    def test___init__(self):
        """Test method :meth:`plugins.asciiart.TextTriangle.__init__`

        **Tested:**

        - The attributes of a TextTriangle are correct after initialization.
        """
        triangle = asciiart.TextTriangle()
        self.assertEqual(triangle.char, ['*'])
        self.assertEqual(triangle.n1, 1)
        self.assertEqual(triangle.rm, 0)
        self.assertEqual(triangle.lm, 1)
        self.assertEqual(triangle.add, 1)
        self.assertEqual(triangle.nlevels, 5)
        self.assertEqual(triangle.o, '^')
        self.assertEqual(triangle.a, '<')


    def test___str__(self):
        """Test method :meth:`plugins.asciiart.TextTriangle.__str__`

        **Tested:**

        - The returned single-character triangle string is correct.
        - The returned multicharacter triangle string is correct.
        """
        result = [
            asciiart.TextTriangle().__str__(),
            asciiart.TextTriangle(char='a b c'.split()).__str__(),
        ]
        expected = [
            '*\n**\n***\n****\n*****',
            'a\nbc\nabc\nabca\nbcabc',
        ]
        self.assertTrue(all([r==e for r, e in zip(result, expected)]))


    def test__compose_level(self):
        """Test method :meth:`plugins.asciiart.TextTriangle._compose_level`

        **Tested:**

        - The correct level is generated in case of single-character tirangles.
        - The correct level is generated in case of multicharacter triangles.
        """
        result = [
            asciiart.TextTriangle()._compose_level(10),
            asciiart.TextTriangle(char='ab')._compose_level(5),
            asciiart.TextTriangle(char='a b c'.split())._compose_level(10),
            asciiart.TextTriangle(char='a b c'.split())._compose_level(10, 1),
        ]
        expected = [
            ('* * * * * * * * * *'.split(), 0),
            ('ab ab ab ab ab'.split(), 0),
            ('a b c a b c a b c a'.split(), 1),
            ('b c a b c a b c a b'.split(), 2),
        ]
        self.assertTrue(all([r==e for r, e in zip(result, expected)]))


if __name__ == '__main__':
    unittest.main()
