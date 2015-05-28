#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/listtools.py

Collection of useful operations on lists (source_).
"""

import copy


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


def count_items(x, counts=None):
    """Count the items in a list.

    Note that, when providing a dictionary to which the count should be added, a deep copy of this
    dictionary is made and returned. The provided dictionary is not updated in-place!

    :param list x: the list of which items must be counted
    :param counts: dictionary to which the item counts will be added, if None a new dictionary is
                   created (default None)
    :type counts: None or dict
    :return: a deep copy of the provided dictionary, with updated counts for the items in the list
    :rtype: dict

    Example::

        >>> counts = count_items(['a', 'b', 'b', 'c', 'c', 'c', 'a'])
        >>> counts
        {'b': 2, 'a': 2, 'c': 3}
        >>> count_items(['d', 'd', 'e', 'e', 'a', 'e', 'e'], counts=counts)  ## The counts are added to the provided dictionary
        {'b': 2, 'e': 4, 'd': 2, 'a': 3, 'c': 3}
        >>> counts  ## But the provided dictionary was not updated in-place!
        {'b': 2, 'a': 2, 'c': 3}
    """
    if counts is None:
        counts = {}
    else:
        counts = copy.deepcopy(counts)
    for xi in x:
        if xi in counts:
            counts[xi] += 1
        else:
            counts[xi] = 1
    return counts


def most_prevalent_items(x):
    """Determine the most prevalent item(s) in a list.

    :param list x: the list of which the most prevalent item(s) must be determined
    :return: set containing the most prevalent item(s)
    :rtype: set

    Example::

        >>> most_prevalent_items(['a', 'b', 'b', 'c'])
        {'b'}
        >>> most_prevalent_items(['a', 'a', 'b', 'b', 'c'])
        {'a', 'b'}
    """
    counts = count_items(x)
    maxcount = 0
    maxitems = set()
    for item, count in counts.items():
        if count > maxcount:
            maxcount = count
            maxitems = set(item)
        elif count == maxcount:
            maxitems.add(item)
    return maxitems


def find_first_duplicate(x):
    """Find the first duplicate item in a list.

    :param list x: the list to find the first duplicate item of
    :return: the first duplicate item or None if there are no duplicate items
    :rtype: None or object

    Example::

        >>> print(find_first_duplicate([0, 1, 2, 3, 4]))
        None
        >>> find_first_duplicate([0, 1, 2, 3, 4, 2])
        2
        >>> find_first_duplicate([0, 1, 2, 3, 3, 4, 2])
        3
    """
    counts = set()
    for xi in x:
        if xi in counts:
            return xi
        counts.add(xi)

