#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/031e.py

| **Challenge name:** Base 26 Multiplication (reddit_, source_)
| **Challenge number:** 31
| **Difficulty:** Easy
| **Submission date:** 2012-03-27
| **Status:** Complete

Description
-----------

Write a function that takes two base-26 numbers in which digits are represented by letters with
``A=0, B=1, … Z=25`` and returns their product using the same notation. As an example,
``CSGHJ * CBA = FNEUZJA``.

Your task is to write the base-26 multiplication function.

Try to be very efficient in your code!

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 031e
    First base 26 number (A - Z): CSGHJ
    Second base 26 number (A - Z): CBA
    Multiplication of both numbers: FNEUZJA

Imported plugins
----------------

| :mod:`plugins.enhancedint`

Module contents
---------------

| *var* challenges.031e.\ **map_nrs2ltrs** *(dict(int: str, ...))*
|     dictionary mapping the numbers 0 - 25 to the letters A - Z

| *var* challenges.031e.\ **map_ltrs2nrs** *(dict(int: str, ...))*
|     dictionary mapping the letters A - Z to the numbers 0 - 25
"""

from plugins import enhancedint as ei
from plugins import utils

map_nrs2ltrs = {
    nr: ltr for nr, ltr in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
}
map_ltrs2nrs = {
    ltr: nr for nr, ltr in map_nrs2ltrs.items()
}


def run():
    """Execute the challenges.031e module."""
    nr1 = utils.get_input('First base 26 number (A - Z): ').upper()
    nr2 = utils.get_input('Second base 26 number (A - Z): ').upper()
    nr1 = ei.EnhancedInt([map_ltrs2nrs[char] for char in nr1], 26)
    nr2 = ei.EnhancedInt([map_ltrs2nrs[char] for char in nr2], 26)
    result = ''.join([map_nrs2ltrs[digit] for digit in (nr1 * nr2).digits])
    print("Multiplication of both numbers: {}".format(result))

