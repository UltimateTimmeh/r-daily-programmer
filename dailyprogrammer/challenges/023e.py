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

    $ python3 dailyprogrammer.py execute 023e
    Length of list: 10
    Split fraction: 0.5
    Original list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Split part 1: [0, 1, 2, 3, 4]
    Split part 2: [5, 6, 7, 8, 9]

Imported plugins
----------------

| :mod:`plugins.listtools`

Module contents
---------------
"""

from plugins import listtools as lt
from plugins import utils


def run():
    """Execute the challenges.023e module."""
    x = list(range(int(utils.get_input("Length of list: "))))
    f = float(utils.get_input("Split fraction: "))
    x1, x2 = lt.split_list(x, f=f)
    print("Original list: {}".format(x))
    print("Split part 1: {}".format(x1))
    print("Split part 2: {}".format(x2))

