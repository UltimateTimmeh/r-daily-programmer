#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/reago/3262012_challenge_30_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/030e.py

| **Challenge name:** Find Sum Pairs (reddit_, source_)
| **Challenge number:** 30
| **Difficulty:** Easy
| **Submission date:** 2012-03-26
| **Status:** Complete

Description
-----------

Write a program that takes a list of integers and a target number and determines if any two integers
in the list sum to the target number. If so, return the two numbers. If not, return an indication
that no such integers exist.

Edit : Note the "Intermediate" challenge #30 has been changed. Thank you!

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 030e
    Amount of elements in list: 10
    Minimum element value: 0
    Maximum element value: 1
    Choose a target: 3
    Randomly generated list: [0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    Target: 3
    There are no pairs in this list of which the sum equals the target!

::

    $ python3 dailyprogrammer.py execute 030e
    Amount of elements in list: 20
    Minimum element value: 0
    Maximum element value: 10
    Choose a target: 10
    Randomly generated list: [0, 10, 10, 8, 8, 7, 4, 4, 3, 0, 3, 4, 1, 4, 9, 6, 9, 8, 9, 5]
    Target: 10
    Pairs in this list of which the sum equals the target:
    [(0, 10), (0, 10), (1, 9), (3, 7), (4, 6)]

Imported plugins
----------------

| None

Module contents
---------------
"""

import random

from plugins import utils


def find_target_pairs(x, target):
    """Find all pairs of integers in a list whose sum equals a certain target.

    In this implementation, if a pair has been found, both elements belonging to the pair
    will be 'depleted' from the list. This means those elements cannot be used for other pairs
    (see the second example). This also means an element cannot pair with itself (see the third
    example). If a duplicate pair has been found, it will simply be appended to the result
    and be present more than once (see the fourth example).

    Note that in this implementation, the list is first sorted. As such, the order of the
    elements in the output is not preserved (see the fifth example). The list is not sorted
    in-place, however, so the order of the input list is preserved.

    :param x: list containing integers
    :type x: list(int, ...)
    :param int target: the requested target
    :return: list of integer pairs whose sum equals the target
    :rtype: list(tuple(int, int), ...)

    Example::

        >>> find_target_pairs([1, 2, 3, 4, 5], 6)
        [(1, 5), (2, 4)]
        >>> find_target_pairs([1, 1, 3], 4)  ## Note how the second 1 remains unpaired because the single 3 was already paired with the first 1.
        [(1, 3)]
        >>> find_target_pairs([2], 4)  ## Note how no pairs are found because elements cannot pair with themselves.
        []
        >>> find_target_pairs([1, 3, 3, 1], 4)  ## Note how the pair (1, 3) is found twice.
        [(1, 3), (1, 3)]
        >>> find_target_pairs([3, 1], 4)  ## Note the order of the elements in the input list and in the found pair.
        [(1, 3)]
    """
    x = sorted(x)
    p = []
    i, j = 0, len(x)-1
    while i < j:
        if x[i] + x[j] == target:
            p.append((x[i], x[j]))
            i += 1
            j -= 1
        elif x[i] + x[j] > target:
            j -= 1
        else:
            i += 1
    return p

    ## The algorithm in words:
    ##
    ## First sort your list.
    ## Now consider the two outer elements of this sorted list:
    ##
    ##   If the sum of the outer elements is equal to the target, then you have found a pair.
    ##   This pair can be added to the results and both elements can be removed from the
    ##   list (since an element cannot be used in more than one pair).
    ##
    ##   If the sum of the outer elements is bigger than the target, then you can 'remove' the
    ##   last (biggest) element. This is because, since the list is sorted, there is no element
    ##   in the list smaller than the first. Thus there is no element in the list with which the
    ##   last element can be paired to make the sum small enough to be equal to the target.
    ##
    ##   If the sum of the outer elements is smaller than the target, then you can 'remove' the
    ##   first (smallest) element. This is because, since the list is sorted, there is no element
    ##   in the list bigger than the last. Thus there is no element in the list with which the
    ##   first element can be paired to make the sum big enough to be equal to the target.
    ##
    ## By reducing your list like this, you will always go to the next lower sum (in case the
    ## sum was too big) or the next higher sum (in case the sum was too low), and all pairs
    ## are guaranteed to be found.


def run():
    """Execute the challenges.030e module."""
    # Generate random list (with repetition).
    nelems = int(utils.get_input("Amount of elements in list: "))
    minval = int(utils.get_input("Minimum element value: "))
    maxval = int(utils.get_input("Maximum element value: "))
    if minval > maxval:
        minval, maxval = maxval, minval
    x = [random.randrange(minval, maxval+1) for n in range(nelems)]

    # Choose a target, find and print pairs.
    target = int(utils.get_input("Choose a target: "))
    p = find_target_pairs(x, target)
    print("Randomly generated list: {}".format(x))
    print("Target: {}".format(target))
    if len(p) == 0:
        print("There are no pairs in this list of which the sum equals the target!")
    else:
        print("Pairs in this list of which the sum equals the target:\n{}".format(p))

