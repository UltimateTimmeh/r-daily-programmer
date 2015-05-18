#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/014e.py

| **Challenge name:**  Block Invert (reddit_, source_)
| **Challenge number:** 14
| **Difficulty:** Easy
| **Submission date:** 2012-02-23
| **Status:** Complete

Description
-----------

*Input:** List of elements and a block size k or some other variable of your choice.

**Output:** Return the list of elements with every block of k elements reversed, starting from the
beginning of the list.

**Example:** Given the list ``[12, 24, 32, 44, 55, 66]`` and the block size ``k = 2``, the result is
``[24, 12, 44, 32, 66, 55]``.

Example run
-----------

::

    $ python3 dailyprogrammer.py 014e
    Input: [12, 24, 32, 44, 55, 66]
    Result of inversion in blocks with size 2: [24, 12, 44, 32, 66, 55]

Module contents
---------------
"""


def blockinvert(x, k):
    """Invert items in a list in blocks of arbitrary size.

    :param list x: the list
    :param int k: block size
    :return: the list with items inverted in blocks with the specified size
    :rtype: list
    """
    nb = int(len(x)/k) + 1
    xn = [list(x[ii*k:(ii+1)*k][::-1]) for ii in range(nb)]
    xn = sum(xn, [])
    return xn


def run():
    """Execute the challenges.014e module."""
    x = [12, 24, 32, 44, 55, 66]
    k = 2
    xn = blockinvert(x, k)
    print("Input: {}".format(x))
    print("Result of inversion in blocks with size {}: {}".format(k, xn))

