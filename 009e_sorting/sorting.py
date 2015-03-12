#!/usr/bin/env python3.4
"""
Implementation of various sorting algorithms, and tests on
various list sizes to determine which ones are more efficient.
"""

import datetime
import random


def sort_insertion(_list):
    """Implementation of insertion sort.

    Algorithm:
    1) Go over all items of the list, starting at the second item (the first
       one is automatically in the correct position). The current item will be
       called the pivot, and is taken out of the list (consider its original
       space to now be empty).
    2) Start moving to the left of the pivot. Shift the encountered items one
       space to right (effectively moving the empty space to the left), but
       stop once you encounter an item that is smaller than the pivot or once
       shifting is no longer possible (i.e. the empty space reaches the start
       of the list).
    3) Place the pivot into the resulting empty space.
    4) After going over all elements in the list, the list is sorted.
    """
    for ip in range(1, len(_list)):
        pivot = _list[ip]
        il = ip
        while il > 0 and _list[il-1] > pivot:
            _list[il] = _list[il-1]
            il -= 1
        _list[il] = pivot
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
    4) After going over all elements in the list, the list is sorted.
    """
    for ip in range(len(_list)):
        smallest = ip
        for ir in range(ip+1,  len(_list)):
            if _list[ir] < _list[smallest]:
                smallest = ir
        if ip != smallest:
            pivot = _list[ip]
            _list[ip] = _list[smallest]
            _list[smallest] = pivot
    return _list


def sort_merge(_list):
    """Implementation of merge sort.

    Algorithm:
    1) Keep dividing the list in half until you reach the smallest possible size.
    2) Repeatedly merge the lists back together in pairs, meanwhile sorting the
       elements.
    3) Once all parts have been merged back together, the list is sorted.
    """
    ll = len(_list)
    if ll <= 1:
        return _list
    left = sort_merge(_list[:int(ll/2)])
    right = sort_merge(_list[int(ll/2):])
    merged = []
    il = 0
    ir = 0
    while il != len(left) and ir != len(right):
        if left[il] < right[ir]:
            merged.append(left[il])
            il += 1
        else:
            merged.append(right[ir])
            ir += 1
    return merged + left[il:] + right[ir:]


if __name__ == '__main__':
    # Create a list containing a chosen amount of numbers, and randomize.
    nelems = 10000
    elems = list(range(nelems))
    random.shuffle(elems)

    # The sorting algorithms to be considered.
    sort_names = [
        'Insertion sort',
        'Selection sort',
        'Merge sort',
        ]
    sort_funcs = [
        sort_insertion,
        sort_selection,
        sort_merge,
        ]

    # Feed the list to the sorting algorithms, time the execution and print a report.
    for sort_name,  sort_func in zip(sort_names, sort_funcs):
        elems_copy = [e for e in elems]
        ts = datetime.datetime.now()
        elems_sorted = sort_func(elems_copy)
        te = datetime.datetime.now()
        td = te - ts
        txt = [
            '\n'.join(['='*len(sort_name),  sort_name,  '='*len(sort_name)]),
            ## "Original: {0}",
            ## "Sorted: {1}",
            "Amount of elements: {2}",
            "Elapsed time: {3}",
            ]
        txt = '\n'.join(txt)
        print('\n'+txt.format(elems, elems_sorted, len(elems), td.total_seconds()))


# End
