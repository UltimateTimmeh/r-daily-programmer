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


def merge_lists(x, y):
    """Merge two lists.

    This function is different from concatenating two lists. The first list is subtracted
    from the second list, and the remaining difference is appended to the first list. The
    output will always contain the elements in both lists the same amount of times as its
    maximum prevalence across the individual lists. In other words: if both lists contain
    the character ``'a'`` once, then the output will also contain the character ``'a'`` once.
    If one of the lists contains the character ``'a'`` once, and the other contains it three,
    times, then the output will also contain it three times.

    Note that this operation is not commutative: ``merge_lists(x, y)`` is not the same as
    ``merge_lists(y, x)``.

    :param list x: the first list
    :param list y: the second list
    :return: the merged list
    :rtype: list

    Example::

        >>> merge_lists(['a'], ['a'])
        ['a']
        >>> merge_lists(['a'], ['b'])
        ['a', 'b']
        >>> merge_lists(['a'], ['a', 'a'])
        ['a', 'a']
        >>> merge_lists(['a', 'b'], ['a', 'c'])  ## Operation is not commutative.
        ['a', 'b', 'c']
        >>> merge_lists(['a', 'c'], ['a', 'b'])  ## Operation is not commutative.
        ['a', 'c', 'b']
    """
    y_copy = [yi for yi in y]
    [y_copy.remove(xi) for xi in x if xi in y_copy]
    return x + y_copy


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

