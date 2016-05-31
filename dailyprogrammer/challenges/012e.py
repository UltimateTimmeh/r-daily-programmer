#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/012e.py

| **Challenge name:**  Permutations (reddit_, source_)
| **Challenge number:** 12
| **Difficulty:** Easy
| **Submission date:** 2012-02-20
| **Status:** Complete

Description
-----------

Write a small program that can take a string (e.g. ``'hi!'``) and print all the possible permutations
of the string::

    "hi!"
    "h!i"
    "ih!"
    "i!h"
    "!hi"
    "!ih"

Thanks to hewts for this challenge!

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 012e
    Input: hi!
    hi!
    h!i
    ih!
    i!h
    !hi
    !ih

Imported plugins
----------------

| None

Module contents
---------------
"""

from plugins import utils


def permutations(x):
    """Determine all possible permutations of a list or string.

    :param x: list or string to determine permutations of
    :type x: list or str
    :return: a list containing all possible permutations of the input
    :rtype: list(list, ...) or list(str, ...)
    """
    if len(x) == 1:
        return [x]
    perms = []
    for n, i in enumerate(x):
        if isinstance(x, list):
            i = [i]
        subx = x[:n] + x[n+1:]
        perms += [i + pp for pp in permutations(subx)]
    return perms


def run():
    """Execute the challenges.012e module."""
    x = utils.get_input("Input: ")
    print('\n'.join(permutations(x)))

