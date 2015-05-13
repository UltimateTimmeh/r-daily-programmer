#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/009e.py

| **Challenge name:**  Sort Numbers (reddit_, source_)
| **Challenge number:** 9
| **Difficulty:** Easy
| **Submission date:** 2012-02-17
| **Status:** Done

Description
-----------

Write a program that will allow the user to input digits, and arrange them in numerical order.
For extra credit, have it also arrange strings in alphabetical order

Example run
-----------

::

    $ python3 dailyprogrammer.py 009e
    Enter numbers to sort, separated by a comma: 1.2, 325.0, 2, 5.6, 2.0, -3.75

    The available sorting algorithms are: ['selection', 'heap', 'merge', 'bubble', 'quick', 'shell', 'insertion', 'comb']
    Choose one: merge

    Your unsorted list was:
        [1.2, 325.0, 2.0, 5.6, 2.0, -3.75]
    Your sorted list is:
        [-3.75, 1.2, 2.0, 2.0, 5.6, 325.0]

Module contents
---------------
"""

from plugins import sort


def run():
    """Execute the challenges.009e module."""
    # Ask for list of numbers to sort.
    nrs = input("Enter numbers to sort, separated by a comma: ")
    x = [float(nr) for nr in nrs.split(',')]

    # Ask for sorting algorithm to use.
    algorithms = {
        'insertion': (1, sort.insertion),
        'selection': (1, sort.selection),
        'merge': (0, sort.merge),
        'quick': (1,  sort.quick),
        'heap': (1, sort.heap),
        'bubble': (1, sort.bubble),
        'shell': (1, sort.shell),
        'comb': (1, sort.comb),
    }
    print("\nThe available sorting algorithms are: {}".format(list(algorithms.keys())))
    chosen = input("Choose one: ")
    while chosen not in algorithms:
        chosen = input("Invalid algorithm! Choose one from the list: ")

    # Sort the list and print the result.
    inplace, sortfunc = algorithms[chosen]
    print("\nYour unsorted list was:\n    {}".format(x))
    if inplace:
        sortfunc(x)
    else:
        x = sortfunc(x)
    print("Your sorted list is:\n    {}".format(x))

