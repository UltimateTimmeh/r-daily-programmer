#!/usr/bin/env python3.4
"""
Implementation of various sorting algorithms, and tests on
various list sizes to determine which ones are more efficient.
"""

import datetime
import random

###
### SIMPLE SORTING ALGORITHMS
###


def sort_insertion(_list):
    """Implementation of insertion sort.

    NOTE: This implementation sorts the input list in-place!

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

    NOTE: This implementation sorts the input list in-place!

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


###
### EFFICIENT SORTING ALGORITHMS
###


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


def sort_quick(_list,  lo=0,  hi=None):
    """Implentation of quick sort.

    NOTE: This implementation sorts the input list in-place!

    Algorithm:
    1) Determine a pivot element (choice is arbitrary, but different methods of
       determining the pivot can have a difference in the average efficiency of the
       algorithm).
    2) Reorder the list so all items smaller than the pivot come before it, and all
       items larger than the pivot come after it. Once this is done, the pivot is
       automatically in the correct position.
    3) Recursively apply this algorithm to the lower and higher partitions. The
       base case of the recursion is a partition with one or no elements.
    """
    if hi is None:  ## Starting condition.
        hi = len(_list) - 1
    if lo >= hi:
        return _list
    pi = lo + int((hi-lo)/2)  ## This prevents overflow if lo + hi would be too large.
    pivot = _list[pi]
    _list[pi] = _list[hi]
    _list[hi] = pivot
    pi = lo
    for li in range(lo,  hi):
        if _list[li] < pivot:
            backup = _list[pi]
            _list[pi] = _list[li]
            _list[li] = backup
            pi += 1
    _list[hi] = _list[pi]
    _list[pi] = pivot
    sort_quick(_list,  lo,  pi-1)
    sort_quick(_list,  pi+1,  hi)
    return _list


def sift_down(_list, start, end):
    """Restore list heap structure.

    Sift down the node at index 'start' to the proper place such that all nodes
    below the start index are in heap order.
    """
    root = start
    while root*2+1 <= end:  ## While the root has at least one child.
        child = root*2+1  ## Left child.
        swap = root  ## Keeps track of child to swap with.
        if _list[swap] < _list[child]:
            swap = child
        if child+1 <= end and _list[swap] < _list[child+1]:  ## If there is a right child, and it is larger than the current child to swap with.
            swap = child+1
        if swap == root:
            return  ## The root holds the largest element. Since we assume the heaps rooted at the children are valid, this means we are done.
        else:
            backup = _list[swap]
            _list[swap] = _list[root]
            _list[root] = backup
            root = swap  ## Repeat to continue sifting down the child with which was swapped.


def sort_heap(_list):
    """Implentation of heap sort.

    NOTE: This implementation sorts the input list in-place!

    Algorithm:
    1) Restructure the list into a heap structure.
    2) The first element (root) is now the largest, swap it with the last element.
    3) Repeat, but shrink the list down one element from the back after every
       iteration.
    4) Once the heap has shrunk down to size one the list is sorted.
    """
    # Restructure the list into a heap.
    ll = len(_list)
    start = int((ll - 2) / 2)
    while start >= 0:
        sift_down(_list, start, ll-1)
        start -= 1

    # Swap and restore heap property of shrunk list. Repeat until done.
    end = ll - 1
    while end > 0:
        largest = _list[0]
        _list[0] = _list[end]
        _list[end] = largest
        end -= 1
        sift_down(_list, 0, end)
    return _list


###
### MAIN BODY COMPAIRS ALGORITHMS
###

if __name__ == '__main__':
    # Create lists containing a chosen amount of numbers, and randomize.
    nelems = [10,  50, 100, 500, 1000, 5000, 10000]
    lists = [list(range(nn)) for nn in nelems]
    for ll in lists:
        random.shuffle(ll)

    header = "Algorithm |" + " {:10d} elems |"*len(nelems)
    header = header.format(*nelems)
    print('\n'+"="*len(header))
    print(header)
    print("="*len(header),  end='')

    # The sorting algorithms to be considered.
    sort_funcs = [
        ('Insertion', sort_insertion),
        ('Selection', sort_selection),
        ('Merge    ', sort_merge),
        ('Quick    ', sort_quick),
        ('Heap     ', sort_heap),
        ]

    # Feed the lists to the sorting algorithms, time the execution and print a report.
    for sort_func in sort_funcs:
        print("\n{} |".format(sort_func[0]),  end='')
        for _list in lists:
            _list_copy = [e for e in _list]
            ts = datetime.datetime.now()
            _list_sorted = sort_func[1](_list_copy)
            te = datetime.datetime.now()
            td = te - ts
            print(" {:15f}s |".format(td.total_seconds()), end='')
        print('\n'+'-'*len(header),  end='')

# End
