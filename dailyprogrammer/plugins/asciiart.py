#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/asciiart.py

Classes and functions for printing ASCII art (source_).
"""

from plugins.enhancedstring import EnhancedString


class TextTriangle(object):
    """An ASCII text triangle.

    Formula for the amount of characters in each level of the triangle::

        first level:      nchars[1] = n1
        following levels: nchars[i] = nchars[i-1]*rm + i*lm + add

    The triangle can be constructed of a string consisting of a single character (see the first
    example), a string consisting of multiple characters (see the second example) or a list of such
    strings. In the last case, iteration through the list of characters is used to compose the
    triangle. When the end of the list of characters is reached, it loops back to the beginning (see
    the third example).

    :param char: character(s) out of which the triangle is composed (default '*')
    :type char: str or list(str, ...)
    :param int s: amount of characters in the first level (default 1)
    :param int rm: recursive multiplication factor, see formula for more info (default 0)
    :param int lm: level multiplication factor, see formula for more info (default 1)
    :param int add: addition factor, see formula for more info (default 1)
    :param int nlevels: amount of levels in the triangle (default 5)
    :param str o: order of the triangle, '^' for ascending, 'v' for descending (default '^')
    :param str a: alignment of the triangle, '<' for left, '^' for center, '>' for right
                  (default '<')
    :raise: ValueError if triangle order invalid.
    :raise: ValueError if triangle alignment invalid.

    Example::

        >>> print(TextTriangle())
        *
        **
        ***
        ****
        *****
        >>> print(TextTriangle(char='abc.'))
        abc.
        abc.abc.
        abc.abc.abc.
        abc.abc.abc.abc.
        abc.abc.abc.abc.abc.
        >>> print(TextTriangle(char=['a', 'b', 'c']))
        a
        bc
        abc
        abca
        bcabc
    """


    def __init__(self, char='*', n1=1, rm=0, lm=1, add=1, nlevels=5, o='^', a='<'):
        """Create a new text triangle."""
        if o not in '^v':
            raise ValueError("Invalid triangle order: '{}'".format(o))
        if a not in '<^>':
            raise ValueError("Invalid triangle alignment: '{}'".format(a))
        if isinstance(char, str):
            char = [char]
        self.char = char
        self.nlevels = nlevels
        self.n1 = n1
        self.rm = rm
        self.lm = lm
        self.add = add
        self.o = o
        self.a = a


    def __str__(self):
        """Format a text triangle as a string."""
        level, ci = self._compose_level(self.n1)
        triangle = [level]
        for ii in range(1, self.nlevels):
            nelems = len(triangle[-1])*self.rm + ii*self.lm + self.add
            level, ci = self._compose_level(nelems, ci)
            triangle.append(level)
        triangle = [''.join(lvl) for lvl in triangle]

        if self.o == 'v':
            triangle = triangle [::-1]
        triangle = EnhancedString('\n'.join(triangle))
        triangle.align(self.a)
        return triangle.__str__()


    def _compose_level(self, nelems, ci=0):
        """Compose a multicharacter triangle level.

        The generated level will contain the given amount of elements, taken in sequential order
        from the list of characters. For continuation of the character sequence between levels, the
        index of the first character can be given.
        """
        level = []
        for i in range(nelems):
            level.append(self.char[ci])
            ci = (ci+1) % len(self.char)
        return level, ci


class Tile(object):
    """A tile, which is a basic element of a checkered grid.

    :param int x: character length in the x-direction (width) of the tile
    :param int y: character length in the y-direction (height) of the tile
    :param str char: character out of which the tile is composed (default '#')

    Example::

        >>> tile = Tile(5, 3, 'x')
        >>> print(tile)
        xxxxx
        xxxxx
        xxxxx
        >>> tile.char = 'O'
        >>> print(tile)
        OOOOO
        OOOOO
        OOOOO
    """


    def __init__(self, x, y, char='#'):
        """Initialize a new tile."""
        self.x = x
        self.y = y
        self.char = char


    def __str__(self):
        """Format a string representation of the tile."""
        return '\n'.join(self.lines)


    @property
    def lines(self):
        """Return the list of lines out of which the tile is composed.

        :return: the list of lines out of which the tile is composed
        :rtype: list(str, ...)

        Example::

            >>> tile = Tile(5, 3)
            >>> tile.lines
            ['#####', '#####', '#####']
        """
        return [self.char*self.x]*self.y


class CheckeredGrid(object):
    """A checkered grid, composed of alternating tiles of (possibly) different characters.

    :param int x: amount of tiles in the x-direction of the grid
    :param int y: amount of tiles in the y-direction of the grid
    :param int tx: tile width
    :param int ty: tile height
    :param str chars: list of characters out of which tiles are alternatingly composed

    Example::

        >>> grid = CheckeredGrid(8, 3, 3, 2, ['.', '#'])
        >>> print(grid)
        ...###...###...###...###
        ...###...###...###...###
        ###...###...###...###...
        ###...###...###...###...
        ...###...###...###...###
        ...###...###...###...###
        >>> grid = CheckeredGrid(8, 3, 3, 2, ['.', 'x', 'O'])
        >>> print(grid)
        ...xxxOOO...xxxOOO...xxx
        ...xxxOOO...xxxOOO...xxx
        xxxOOO...xxxOOO...xxxOOO
        xxxOOO...xxxOOO...xxxOOO
        OOO...xxxOOO...xxxOOO...
        OOO...xxxOOO...xxxOOO...
    """


    def __init__(self, x, y, tx, ty, chars):
        """Initialize a new checkered grid."""
        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty
        self.chars = chars


    def __str__(self):
        """Format a string representation of the checkered grid."""
        chars = self.chars
        allrows = []
        for yi in range(self.y):
            tiles = [Tile(self.tx, self.ty, chars[xi%len(chars)]) for xi in range(self.x)]
            tilerows = [''.join([tile.lines[tyi] for tile in tiles]) for tyi in range(self.ty)]
            allrows += tilerows
            chars = chars[1:] + chars[:1]
        return '\n'.join(allrows)

