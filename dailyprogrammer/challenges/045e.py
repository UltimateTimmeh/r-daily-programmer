#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/sv6lw/4272012_challenge_45_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/045e.py

| **Challenge name:** Checkered Grid (reddit_, source_)
| **Challenge number:** 45
| **Difficulty:** Easy
| **Submission date:** 2012-04-27
| **Status:** Complete

Description
-----------

Your challenge today is to write a program that can draw a checkered grid (like a chessboard) to any
dimension. For instance, a 3 by 8 board might look like this::

    *********************************
    *   *###*   *###*   *###*   *###*
    *   *###*   *###*   *###*   *###*
    *   *###*   *###*   *###*   *###*
    *********************************
    *###*   *###*   *###*   *###*   *
    *###*   *###*   *###*   *###*   *
    *###*   *###*   *###*   *###*   *
    *********************************
    *   *###*   *###*   *###*   *###*
    *   *###*   *###*   *###*   *###*
    *   *###*   *###*   *###*   *###*
    *********************************

Yours doesn't have to look like mine, you can make it look any way you want (now that I think of it,
mine looks kinda bad, actually). Also try to make it scalable, so that if you want to make a 2 by 5
board, but with bigger squares, it would print out::

    *******************************
    *     *#####*     *#####*     *
    *     *#####*     *#####*     *
    *     *#####*     *#####*     *
    *     *#####*     *#####*     *
    *     *#####*     *#####*     *
    *******************************
    *#####*     *#####*     *#####*
    *#####*     *#####*     *#####*
    *#####*     *#####*     *#####*
    *#####*     *#####*     *#####*
    *#####*     *#####*     *#####*
    *******************************

Have fun!

Example run
-----------

::

    Amount of tiles along the width > 8
    Amount of tiles along the height > 8
    Tile character width > 3
    Tile character height > 2
    Tile characters (separated with space) > ░ █
    ░░░███░░░███░░░███░░░███
    ░░░███░░░███░░░███░░░███
    ███░░░███░░░███░░░███░░░
    ███░░░███░░░███░░░███░░░
    ░░░███░░░███░░░███░░░███
    ░░░███░░░███░░░███░░░███
    ███░░░███░░░███░░░███░░░
    ███░░░███░░░███░░░███░░░
    ░░░███░░░███░░░███░░░███
    ░░░███░░░███░░░███░░░███
    ███░░░███░░░███░░░███░░░
    ███░░░███░░░███░░░███░░░
    ░░░███░░░███░░░███░░░███
    ░░░███░░░███░░░███░░░███
    ███░░░███░░░███░░░███░░░
    ███░░░███░░░███░░░███░░░

Module contents
---------------
"""

from plugins import asciiart as aa
from plugins import utils


def run():
    """Execute the challenges.045e module."""
    x = int(utils.get_input("Amount of tiles along the width > "))
    y = int(utils.get_input("Amount of tiles along the height > "))
    tx = int(utils.get_input("Tile character width > "))
    ty = int(utils.get_input("Tile character height > "))
    chars = utils.get_input("Tile characters (separated with space) > ").split()
    grid = aa.CheckeredGrid(x, y, tx, ty, chars)
    print(grid)

