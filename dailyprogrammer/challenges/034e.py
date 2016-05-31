#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/034e.py

| **Challenge name:** Sum Of Squares (reddit_, source_)
| **Challenge number:** 34
| **Difficulty:** Easy
| **Submission date:** 2012-03-31
| **Status:** Complete

Description
-----------

A very basic challenge. In this challenge, the input is 3 numbers. The output is the sum of the
squares of the two larger numbers. Your task is to write the indicated challenge.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 034e
    Provide three numbers, separated with a comma: 9,2,6
    The largest two numbers are [6, 9] and the sum of their squares is 117.

Imported plugins
----------------

| None

Module contents
---------------
"""

from plugins import utils


def sumsq(nrs):
    """Return the sum of the squares of the numbers in a list.

    :param nrs: list containing the numbers
    :type nrs: list(int or float, ...)
    :return: the sum of the squares of all numbers in the list
    :rtype: int or float

    Example::

        >>> sumsq([2, 3, 4])
        29
    """
    return sum([nr**2 for nr in nrs])


def run():
    """Execute the challenges.034e module."""
    inputmsg = "Provide three numbers, separated with a comma: "
    nrs = sorted([int(nr) for nr in utils.get_input(inputmsg).split(',')])[-2:]
    outputmsg = "The largest two numbers are {} and the sum of their squares is {}."
    print(outputmsg.format(nrs, sumsq(nrs)))

