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

| :mod:`plugins.listtools`

Module contents
---------------
"""

from plugins import listtools as lt
from plugins import utils


def run():
    """Execute the challenges.012e module."""
    x = utils.get_input("Input: ")
    print('\n'.join(lt.permutations(x)))

