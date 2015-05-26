#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/quli5/3132012_challenge_23_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/023e.py

| **Challenge name:** Split Lists (reddit_, source_)
| **Challenge number:** 23
| **Difficulty:** Easy
| **Submission date:** 2012-03-13
| **Status:** Complete

Description
-----------

**Input**: a list

**Output**: Return the two halves as different lists.

If the input list has an odd number, the middle item can go to any of the list. Your task is to
write the function that splits a list in two halves.

Example run
-----------

::

    $ python3 dailyprogrammer.py 023e
    Length of list: 10
    Split fraction: 0.5
    Original list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Split part 1: [0, 1, 2, 3, 4]
    Split part 2: [5, 6, 7, 8, 9]

Module contents
---------------
"""


def split_list(x, f=0.5):
    """Split a list in two at a certain fraction of its length.

    :param list x: the list to split
    :param float f: split fraction, the fraction at which the list should be split, must be between
                    0. and 1. (default 0.5)
    :return: tuple containing the two parts of the split list
    :rtype: tuple(list, list)
    :raise: ValueError if the split fraction is not between 0. and 1.

    Example::

        >>> x = list(range(10))
        >>> split_list(x)
        ([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])
        >>> split_list(x, f=0.2)
        ([0, 1], [2, 3, 4, 5, 6, 7, 8, 9])
        >>> split_list(x, f=0.8)
        ([0, 1, 2, 3, 4, 5, 6, 7], [8, 9])
        >>> split_list(x, f=1.0)
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [])
    """
    if f < 0. or f > 1.:
        raise ValueError("Split fraction should be between 0. and 1. (got {})".format(f))
    mid = round(len(x)*f)
    return x[:mid], x[mid:]


def run():
    """Execute the challenges.023e module."""
    x = list(range(int(input("Length of list: "))))
    f = float(input("Split fraction: "))
    x1, x2 = split_list(x, f=f)
    print("Original list: {}".format(x))
    print("Split part 1: {}".format(x1))
    print("Split part 2: {}".format(x2))

