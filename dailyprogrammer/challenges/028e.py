#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/r59kk/3202012_challenge_28_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/028e.py

| **Challenge name:** Array Duplicate (reddit_, source_)
| **Challenge number:** 28
| **Difficulty:** Easy
| **Submission date:** 2012-03-20
| **Status:** Complete

Description
-----------

The array duplicates problem is when one integer is in an array for more than once.

If you are given an array with integers between 1 and 1,000,000 or in some other interval and one
integer is in the array twice. How can you determine which one?

Your task is to write code to solve the challenge.

Note: try to find the most efficient way to solve this challenge.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 028e
    Amount of elements in list: 10
    Lower element limit: 1
    Upper element limit: 1000000
    Print the list (y/n)? y
    Randomly generated list:
    [202916, 14934, 986188, 582840, 702836, 456129, 169183, 986188, 95907, 734183]
    The duplicate element in the list is: 986188

::

    $ python3 dailyprogrammer.py execute 028e
    Amount of elements in list: 1000000
    Lower element limit: 1
    Upper element limit: 2000000
    Print the list (y/n)? n
    The duplicate element in the list is: 1892775

.. note:: In the second example, although I haven't timed it, I assume the bulk of the execution
          time is spent generating the random list. Finding the first duplicate should be pretty
          fast.

Imported plugins
----------------

| :mod:`plugins.listtools`

Module contents
---------------
"""

import random

from plugins import listtools as lt
from plugins import utils


def run():
    """Execute the challenges.028e module."""
    # Ask user input.
    nelems = int(utils.get_input("Amount of elements in list: "))
    llim = int(utils.get_input("Lower element limit: "))
    ulim = int(utils.get_input("Upper element limit: "))
    plist = utils.get_input("Print the list (y/n)? ").lower()[0]

    # Generate the random list with a single duplicate element.
    if llim > ulim:
        llim, ulim = ulim, llim
    if nelems > ulim - llim + 1:
        nelems = ulim - llim + 1
    x = list(range(llim, ulim+1))
    random.shuffle(x)
    x = x[:nelems-1] + x[nelems-2:nelems-1]
    random.shuffle(x)
    if plist == 'y':
        print("Randomly generated list:")
        print(x)

    # Find and print the duplicate element.
    print("The duplicate element in the list is: {}".format(lt.first_duplicate(x)))

