#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/schtf/4162012_challenge_40_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/040e.py

| **Challenge name:** Alternative Counting (reddit_, source_)
| **Challenge number:** 40
| **Difficulty:** Easy
| **Submission date:** 2012-04-16
| **Status:** Complete

Description
-----------

Print the numbers from 1 to 1000 without using any loop or conditional statements.

Don’t just write the printf() or cout statement 1000 times.

Be creative and try to find the most efficient way!

Source: `stackexchange.com <http://www.stackexchange.com>`_

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 040e
    Start of printed range: 1
    End of printed range: 1001
    Counting step: 1
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000,

Module contents
---------------
"""


def print_range(n1, n2=None, step=1):
    """Print the defined range of integers.

    This function doesn't use loops or conditional statements (apart from those used for parsing the
    arguments).

    :param int n1: end of the range if n2 is None, start of the range otherwise
    :param n2: None or end of the range (default None)
    :type n2: None or int
    :param int step: incrementation step of the count (default 1)

    Example::

        >>> print_range(5)
        0, 1, 2, 3, 4,
        >>> print_range(5, 10)
        5, 6, 7, 8, 9,
        >>> print_range(10, step=2)
        0, 2, 4, 6, 8,
        >>> print_range(10, 5, step=-1)
        10, 9, 8, 7, 6,
    """
    if n2 is None:
        start = 0
        end = n1
    else:
        start = n1
        end = n2
    i = start
    exec("print(i, end=', '); i += {}; ".format(step) * ((end-start)//step))
    print('')


def run():
    """Execute the challenges.040e module."""
    start = int(input("Start of printed range: "))
    end = int(input("End of printed range: "))
    step = int(input("Counting step: "))
    print_range(start, end, step)

