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


class TestTile(unittest.TestCase):
    """Unit tests for class :func:`plugins.asciiart.Tile`."""


    def test___init__(self):
        """Test method :meth:`plugins.asciiart.Tile.__init__`

        **Tested:**

        - The attributes of a Tile are correct after initialization.
        """
        tile = asciiart.Tile(3, 2, '#')
        self.assertEqual(tile.x, 3)
        self.assertEqual(tile.y, 2)


    def test___str__(self):
        """Test method :meth:`plugins.asciiart.Tile.__str__`

        **Tested:**

        - The returned tile string is correct.
        """
        tile = asciiart.Tile(3, 2, '#')
        result = tile.__str__()
        expected = '###\n###'
        self.assertEqual(result, expected)


    def test_lines(self):
        """Test method :meth:`plugins.asciiart.Tile.lines`

        **Tested:**

        - The returned list of tile lines is correct.
        """
        tile = asciiart.Tile(3, 2, '#')
        result = tile.lines
        expected = ['###', '###']
        self.assertEqual(result, expected)


class TestCheckeredGrid(unittest.TestCase):
    """Unit tests for class :func:`plugins.asciiart.CheckeredGrid`."""


    def test___init__(self):
        """Test method :meth:`plugins.asciiart.CheckeredGrid.__init__`

        **Tested:**

        - The attributes of a CheckeredGrid are correct after initialization.
        """
        grid = asciiart.CheckeredGrid(8, 3, 3, 2, ['.', '#'])
        self.assertEqual(grid.x, 8)
        self.assertEqual(grid.y, 3)
        self.assertEqual(grid.tx, 3)
        self.assertEqual(grid.ty, 2)
        self.assertEqual(grid.chars, ['.', '#'])


    def test___str__(self):
        """Test method :meth:`plugins.asciiart.CheckeredGrid.__str__`

        **Tested:**

        - The returned checkered grid string is correct.
        """
        grid = asciiart.CheckeredGrid(8, 3, 3, 2, ['.', '#'])
        result = grid.__str__()
        expected = ("...###...###...###...###\n...###...###...###...###\n"
                    "###...###...###...###...\n###...###...###...###...\n"
                    "...###...###...###...###\n...###...###...###...###")
        self.assertEqual(result, expected)

        grid = asciiart.CheckeredGrid(8, 3, 3, 2, ['.', 'x', 'O'])
        result = grid.__str__()
        expected = ("...xxxOOO...xxxOOO...xxx\n...xxxOOO...xxxOOO...xxx\n"
                    "xxxOOO...xxxOOO...xxxOOO\nxxxOOO...xxxOOO...xxxOOO\n"
                    "OOO...xxxOOO...xxxOOO...\nOOO...xxxOOO...xxxOOO...")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
