#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/listtools.py

Collection of useful operations on lists (source_).
"""

import copy


def swap(x, ii, jj):
    """In-place swapping of elements in a list.

    :param list x: the list in which the elements should be swapped
    :param int ii: index of the first element to be swapped
    :param int jj: index of the second element to be swapped
    :return: the first element to be swapped
    :rtype: object

    Example::

        >>> x = ['a', 'b', 'c', 'd', 'e']
        >>> swap(x, 0, 4)
        'a'
        >>> x
        ['e', 'b', 'c', 'd', 'a']
    """
    backup = x[ii]
    x[ii] = x[jj]
    x[jj] = backup
    return backup


def insertionsort(x, verbose=False):
    """In-place list sorting using the 'insertion sort' algorithm.

    `Insertion sort on Wikipedia <http://en.wikipedia.org/wiki/Insertion_sort>`_

    :param list x: list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [4, 1, 3, 5, 2]
        >>> insertionsort(x, verbose=True)
        Taking out element '1' --> [4, '_', 3, 5, 2]
        Shifting empty space to the left --> ['_', 4, 3, 5, 2]
        Inserting pivot element in empty space --> [1, 4, 3, 5, 2]
        Taking out element '3' --> [1, 4, '_', 5, 2]
        Shifting empty space to the left --> [1, '_', 4, 5, 2]
        Inserting pivot element in empty space --> [1, 3, 4, 5, 2]
        Taking out element '5' --> [1, 3, 4, '_', 2]
        Inserting pivot element in empty space --> [1, 3, 4, 5, 2]
        Taking out element '2' --> [1, 3, 4, 5, '_']
        Shifting empty space to the left --> [1, 3, 4, '_', 5]
        Shifting empty space to the left --> [1, 3, '_', 4, 5]
        Shifting empty space to the left --> [1, '_', 3, 4, 5]
        Inserting pivot element in empty space --> [1, 2, 3, 4, 5]
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_startpass = "Taking out element '{}' --> {}"
    txt_shift = "Shifting empty space to the left --> {}"
    txt_insert = "Inserting pivot element in empty space --> {}"

    # Sort code.
    for pi in range(1, len(x)):
        pivot = x[pi]
        if verbose:
            x[pi] = '_'
            print(txt_startpass.format(pivot, x))
        ei = pi
        while ei > 0 and x[ei-1] > pivot:
            x[ei] = x[ei-1]
            if verbose:
                x[ei-1] = '_'
                print(txt_shift.format(x))
            ei -= 1
        x[ei] = pivot
        if verbose:
            print(txt_insert.format(x))


def selectionsort(x,  verbose=False):
    """In-place list sorting using the 'selection sort' algorithm.

    `Selection sort on Wikipedia <http://en.wikipedia.org/wiki/Selection_sort>`_

    :param list x: list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [2, 4, 3, 1, 5]
        >>> selectionsort(x, verbose=True)
        Start looking for element to put in location 0.
        Currect smallest is 0='2'. Comparing with 1='4', which is greater, so the smallest remains the same.
        Currect smallest is 0='2'. Comparing with 2='3', which is greater, so the smallest remains the same.
        Currect smallest is 0='2'. Comparing with 3='1', which is smaller, so it becomes the new smallest element.
        Currect smallest is 3='1'. Comparing with 4='5', which is greater, so the smallest remains the same.
        [2, 4, 3, 1, 5] <-- Swapping 3 with 0 --> [1, 4, 3, 2, 5]
        Start looking for element to put in location 1.
        Currect smallest is 1='4'. Comparing with 2='3', which is smaller, so it becomes the new smallest element.
        Currect smallest is 2='3'. Comparing with 3='2', which is smaller, so it becomes the new smallest element.
        Currect smallest is 3='2'. Comparing with 4='5', which is greater, so the smallest remains the same.
        [1, 4, 3, 2, 5] <-- Swapping 3 with 1 --> [1, 2, 3, 4, 5]
        Start looking for element to put in location 2.
        Currect smallest is 2='3'. Comparing with 3='4', which is greater, so the smallest remains the same.
        Currect smallest is 2='3'. Comparing with 4='5', which is greater, so the smallest remains the same.
        Element at location 2 was already the smallest.
        Start looking for element to put in location 3.
        Currect smallest is 3='4'. Comparing with 4='5', which is greater, so the smallest remains the same.
        Element at location 3 was already the smallest.
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_startpass = "Start looking for element to put in location {}."
    txt_compare = "Currect smallest is {}='{}'. Comparing with {}='{}', "
    txt_smaller = "which is smaller, so it becomes the new smallest element."
    txt_greater = "which is greater, so the smallest remains the same."
    txt_swap = "{} <-- Swapping {} with {} --> "
    txt_same = "Element at location {} was already the smallest."

    # Sort code.
    for pi in range(len(x)-1):
        si = pi
        if verbose:
            print(txt_startpass.format(pi), )
        for ri in range(pi+1,  len(x)):
            if verbose:
                print(txt_compare.format(si, x[si], ri, x[ri]), end='')
            if x[ri] < x[si]:
                if verbose:
                    print(txt_smaller)
                si = ri
            elif verbose:
                print(txt_greater)
        if pi != si:
            if verbose:
                print(txt_swap.format(x, si, pi), end='')
            swap(x, pi, si)
            if verbose:
                print(x)
        elif verbose:
            print(txt_same.format(pi))


def mergesort(x, verbose=False, _layer=0):
    """List sorting using the 'merge sort' algorithm.

    `Merge sort on Wikipedia <http://en.wikipedia.org/wiki/Merge_sort>`_

    :param list x: (sub)list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)
    :param int _layer: current layer in the merge sort algorithm, for internal use only (default 0)
    :return: the sorted (sub)list
    :rtype: list

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [2, 3, 5, 1, 4]
        >>> mergesort(x, verbose=True)
        Splitting [2, 3, 5, 1, 4] --> [2, 3] + [5, 1, 4]
        Performing merge sort on [2, 3]
        |   Splitting [2, 3] --> [2] + [3]
        |   Performing merge sort on [2]
        |   |   Returning trivially sorted list.
        |   Got back left sorted list [2]
        |   Performing merge sort on [3]
        |   |   Returning trivially sorted list.
        |   Got back right sorted list [3]
        |   Merging [2] + [3] --> [2, 3]
        Got back left sorted list [2, 3]
        Performing merge sort on [5, 1, 4]
        |   Splitting [5, 1, 4] --> [5] + [1, 4]
        |   Performing merge sort on [5]
        |   |   Returning trivially sorted list.
        |   Got back left sorted list [5]
        |   Performing merge sort on [1, 4]
        |   |   Splitting [1, 4] --> [1] + [4]
        |   |   Performing merge sort on [1]
        |   |   |   Returning trivially sorted list.
        |   |   Got back left sorted list [1]
        |   |   Performing merge sort on [4]
        |   |   |   Returning trivially sorted list.
        |   |   Got back right sorted list [4]
        |   |   Merging [1] + [4] --> [1, 4]
        |   Got back right sorted list [1, 4]
        |   Merging [5] + [1, 4] --> [1, 4, 5]
        Got back right sorted list [1, 4, 5]
        Merging [2, 3] + [1, 4, 5] --> [1, 2, 3, 4, 5]
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_tab = '|   '*_layer
    txt_returnunit = txt_tab + "Returning trivially sorted list."
    txt_split = txt_tab + "Splitting {} --> {} + {}"
    txt_sort = txt_tab + "Performing merge sort on {}"
    txt_result = txt_tab + "Got back {} sorted list {}"
    txt_merge = txt_tab + "Merging {} + {} --> {}"

    # Sort code.
    ll = len(x)
    if ll < 2:
        if verbose:
            print(txt_returnunit)
        return x
    left = x[:int(ll/2)]
    right = x[int(ll/2):]
    if verbose:
        print(txt_split.format(x, left, right))
        print(txt_sort.format(left))
    left = mergesort(left, _layer=_layer+1, verbose=verbose)
    if verbose:
        print(txt_result.format('left', left))
        print(txt_sort.format(right))
    right = mergesort(right, _layer=_layer+1, verbose=verbose)
    if verbose:
        print(txt_result.format('right', right))
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
    merged = merged + left[il:] + right[ir:]
    if verbose:
        print(txt_merge.format(left, right, merged))
    return merged


def quicksort(x, verbose=False, _lo=0, _hi=None, _layer=0):
    """In-place list sorting using the 'quicksort' algorithm.

    `Quicksort on Wikipedia <http://en.wikipedia.org/wiki/Quicksort>`_

    :param list x: list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)
    :param int _lo: lower index limit of the current layer in the quicksort algorithm, for internal
                    use only (default 0)
    :param _hi: higher index limit of the current layer in the quicksort algorithm, for internal
                use only (default None)
    :type _hi: None or int
    :param int _layer: current layer in the quicksort algorithm, for internal use only (default 0)

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [2, 3, 4, 1, 5]
        >>> quicksort(x, verbose=True)
        The pivot element is '4'.
        [2, 3, 4, 1, 5] <-- swapping pivot to the end --> [2, 3, 5, 1, 4]
        [2, 3, 5, 1, 4] <-- swapping 0 with 0 --> [2, 3, 5, 1, 4] (pivot location updated to 1)
        [2, 3, 5, 1, 4] <-- swapping 1 with 1 --> [2, 3, 5, 1, 4] (pivot location updated to 2)
        [2, 3, 5, 1, 4] <-- swapping 3 with 2 --> [2, 3, 1, 5, 4] (pivot location updated to 3)
        [2, 3, 1, 5, 4] <-- swapping pivot to location 3 --> [2, 3, 1, 4, 5]
        Performing quick sort on left sublist: [2, 3, 1]
        |   The pivot element is '3'.
        |   [2, 3, 1] <-- swapping pivot to the end --> [2, 1, 3]
        |   [2, 1, 3] <-- swapping 0 with 0 --> [2, 1, 3] (pivot location updated to 1)
        |   [2, 1, 3] <-- swapping 1 with 1 --> [2, 1, 3] (pivot location updated to 2)
        |   [2, 1, 3] <-- swapping pivot to location 2 --> [2, 1, 3]
        |   Performing quick sort on left sublist: [2, 1]
        |   |   The pivot element is '2'.
        |   |   [2, 1] <-- swapping pivot to the end --> [1, 2]
        |   |   [1, 2] <-- swapping 0 with 0 --> [1, 2] (pivot location updated to 1)
        |   |   [1, 2] <-- swapping pivot to location 1 --> [1, 2]
        |   |   Performing quick sort on left sublist: [1]
        |   |   Got back sorted left sublist: [1]
        |   |   Performing quick sort on right sublist: []
        |   |   Got back sorted right sublist: []
        |   Got back sorted left sublist: [1, 2]
        |   Performing quick sort on right sublist: []
        |   Got back sorted right sublist: []
        Got back sorted left sublist: [1, 2, 3]
        Performing quick sort on right sublist: [5]
        Got back sorted right sublist: [5]
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_tab = "|   "*_layer
    txt_pivot = txt_tab + "The pivot element is '{}'."
    txt_swappre = txt_tab + "{} <-- swapping pivot to the end --> "
    txt_swap = txt_tab + "{} <-- swapping {} with {} --> "
    txt_piupdate = "(pivot location updated to {})"
    txt_swappost = txt_tab + "{} <-- swapping pivot to location {} --> "
    txt_quick = txt_tab + "Performing quick sort on {} sublist: {}"
    txt_return = txt_tab + "Got back sorted {} sublist: {}"

    # Sort code.
    if _hi is None:  ## Starting condition.
        _hi = len(x) - 1
    if _lo >= _hi:
        return
    pi = _lo + int((_hi-_lo)/2)  ## This prevents overflow if _lo + _hi would be too large.
    if verbose:
        print(txt_pivot.format(x[pi]))
        print(txt_swappre.format(x[_lo:_hi+1]), end='')
    pivot = swap(x, pi, _hi)
    if verbose:
        print(x[_lo:_hi+1])
    pi = _lo
    for li in range(_lo,  _hi):
        if x[li] < pivot:
            if verbose:
                print(txt_swap.format(x[_lo:_hi+1], li, pi), end='')
            swap(x, pi, li)
            pi += 1
            if verbose:
                print(x[_lo:_hi+1], end=' ')
                print(txt_piupdate.format(pi))
    if verbose:
        print(txt_swappost.format(x[_lo:_hi+1], pi), end='')
    swap(x, _hi, pi)
    if verbose:
        print(x[_lo:_hi+1])
        print(txt_quick.format('left', x[_lo: pi]))
    quicksort(x, verbose=verbose, _lo=_lo, _hi=pi-1, _layer=_layer+1)
    if verbose:
        print(txt_return.format('left', x[_lo: pi]))
        print(txt_quick.format('right', x[pi+1: _hi+1]))
    quicksort(x, verbose=verbose, _lo=pi+1, _hi=_hi, _layer=_layer+1)
    if verbose:
        print(txt_return.format('right', x[pi+1: _hi+1]))


def heapsort(x, verbose=False):
    """In-place list sorting using the 'heapsort' algorithm.

    `Heapsort on Wikipedia <http://en.wikipedia.org/wiki/Heapsort>`_

    :param list x: list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [2, 5, 4, 3, 1]
        >>> heapsort(x, verbose=True)
        Start constructing heap from full list: [2, 5, 4, 3, 1]
        |   Considering sublist from 1 to 5: [5, 4, 3, 1]
        |   |   Starting with root '5'
        |   |   Current root '5' is bigger than child(ren), heap property is fulfilled
        |   Considering sublist from 0 to 5: [2, 5, 4, 3, 1]
        |   |   Starting with root '2'
        |   |   Left child '5' is bigger than root
        |   |   [2, 5, 4, 3, 1] <-- swapping '2' with '5' --> [5, 2, 4, 3, 1]
        |   |   New root is '2'
        |   |   Left child '3' is bigger than root
        |   |   [5, 2, 4, 3, 1] <-- swapping '2' with '3' --> [5, 3, 4, 2, 1]
        |   |   New root is '2'
        |   |   This root has no children, heap property is fulfilled
        Heap constructed --> [5, 3, 4, 2, 1]
        [5, 3, 4, 2, 1] <-- swap root with end sublist --> [1, 3, 4, 2, 5]
        Start fixing heap for sublist from 0 to 3: [1, 3, 4, 2]
        |   Starting with root '1'
        |   Left child '3' is bigger than root
        |   Right child '4' is bigger than root and left child
        |   [1, 3, 4, 2] <-- swapping '1' with '4' --> [4, 3, 1, 2]
        |   New root is '1'
        |   This root has no children, heap property is fulfilled
        Heap fixed for sublist --> [4, 3, 1, 2]
        [4, 3, 1, 2, 5] <-- swap root with end sublist --> [2, 3, 1, 4, 5]
        Start fixing heap for sublist from 0 to 2: [2, 3, 1]
        |   Starting with root '2'
        |   Left child '3' is bigger than root
        |   [2, 3, 1] <-- swapping '2' with '3' --> [3, 2, 1]
        |   New root is '2'
        |   This root has no children, heap property is fulfilled
        Heap fixed for sublist --> [3, 2, 1]
        [3, 2, 1, 4, 5] <-- swap root with end sublist --> [1, 2, 3, 4, 5]
        Start fixing heap for sublist from 0 to 1: [1, 2]
        |   Starting with root '1'
        |   Left child '2' is bigger than root
        |   [1, 2] <-- swapping '1' with '2' --> [2, 1]
        |   New root is '1'
        |   This root has no children, heap property is fulfilled
        Heap fixed for sublist --> [2, 1]
        [2, 1, 3, 4, 5] <-- swap root with end sublist --> [1, 2, 3, 4, 5]
        Start fixing heap for sublist from 0 to 0: [1]
        |   Starting with root '1'
        |   This root has no children, heap property is fulfilled
        Heap fixed for sublist --> [1]
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_tab = "|   "
    txt_startconstruct = "Start constructing heap from full list: {}"
    txt_subconstruct = "Considering sublist from {} to {}: {}"
    txt_endconstruct = "Heap constructed --> {}"
    txt_swaproot = "{} <-- swap root with end sublist --> "
    txt_startfix = "Start fixing heap for sublist from 0 to {}: {}"
    txt_endfix = "Heap fixed for sublist --> {}"
    txt_swapsift = "{} <-- swapping '{}' with '{}' --> "
    txt_rootstart = "Starting with root '{}'"
    txt_leftchild = "Left child '{}' is bigger than root"
    txt_rightchild = "Right child '{}' is bigger than root and left child"
    txt_rootbiggest = "Current root '{}' is bigger than child(ren), heap property is fulfilled"
    txt_newroot = "New root is '{}'"
    txt_nochildren = "This root has no children, heap property is fulfilled"

    # Sort code.
    def sift_down(x, starti, endi, _layer=0):
        """In-place restoring of (sub)list heap structure.

        Sift down the node at start index 'starti' to the proper place such that all nodes
        below the start index are in heap order.

        :param list x: list of which heap structure will be restored
        :param int starti: start index of considered sublist
        :param int endi: end index of considered sublist
        :param int _layer: current layer in the heapsort algorithm, for internal use only
                           (default 0)
        """
        rooti = starti
        if verbose:
            print(txt_tab*_layer + txt_rootstart.format(x[rooti]))
        if verbose and rooti*2+1 > endi:
            print(txt_tab*_layer + txt_nochildren)
        while rooti*2+1 <= endi:  ## While the root has at least one child.
            childi = rooti*2+1  ## Left child.
            swapi = rooti  ## Keeps track of child to swap with.
            if x[swapi] < x[childi]:
                if verbose:
                    print(txt_tab*_layer + txt_leftchild.format(x[childi]))
                swapi = childi
            if childi+1 <= endi and x[swapi] < x[childi+1]:  ## If there is a right child, and it is larger than the current item to swap with.
                if verbose:
                    print(txt_tab*_layer + txt_rightchild.format(x[childi+1]))
                swapi = childi+1
            if swapi == rooti:
                if verbose:
                    print(txt_tab*_layer + txt_rootbiggest.format(x[rooti]))
                return  ## The root holds the largest element. Since we assume the heaps rooted at the children are valid, this means we are done.
            else:
                if verbose:
                    print(txt_tab*_layer + txt_swapsift.format(x[starti:endi+1], x[rooti], x[swapi]), end='')
                swap(x, swapi, rooti)
                rooti = swapi  ## Repeat to continue sifting down the child with which was swapped.
                if verbose:
                    print(x[starti:endi+1])
                    print(txt_tab*_layer + txt_newroot.format(x[rooti]))
                if verbose and rooti*2+1 > endi:
                    print(txt_tab*_layer + txt_nochildren)


    # Restructure the list into a heap.
    ll = len(x)
    starti = int((ll - 2) / 2)
    if verbose:
        print(txt_startconstruct.format(x))
    while starti >= 0:
        if verbose:
            print(txt_tab + txt_subconstruct.format(starti, ll, x[starti:ll]))
        sift_down(x, starti, ll-1, _layer=2)
        starti -= 1
    if verbose:
        print(txt_endconstruct.format(x))

    # Shrink list. Swap and restore heap property of shrunk list. Repeat until done.
    endi = ll - 1
    while endi > 0:
        if verbose:
            print(txt_swaproot.format(x), end='')
        swap(x, 0, endi)
        endi -= 1
        if verbose:
            print(x)
            print(txt_startfix.format(endi, x[0:endi+1]))
        sift_down(x, 0, endi, _layer=1)
        if verbose:
            print(txt_endfix.format(x[0:endi+1]))


def bubblesort(x, verbose=False):
    """In-place list sorting using the 'bubble sort' algorithm.

    `Bubble sort on Wikipedia <http://en.wikipedia.org/wiki/Bubble_sort>`_

    :param list x: list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [1, 5, 2, 3, 4]
        >>> bubblesort(x, verbose=True)
        Starting new pass, last swap in previous pass was at 5.
        Comparing 0='1' with 1='5'... Looks OK.
        Comparing 1='5' with 2='2': [1, 5, 2, 3, 4] <-- swapping 1 with 2 --> [1, 2, 5, 3, 4]
        Comparing 2='5' with 3='3': [1, 2, 5, 3, 4] <-- swapping 2 with 3 --> [1, 2, 3, 5, 4]
        Comparing 3='5' with 4='4': [1, 2, 3, 5, 4] <-- swapping 3 with 4 --> [1, 2, 3, 4, 5]
        Starting new pass, last swap in previous pass was at 4.
        Comparing 0='1' with 1='2'... Looks OK.
        Comparing 1='2' with 2='3'... Looks OK.
        Comparing 2='3' with 3='4'... Looks OK.
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_startpass = "Starting new pass, last swap in previous pass was at {}."
    txt_compare = "Comparing {}='{}' with {}='{}'"
    txt_swap = ": {} <-- swapping {} with {} --> "
    txt_ok = "... Looks OK."

    # Sort code.
    lsi = len(x)
    while lsi > 0:
        if verbose:
            print(txt_startpass.format(lsi))
        newlsi = 0
        for ii in range(1, lsi):
            if verbose:
                print(txt_compare.format(ii-1, x[ii-1], ii, x[ii]), end='')
            if x[ii-1] > x[ii]:
                if verbose:
                    print(txt_swap.format(x, ii-1, ii), end='')
                swap(x, ii, ii-1)
                if verbose:
                    print(x)
                newlsi = ii
            elif verbose:
                print(txt_ok)
        lsi = newlsi


def shellsort(x, gap_sequence='ciura', verbose=False):
    """In-place list sorting using the 'shellsort' algorithm.

    `Shellsort on Wikipedia <http://en.wikipedia.org/wiki/Shellsort>`_

    :param list x: list to be sorted
    :param str gap_sequence: gap sequence to use (see Wikipedia entry for more information), for
                             the moment only Marcin Ciura's gap sequence is supported (default
                             'ciura')
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)
    :raise: ValueError if an invalid gap sequence was passed

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [5, 3, 1, 4, 2]
        >>> shellsort(x, verbose=True)
        Using gap sequence 'ciura': [4, 1]
        Start pass with gap 4...
            Taking out element '2' --> [5, 3, 1, 4, '_']
                Swapping empty space 4 locations to the left --> ['_', 3, 1, 4, 5]
            Inserting pivot element in empty space --> [2, 3, 1, 4, 5]
        Start pass with gap 1...
            Taking out element '3' --> [2, '_', 1, 4, 5]
            Inserting pivot element in empty space --> [2, 3, 1, 4, 5]
            Taking out element '1' --> [2, 3, '_', 4, 5]
                Swapping empty space 1 locations to the left --> [2, '_', 3, 4, 5]
                Swapping empty space 1 locations to the left --> ['_', 2, 3, 4, 5]
            Inserting pivot element in empty space --> [1, 2, 3, 4, 5]
            Taking out element '4' --> [1, 2, 3, '_', 5]
            Inserting pivot element in empty space --> [1, 2, 3, 4, 5]
            Taking out element '5' --> [1, 2, 3, 4, '_']
            Inserting pivot element in empty space --> [1, 2, 3, 4, 5]
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_tab = '    '
    txt_error = "ERROR: Gap sequence '{}' is not supported!"
    txt_gap = "Using gap sequence '{}': {}"
    txt_startgap = "Start pass with gap {}..."
    txt_startpass = txt_tab + "Taking out element '{}' --> {}"
    txt_swap = txt_tab*2 + "Swapping empty space {} locations to the left --> {}"
    txt_insert = txt_tab + "Inserting pivot element in empty space --> {}"

    # Sort code.
    if gap_sequence == 'ciura':
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    else:
        raise ValueError(txt_error.format(gap_sequence))
    gaps = [e for e in gaps if e < len(x)]
    if verbose:
        print(txt_gap.format(gap_sequence, gaps))
    for gap in gaps:
        if verbose:
            print(txt_startgap.format(gap))
        for pi in range(gap, len(x)):
            pivot = x[pi]
            ei = pi
            if verbose:
                x[ei] = '_'
                print(txt_startpass.format(pivot, x))
            while ei >= gap and x[ei-gap] > pivot:
                x[ei] = x[ei-gap]
                if verbose:
                    x[ei-gap] = '_'
                    print(txt_swap.format(gap, x))
                ei -= gap
            x[ei] = pivot
            if verbose:
                print(txt_insert.format(x))


def combsort(x, shrink=1.3, verbose=False):
    """In-place list sorting using the 'comb sort' algorithm.

    `Comb sort on Wikipedia <http://en.wikipedia.org/wiki/Comb_sort>`_

    :param list x: list to be sorted
    :param float shrink: gap shrink factor (see Wikipedia entry for more information), should
                         be higher than 1.0 (default 1.3)
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)
    :raise: ValueError if the gap shrink factor is smaller than or equal to 1.0.

    Example::

        >>> import random
        >>> x = list(range(1, 6))
        >>> random.shuffle(x)
        >>> x
        [4, 2, 1, 5, 3]
        >>> combsort(x, verbose=True)
        Start comb with gap 3...
        |   Comparing 0='4' with 3='5'... Looks OK.
        |   Comparing 1='2' with 4='3'... Looks OK.
        Start comb with gap 2...
        |   Comparing 0='4' with 2='1': [4, 2, 1, 5, 3] <-- swapping 0 with 2 --> [1, 2, 4, 5, 3]
        |   Comparing 1='2' with 3='5'... Looks OK.
        |   Comparing 2='4' with 4='3': [1, 2, 4, 5, 3] <-- swapping 2 with 4 --> [1, 2, 3, 5, 4]
        Start comb with gap 1...
        |   Comparing 0='1' with 1='2'... Looks OK.
        |   Comparing 1='2' with 2='3'... Looks OK.
        |   Comparing 2='3' with 3='5'... Looks OK.
        |   Comparing 3='5' with 4='4': [1, 2, 3, 5, 4] <-- swapping 3 with 4 --> [1, 2, 3, 4, 5]
        Start comb with gap 1...
        |   Comparing 0='1' with 1='2'... Looks OK.
        |   Comparing 1='2' with 2='3'... Looks OK.
        |   Comparing 2='3' with 3='4'... Looks OK.
        |   Comparing 3='4' with 4='5'... Looks OK.
        >>> x
        [1, 2, 3, 4, 5]
    """
    # Verbosity texts.
    txt_error = "ERROR: Shrink factor should be larger than 1. (got {})"
    txt_startcomb = "Start comb with gap {}..."
    txt_compare = "|   Comparing {}='{}' with {}='{}'"
    txt_swap = ": {} <-- swapping {} with {} --> "
    txt_ok = "... Looks OK."

    # Sort code.
    gap = len(x)
    if shrink <= 1.:
        raise ValueError(txt_error.format(shrink))
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap/shrink)
        if gap < 1:
            gap = 1
        ii = 0
        swapped = False
        if verbose:
            print(txt_startcomb.format(gap))
        while ii+gap < len(x):
            if verbose:
                print(txt_compare.format(ii, x[ii], ii+gap, x[ii+gap]), end='')
            if x[ii] > x[ii+gap]:
                if verbose:
                    print(txt_swap.format(x, ii, ii+gap), end='')
                swap(x, ii, ii+gap)
                swapped = True
                if verbose:
                    print(x)
            elif verbose:
                print(txt_ok)
            ii += 1


def evensort(x, verbose=False):
    """In-place sorting of a list such that even numbers come before odd numbers.

    The list is edited in-place such that all even numbers come before odd numbers. Note that this
    does not preserve the relative order of even and odd numbers.

    :param list x: list to be sorted
    :param bool verbose: make the function verbose, printing a detailed report of all actions
                         (default False)

    Example::

        >>> import random
        >>> x = list(range(1, 8))
        >>> random.shuffle(x)
        >>> x
        [4, 1, 7, 2, 6, 3, 5]
        >>> evensort(x, verbose=True)
        Lower index (0) smaller than higher index (6). Continuing sort.
        Element at lower index (0) is not odd. Incrementing lower index.
        Element at higher index (6) is not even. Decrementing higher index.
        Element at higher index (5) is not even. Decrementing higher index.
        An odd element was found to be ranked lower than an even element:
        [4, 1, 7, 2, 6, 3, 5] <-- swapping 1 with 4 --> [4, 6, 7, 2, 1, 3, 5]
        Lower index (1) smaller than higher index (4). Continuing sort.
        Element at lower index (1) is not odd. Incrementing lower index.
        Element at higher index (4) is not even. Decrementing higher index.
        An odd element was found to be ranked lower than an even element:
        [4, 6, 7, 2, 1, 3, 5] <-- swapping 2 with 3 --> [4, 6, 2, 7, 1, 3, 5]
        Lower index (2) smaller than higher index (3). Continuing sort.
        Element at lower index (2) is not odd. Incrementing lower index.
        Lower index has become equal to higher index. Sort complete.
        >>> x
        [4, 6, 2, 7, 1, 3, 5]
    """
    # Verbosity texts.
    txt_continue = "Lower index ({}) smaller than higher index ({}). Continuing sort."
    txt_increment = "Element at lower index ({}) is not odd. Incrementing lower index."
    txt_decrement = "Element at higher index ({}) is not even. Decrementing higher index."
    txt_swap = ("An odd element was found to be ranked lower than an even element:\n"
                "{} <-- swapping {} with {} --> ")
    txt_end = ("Lower index has become equal to higher index. Sort complete.")

    lo_ = 0
    hi_ = len(x) - 1
    while lo_ < hi_:
        if verbose:
            print(txt_continue.format(lo_, hi_))
        while lo_ < hi_ and x[lo_] % 2 == 0:
            if verbose:
                print(txt_increment.format(lo_))
            lo_ += 1
        while lo_ < hi_ and x[hi_] % 2 == 1:
            if verbose:
                print(txt_decrement.format(hi_))
            hi_ -= 1
        if lo_ < hi_:
            if verbose:
                print(txt_swap.format(x, lo_, hi_), end='')
            swap(x, lo_, hi_)
            if verbose:
                print(x)
    if verbose:
        print(txt_end)


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


def find_sum(x, a):
    """Find two items in a list of which the sum equals the given number.

    :param list x: the input list
    :param float a: the requested sum
    :return: indices of the two items in the list of which the sum equals the requested number or
             None if no such items exist
    :rtype: (int, int) or None

    Example::

        >>> find_sum([5, 75, 25], 100)
        (1, 2)
        >>> find_sum([150, 24, 79, 50, 88, 345, 3], 200)
        (0, 3)
        >>> find_sum([2, 1, 9, 4, 4, 56, 90, 3], 8)
        (3, 4)
        >>> print(find_sum([5, 75, 25], 5))
        None
    """
    for i1, a1 in enumerate(x[:-1]):
        for i2, a2 in enumerate(x[i1+1:]):
            if (a1 + a2) == a:
                return (i1, i1+1+i2)

