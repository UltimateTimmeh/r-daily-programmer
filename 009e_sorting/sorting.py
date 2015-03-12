#!/usr/bin/env python3.4
"""
Implementation of various sorting algorithms, and tests on
various list sizes to determine which ones are more efficient.
"""

import random


def sort_insertion(_list):
    """Implementation of insertion sort.

    Algorithm:
    1) Go over all items of the list, starting at the second item (the first
       one is automatically in the correct position). The current item will be
       called the pivot.
    2) While the pivot is not at the start of the list and the item before the
       pivot is larger than the pivot, swap the pivot with the item before it.
    """
    for pivot in range(1, len(_list)):
        jj = pivot
        while jj > 0 and _list[jj-1] > _list[jj]:
            backup = _list[jj]
            _list[jj] = _list[jj-1]
            _list[jj-1] = backup
            jj -= 1
    return _list


def sort_selection(_list):
    """Implementation of selection sort.

    Algorithm:
    1) Go over all items of the list. The current item will be called the pivot.
    2) The pivot starts as being the 'smallest'.
    4) Starting at the item after the pivot, go through the remainder of the list
       and keep track of the smallest element.
    3) Once the end of the list has been reached, swap the pivot with the
       smallest element.
    """
    for pivot in range(len(_list)):
        smallest = pivot
        for jj in range(pivot+1,  len(_list)):
            if _list[jj] < _list[smallest]:
                smallest = jj
        backup = _list[pivot]
        _list[pivot] = _list[smallest]
        _list[smallest] = backup
    return _list


if __name__ == '__main__':
    nelems = 10
    elems = list(range(nelems))
    random.shuffle(elems)
    print(elems)
    elems_sorted = sort_selection(elems)
    print(elems_sorted)

# End
