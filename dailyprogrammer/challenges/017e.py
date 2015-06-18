#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/017e.py

| **Challenge name:**  Text Triangle (reddit_, source_)
| **Challenge number:** 17
| **Difficulty:** Easy
| **Submission date:** 2012-03-04
| **Status:** Complete

Description
-----------

Write an application which will print a triangle of stars of user-specified height, with each
line having twice as many stars as the last. sample output::

    @
    @@
    @@@@

| **Hint**: In many languages, the '+' sign concatenates strings.
| **Bonus features**: print the triangle in reverse, print the triangle right justified.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 017e
    Amount of triangle levels: 6

    Normal triangle:
    *
    **
    ****
    ********
    ****************
    ********************************

    Reversed triangle:
    ********************************
    ****************
    ********
    ****
    **
    *

    Reversed triangle with right alignment:
    ********************************
                    ****************
                            ********
                                ****
                                  **
                                   *

Module contents
---------------
"""

from plugins.enhancedstring import EnhancedString


class TextTriangle(object):
    """A class representing an ASCII text triangle.

    Formula for the amount of characters in each level of the triangle::

        first level:      nchars[1] = n1
        following levels: nchars[i] = nchars[i-1]*rm + i*lm + add

    :param str char: character out of which the triangle is composed (default '*')
    :param int s: amount of characters in the first level (default 1)
    :param int rm: recursive multiplication factor, see formula for more info (default 0)
    :param int lm: level multiplication factor, see formula for more info (default 1)
    :param int add: addition factor, see formula for more info (default 1)
    :param int nlevels: amount of levels in the triangle (default 5)
    :param str o: order of the triangle, '^' for ascending, 'v' for descending (default '^')
    :param str a: alignment of the triangle, '<' for left, '^' for center, '>' for right
                  (default '<')

    Example::

        >>> triangle = TextTriangle()
        >>> print(triangle)
        *
        **
        ***
        ****
        *****
    """


    def __init__(self, char='*', n1=1, rm=0, lm=1, add=1, nlevels=5, o='^', a='<'):
        """Create a new text triangle."""
        if o not in '^v':
            raise ValueError("Invalid triangle order: '{}'".format(o))
        if a not in '<^>':
            raise ValueError("Invalid triangle alignment: '{}'".format(a))
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
        # Compose the triangle.
        triangle = [self.char*self.n1]
        for ii in range(1, self.nlevels):
            nelems = len(triangle[-1])*self.rm + ii*self.lm + self.add
            triangle += [self.char*nelems]

        # Format the triangle.
        if self.o == 'v':
            triangle = triangle [::-1]
        triangle = EnhancedString('\n'.join(triangle))
        triangle.align(self.a)
        return triangle.__str__()


def run():
    """Execute the challenges.017e module."""
    nlevels = int(input("Amount of triangle levels: "))
    triangle = TextTriangle(rm=2, lm=0, add=0, nlevels=nlevels)
    print("\nNormal triangle:\n{}".format(triangle))
    triangle.o = 'v'
    print("\nReversed triangle:\n{}".format(triangle))
    triangle.a = '>'
    print("\nReversed triangle with right alignment:\n{}".format(triangle))

