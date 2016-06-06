#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/ti5jc/5112012_challenge_51_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/051e.py

| **Challenge name:** Combinations (reddit_, source_)
| **Challenge number:** 51
| **Difficulty:** Easy
| **Submission date:** 2012-05-11
| **Status:** Complete

Description
-----------

Write a program that given an array A and a number N, generates all combinations of items in A of
length N.

That is, if you are given the array ``[1, 2, 3, 4, 5]`` and ``3``, you're supposed to generate::

    [1,2,3]
    [1,2,4]
    [1,2,5]
    [1,3,4]
    [1,3,5]
    [1,4,5]
    [2,3,4]
    [2,3,5]
    [2,4,5]
    [3,4,5]

Note that order doesn't matter when counting combinations, both ``[1, 2, 3]`` and ``[3, 2, 1]`` are
considered the same. Order also doesn't matter in the output of the combinations, as long as you
generate all of them, you don't have to worry about what order they pop out. You can also assume
that every element of the array is distinct.

Example run
-----------

::

    Input list: [1, 2, 3, 4, 5]
    Non-repeating combinations of length 3:
    [1, 2, 3]
    [1, 2, 4]
    [1, 2, 5]
    [1, 3, 4]
    [1, 3, 5]
    [1, 4, 5]
    [2, 3, 4]
    [2, 3, 5]
    [2, 4, 5]
    [3, 4, 5]

Imported plugins
----------------

| :mod:`plugins.listtools`

Module contents
---------------
"""

from plugins import listtools as lt


def run():
    """Execute the challenges.051e module."""
    x = list(range(1, 6))
    length = 3
    print("Input list:", x)
    print("Non-repeating combinations of length {}:".format(length))
    for cc in lt.combinations(x, length, repeat=False):
        print(cc)

