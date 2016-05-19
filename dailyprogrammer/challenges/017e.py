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

from plugins import asciiart as aa
from plugins import utils


def run():
    """Execute the challenges.017e module."""
    nlevels = int(utils.get_input("Amount of triangle levels: "))
    triangle = aa.TextTriangle(rm=2, lm=0, add=0, nlevels=nlevels)
    print("\nNormal triangle:\n{}".format(triangle))
    triangle.o = 'v'
    print("\nReversed triangle:\n{}".format(triangle))
    triangle.a = '>'
    print("\nReversed triangle with right alignment:\n{}".format(triangle))

