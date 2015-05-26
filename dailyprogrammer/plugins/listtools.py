#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/listtools.py

Collection of useful operations on lists.
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


def count_items(x, count=None):
    """Count the items in a list.

    :param list x: the list of which items must be counted
    :param dict count: dictionary to which the count will be added (default {})
    :return: the dictionary to which the count was added
    :rtype: dict

    Example::

        >>> count = count_items(['a', 'b', 'b', 'c', 'c', 'c', 'a'])
        >>> count
        {'a': 2, 'b': 2, 'c': 3}
        >>> count = count_items(['d', 'd', 'e', 'e', 'a', 'e', 'e'])
        >>> count
        {'a': 3, 'b': 2, 'c': 3, 'd': 2, 'e': 4}
    """
    if count is None:
        count = {}
    for xi in x:
        if xi in count:
            count[xi] += 1
        else:
            count[xi] = 1
    return count


def most_prevalent_items(x):
    """Determine the most prevalent item(s) in a list.

    :param list x: the list of which the most prevalent item(s) must be determined
    :return: list containing the most prevalent item(s)
    :rtype: list

    Example::

        >>> most_prevalent_items(['a', 'b', 'b', 'c'])
        ['b']
        >>> most_prevalent_items(['a', 'a', 'b', 'b', 'c'])
        ['a', 'b']
    """
    count = count_items(x)
    maxcount = 0
    maxitems = []
    s = set(x)
    for xi in s:
        if count[xi] > maxcount:
            maxcount = count[xi]
            maxitems = [xi]
        elif count[xi] == maxcount:
            maxitems.append(xi)
        print(count)
        print(maxcount)
        print(maxitems)
    return maxitems

