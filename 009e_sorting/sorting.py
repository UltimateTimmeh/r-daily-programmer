#!/usr/bin/env python3.4
"""
Implementation of various sorting algorithms, and tests on
various list sizes to determine which ones are more efficient.
"""

import datetime
import random
import sys


###
### GENERAL FUNCTIONS
###


def swap(_list, ii, jj):
    """Swap elements ii and jj in _list (in-place).

    Returns the value of the backed up element (originally in location ii).
    """
    backup = _list[ii]
    _list[ii] = _list[jj]
    _list[jj] = backup
    return backup


###
### SIMPLE SORTING ALGORITHMS
###


def sort_insertion(_list, verbose=False):
    """Implementation of insertion sort.

    NOTE: This implementation sorts the input list in-place!
    NOTE: Verbosity is for educational purposes, and somewhat slows down the
          algorithm.

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
    # Verbosity texts.
    txt_startpass = "Taking out element '{}' --> {}"
    txt_shift = "Shifting empty space to the left --> {}"
    txt_insert = "Inserting pivot element in empty space --> {}"

    # Sort code.
    for pi in range(1, len(_list)):
        pivot = _list[pi]
        if verbose:
            _list[pi] = '_'
            print(txt_startpass.format(pivot, _list))
        ei = pi
        while ei > 0 and _list[ei-1] > pivot:
            _list[ei] = _list[ei-1]
            if verbose:
                _list[ei-1] = '_'
                print(txt_shift.format(_list))
            ei -= 1
        _list[ei] = pivot
        if verbose:
            print(txt_insert.format(_list))
    return _list


def sort_selection(_list,  verbose=False):
    """Implementation of selection sort.

    NOTE: This implementation sorts the input list in-place!
    NOTE: Verbosity is for educational purposes, and somewhat slows down the
          algorithm.

    Algorithm:
    1) Go over all items of the list. The current item will be called the pivot.
    2) The pivot starts as being the 'smallest'.
    4) Starting at the item after the pivot, go through the remainder of the list
       and keep track of the smallest element.
    3) Once the end of the list has been reached, swap the pivot with the
       smallest element.
    4) After going over all elements in the list, the list is sorted.
    """
    # Verbosity texts.
    txt_startpass = "Start looking for element to put in location {}."
    txt_compare = "Currect smallest is {}='{}'. Comparing with {}='{}', "
    txt_smaller = "which is smaller, so it becomes the new smallest element."
    txt_greater = "which is greater, so the smallest remains the same."
    txt_swap = "{} <-- Swapping {} with {} --> "
    txt_same = "Element at location {} was already the smallest."

    # Sort code.
    for pi in range(len(_list)-1):
        si = pi
        if verbose:
            print(txt_startpass.format(pi), )
        for ri in range(pi+1,  len(_list)):
            if verbose:
                print(txt_compare.format(si, _list[si], ri, _list[ri]), end='')
            if _list[ri] < _list[si]:
                if verbose:
                    print(txt_smaller)
                si = ri
            elif verbose:
                print(txt_greater)
        if pi != si:
            if verbose:
                print(txt_swap.format(_list, si, pi), end='')
            swap(_list, pi, si)
            if verbose:
                print(_list)
        elif verbose:
            print(txt_same.format(pi))
    return _list


###
### EFFICIENT SORTING ALGORITHMS
###


def sort_merge(_list, layer=0, verbose=False):
    """Implementation of merge sort.

    Algorithm:
    1) Keep dividing the list in half until you reach the smallest possible size.
    2) Repeatedly merge the lists back together in pairs, meanwhile sorting the
       elements.
    3) Once all parts have been merged back together, the list is sorted.
    """
    # Verbosity texts.
    txt_tab = '|   '*layer
    txt_returnunit = txt_tab + "Returning trivially sorted list."
    txt_split = txt_tab + "Splitting {} --> {} + {}"
    txt_sort = txt_tab + "Performing merge sort on {}"
    txt_result = txt_tab + "Got back {} sorted list {}"
    txt_merge = txt_tab + "Merging {} + {} --> {}"

    # Sort code.
    ll = len(_list)
    if ll < 2:
        if verbose:
            print(txt_returnunit)
        return _list
    left = _list[:int(ll/2)]
    right = _list[int(ll/2):]
    if verbose:
        print(txt_split.format(_list, left, right))
        print(txt_sort.format(left))
    left = sort_merge(left, layer=layer+1, verbose=verbose)
    if verbose:
        print(txt_result.format('left', left))
        print(txt_sort.format(right))
    right = sort_merge(right, layer=layer+1, verbose=verbose)
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


def sort_quick(_list,  lo=0,  hi=None, layer=0, verbose=False):
    """Implentation of quick sort.

    NOTE: This implementation sorts the input list in-place!

    Algorithm:
    1) Determine a pivot element (choice is arbitrary, but different methods of
       determining the pivot can have a difference in the average efficiency of the
       algorithm).
    2) Reorder the list so all items smaller than the pivot come before it, and all
       items larger than the pivot come after it. Once this is done, the pivot is
       automatically in the correct (ordered) position.
    3) Recursively apply this algorithm to the lower and higher partitions. The
       base case of the recursion is a partition with one or no elements.
    """
    # Verbosity texts.
    txt_tab = "|   "*layer
    txt_pivot = txt_tab + "The pivot element is '{}'."
    txt_swappre = txt_tab + "{} <-- swapping pivot to the end --> "
    txt_swap = txt_tab + "{} <-- swapping {} with {} --> "
    txt_piupdate = "(pivot location updated to {})"
    txt_swappost = txt_tab + "{} <-- swapping pivot to location {} --> "
    txt_quick = txt_tab + "Performing quick sort on {} sublist: {}"
    txt_return = txt_tab + "Got back sorted {} sublist: {}"

    # Sort code.
    if hi is None:  ## Starting condition.
        hi = len(_list) - 1
    if lo >= hi:
        return _list
    pi = lo + int((hi-lo)/2)  ## This prevents overflow if lo + hi would be too large.
    if verbose:
        print(txt_pivot.format(_list[pi]))
        print(txt_swappre.format(_list[lo:hi+1]), end='')
    pivot = swap(_list, pi, hi)
    if verbose:
        print(_list[lo:hi+1])
    pi = lo
    for li in range(lo,  hi):
        if _list[li] < pivot:
            if verbose:
                print(txt_swap.format(_list[lo:hi+1], li, pi), end='')
            swap(_list, pi, li)
            pi += 1
            if verbose:
                print(_list[lo:hi+1], end=' ')
                print(txt_piupdate.format(pi))
    if verbose:
        print(txt_swappost.format(_list[lo:hi+1], pi), end='')
    swap(_list, hi, pi)
    if verbose:
        print(_list[lo:hi+1])
        print(txt_quick.format('left', _list[lo: pi]))
    sort_quick(_list,  lo,  pi-1, layer=layer+1, verbose=verbose)
    if verbose:
        print(txt_return.format('left', _list[lo: pi]))
        print(txt_quick.format('right', _list[pi+1: hi+1]))
    sort_quick(_list,  pi+1,  hi, layer=layer+1, verbose=verbose)
    if verbose:
        print(txt_return.format('right', _list[pi+1: hi+1]))
    return _list


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


    def sift_down(_list, starti, endi):
        """Restore list heap structure (in-place).

        Sift down the node at start index 'starti' to the proper place such that all nodes
        below the start index are in heap order.
        """
        rooti = starti
        while rooti*2+1 <= endi:  ## While the root has at least one child.
            childi = rooti*2+1  ## Left child.
            swapi = rooti  ## Keeps track of child to swap with.
            if _list[swapi] < _list[childi]:
                swapi = childi
            if childi+1 <= endi and _list[swapi] < _list[childi+1]:  ## If there is a right child, and it is larger than the current child to swap with.
                swapi = childi+1
            if swapi == rooti:
                return  ## The root holds the largest element. Since we assume the heaps rooted at the children are valid, this means we are done.
            else:
                swap(_list, swapi, rooti)
                rooti = swapi  ## Repeat to continue sifting down the child with which was swapped.


    # Restructure the list into a heap.
    ll = len(_list)
    starti = int((ll - 2) / 2)
    while starti >= 0:
        sift_down(_list, starti, ll-1)
        starti -= 1

    # Swap and restore heap property of shrunk list. Repeat until done.
    endi = ll - 1
    while endi > 0:
        swap(_list, 0, endi)
        endi -= 1
        sift_down(_list, 0, endi)
    return _list


###
### BUBBLE SORT AND VARIANTS
###


def sort_bubble(_list, verbose=False):
    """Implementation of bubble sort.

    NOTE: This implementation sorts the input list in-place!

    Algorithm:
    1) Go through the list in pairs.
    2) If the first item is smaller than the second item, swap them.
    3) Once you reach the end of the list, start again from the beginning.
    4) Once you can pass through the entire list without needing to swap, the list
       is sorted.
    """
    # Verbosity texts.
    txt_startpass = "Starting new pass, last swap in previous pass was at {}."
    txt_compare = "Comparing {}='{}' with {}='{}'"
    txt_swap = ": {} <-- swapping {} with {} --> "
    txt_ok = "... Looks OK."

    # Sort code.
    lsi = len(_list)
    while lsi > 0:
        if verbose:
            print(txt_startpass.format(lsi))
        newlsi = 0
        for ii in range(1, lsi):
            if verbose:
                print(txt_compare.format(ii-1, _list[ii-1], ii, _list[ii]), end='')
            if _list[ii-1] > _list[ii]:
                if verbose:
                    print(txt_swap.format(_list, ii-1, ii), end='')
                swap(_list, ii, ii-1)
                if verbose:
                    print(_list)
                newlsi = ii
            elif verbose:
                print(txt_ok)
        lsi = newlsi
    return _list


def sort_shell(_list,  gap_sequence='ciura', verbose=False):
    """Implementation of shell sort.

    NOTE: This implementation sorts the input list in-place!
    NOTE: Makes use of Marcin Ciura's gap sequence.

    This algorithm is a generalization of insertion sort.

    The idea is to keep insertion sort efficient for larger list sizes. For the larger gap
    sizes you perform insertion sort on many sublists each containing a small amount of
    heavily disordered elements, and for the smaller gap sizes you perform insertion sort
    on few sublists each containing many nearly-ordered elements. In both cases insertion
    sort is efficient.

    Algorithm:
    1) Determine a list of 'gap sizes', in decreasing order, ending with 1.
       Only consider gap sizes that are smaller than the length of the list.
    2) Perform a gapped insertion sort for each gap size:
       - The first 'gap' elements [0..gap-1] are already gap sorted.
       - Insert the other elements one at a time.
       - Back up the element that is being added, and consider its location to
         now be an 'empty' spot.
       - Move the element that is 'gap' locations before the empty spot into
         the empty spot until there is no such element or until that element is
         larger than the backed up element.
       - Move the backed up element into the resulting empty spot.
    3) Once this has been done for all gap sizes (the last one should be 1, in which case
       this algorithm is reduced to a simple insertion sort on a nearly-sorted list),
       the list is sorted.
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
    gaps = [e for e in gaps if e < len(_list)]
    if verbose:
        print(txt_gap.format(gap_sequence, gaps))
    for gap in gaps:
        if verbose:
            print(txt_startgap.format(gap))
        for pi in range(gap, len(_list)):
            pivot = _list[pi]
            ei = pi
            if verbose:
                _list[ei] = '_'
                print(txt_startpass.format(pivot, _list))
            while ei >= gap and _list[ei-gap] > pivot:
                _list[ei] = _list[ei-gap]
                if verbose:
                    _list[ei-gap] = '_'
                    print(txt_swap.format(gap, _list))
                ei -= gap
            _list[ei] = pivot
            if verbose:
                print(txt_insert.format(_list))
    return _list


def sort_comb(_list,  shrink=1.3,  verbose=False):
    """Implementation of comb sort (verbose version).

    NOTE: This implementation sorts the input list in-place!

    This algorithm attempts to improve bubble sort by elinimating 'turtles'. Turtles
    are small values near the end of the list, which typically move forward very slowly
    during a normal bubble sort. The idea is to start sorting with a larger 'gap' between
    the elements that are compared, and to gradually reduce this gap at each pass through the
    list. Once the minimum gap of 1 has been reached, the algorithm has been reduced to a
    standard bubble sort.

    1) Start with a gap equal to the length of the list.
    2) Shrink gap with a certain factor, and perform bubble sort on the list using the
       resulting gap.
    3) Repeat until the minimum gap size of 1 has been reached and there were no swaps during
       the last pass. The list is now sorted.
    """
    # Verbosity texts.
    txt_error = "ERROR: Shrink factor should be larger than 1. (is {})"
    txt_startcomb = "Start comb with gap {}..."
    txt_compare = "Comparing {}='{}' with {}='{}'"
    txt_swap = ": {} <-- swapping {} with {} --> "
    txt_ok = "... Looks OK."

    # Sort code.
    gap = len(_list)
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
        while ii+gap < len(_list):
            if verbose:
                print(txt_compare.format(ii, _list[ii], ii+gap, _list[ii+gap]), end='')
            if _list[ii] > _list[ii+gap]:
                if verbose:
                    print(txt_swap.format(_list, ii, ii+gap), end='')
                swap(_list, ii, ii+gap)
                swapped = True
                if verbose:
                    print(_list)
            elif verbose:
                print(txt_ok)
            ii += 1
    return _list


###
### MAIN BODY: TEST CORRECTNESS OF ALGORITHMS OR COMPAIR SPEED OF ALGORITHMS FOR VARIOUS LIST SIZES.
###

sort_funcs_list = [
        ('Insertion', sort_insertion),
        ('Selection', sort_selection),
        ('Merge', sort_merge),
        ('Quick', sort_quick),
##        ('Heap', sort_heap),
        ('Bubble', sort_bubble),
        ('Shell', sort_shell),
        ('Comb', sort_comb),
        ]
sort_funcs_dict = {sort_func[0]: sort_func[1] for sort_func in sort_funcs_list}


def test_algorithm(algorithm):
    """Test 'algorithm' for correctness."""
    # Set amount of elements.
    nelems = 10

    # Create the benchmark list, and a shuffled copy.
    _list_benchmark = list(range(nelems))
    _list_copy = [e for e in _list_benchmark]
    random.shuffle(_list_copy)
    print("\nTesting algorithm '{}'".format(algorithm))
    print("Shuffled list: {}".format(_list_copy))

    # Sort the list using the chosen algorithm.
    if algorithm not in sort_funcs_dict:
        print("ERROR: Algorithm '{}' not in the list of algorithms!".format(algorithm))
        return
    _list_sorted = sort_funcs_dict[algorithm](_list_copy, verbose=True)
    print("Sorted list: {}".format(_list_sorted))

    # Compare benchmark with sorted.
    if _list_sorted==_list_benchmark:
        print("The algorithm seems to work properly!")
    else:
        print("That does not look right...")


def compare_algorithms():
    """Compare all algorithms for speed on various list sizes."""

    # Create several lists containing a chosen amount of elements, and shuffle them all.
    nelems = [10,  50, 100, 500, 1000, 5000, 10000]
    lists = [list(range(nn)) for nn in nelems]
    for ll in lists:
        random.shuffle(ll)

    # Print the report header.
    header = "Algorithm |" + " {:6d} elems |"*len(nelems)
    header = header.format(*nelems)
    print('\n'+"="*len(header))
    print(header)
    print("="*len(header),  end='')

    # Feed the lists to the sorting algorithms, time the execution and print a report.
    for sort_func in sort_funcs_list:
        print("\n{:9s} |".format(sort_func[0]),  end='')
        for _list in lists:
            _list_copy = [e for e in _list]
            ts = datetime.datetime.now()
            sort_func[1](_list_copy)
            te = datetime.datetime.now()
            td = te - ts
            print(" {:11f}s |".format(td.total_seconds()), end='')
        print('\n'+'-'*len(header),  end='')


if __name__ == '__main__':
    if len(sys.argv)==3 and sys.argv[1]=='test':
        test_algorithm(sys.argv[2])
    elif len(sys.argv)<2 or (len(sys.argv)==2 and sys.argv[1]=='compare'):
        compare_algorithms()
    else:
        usage = [
            "\nUsage: python3.4 sorting.py TYPE [ALGORITHM]",
            "- TYPE is one of 'test' or 'compare'.",
            "- ALGORITHM is required when TYPE is 'test', and is the name of the algorithm to",
            "  test.",
            "",
            "When testing an algorithm, it is executed in verbose mode, printing a detail of",
            "all actions taken during the execution of the algorithm. This is for educational",
            "purposes, so someone who is trying to understand how the algorithm works can see",
            "the steps performed in a real example."
            ]
        print('\n'.join(usage))

# End
