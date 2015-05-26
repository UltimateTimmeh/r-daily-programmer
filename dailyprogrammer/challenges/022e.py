#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/022e.py

| **Challenge name:**  Merge Lists (reddit_, source_)
| **Challenge number:** 22
| **Difficulty:** Easy
| **Submission date:** 2012-03-10
| **Status:** Complete

Description
-----------

Write a program that will compare two lists, and append any elements in the second list that
doesn't exist in the first.

**input:** ``["a","b","c",1,4,], ["a", "x", 34, "4"]``

**output:** ``["a", "b", "c",1,4,"x",34, "4"]``

Example run
-----------

::

    Challenge example:
    Input: ['a', 'b', 'c', 1, 4], ['a', 'b', 'x', 34, '4']
    Output: ['a', 'b', 'c', 1, 4, 'x', 34, '4']
    Extra example:
    Input: ['a', 'b', 'c', 1, 4], ['a', 'b', 'x', 34, '4', 'a']
    Output: ['a', 'b', 'c', 1, 4, 'x', 34, '4', 'a']

.. note:: Note how in the second example, because there is only one 'a' in the first list, and
          there are two 'a's in the second list, an extra 'a' is appended to the output. This means
          my implementation is able to 'merge' two lists instead of merely appending a single
          instance of each missing item.

Module contents
---------------
"""

from plugins.listtools import merge_lists


def run():
    """Execute the challenges.022e module."""
    examples = [
        ("Challenge", ['a', 'b', 'c', 1, 4], ['a', 'b', 'x', 34, '4']),
        ("Extra", ['a', 'b', 'c', 1, 4], ['a', 'b', 'x', 34, '4', 'a']),
    ]
    for example in examples:
        x = example[1]
        y = example[2]
        xnew = merge_lists(x, y)
        print("{} example:".format(example[0]))
        print("Input: {}, {}".format(x, y))
        print("Output: {}".format(xnew))

