#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/t78m8/542012_challenge_48_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/048e.py

| **Challenge name:** Evensort (reddit_, source_)
| **Challenge number:** 48
| **Difficulty:** Easy
| **Submission date:** 2012-05-05
| **Status:** Complete

Description
-----------

Take an array of integers and partition it so that all the even integers in the array precede all
the odd integers in the array. Your solution must take linear time in the size of the array and
operate in-place with only a constant amount of extra space.

Your task is to write the indicated function.

Example run
-----------

::

    First let's prove I have a function that works.
    Randomly shuffled range of 1 to 10 (inclusive): [5, 2, 4, 10, 8, 3, 6, 1, 7, 9]
    After applying the `evensort` function: [6, 2, 4, 10, 8, 3, 5, 1, 7, 9]
    Now let's prove that it runs in linear time relative to array size.
    This may take a while, so sit back and relax...

    list length | evensort execution time  |  factor
    ------------|--------------------------|----------
             10 |  0.000004433000867720693 |   0.000
            100 |  0.000018383001588517800 |   4.147
           1000 |  0.000195455999346449971 |  10.632
          10000 |  0.001952049999090377241 |   9.987
         100000 |  0.021699524000723613426 |  11.116
        1000000 |  0.282696435002435464412 |  13.028
       10000000 |  2.879524725998635403812 |  10.186
      100000000 | 34.316989678998652379960 |  11.918

    We see that when list length is multiplied by ten, so is execution time!

Imported plugins
----------------

| :mod:`plugins.listtools`

Module contents
---------------
"""

import random
import timeit

from plugins import listtools
from plugins import utils


def time_evensort(n=10):
    """Time the execution of the :func:`plugins.listtools.evensort` function.

    A list containing the range from 1 to ``n`` (inclusive) is randomly shuffled and passed to the
    :func:`plugins.listtools.evensort` function. Execution of the function is timed and returned.

    :param int n: the amount of items in the tested list
    :return: the time spent executing the :func:`plugins.listtools.evensort` function
    :rtype: float

    Example::

        >>> time_evensort()
        8.806000550976023e-06
        >>> time_evensort(1000)
        0.0003092639999522362
        >>> time_evensort(10000000)
        2.969431393998093
    """
    x = list(range(1, n+1))
    random.shuffle(x)
    wrapped = utils.wrap_arguments(listtools.evensort, x)
    return timeit.timeit(wrapped, number=1)


def run():
    """Execute the challenges.048e module."""
    print("First let's prove I have a function that works.")
    x = list(range(1, 11))
    random.shuffle(x)
    print("Randomly shuffled range of 1 to 10 (inclusive):", x)
    listtools.evensort(x)
    print("After applying the `evensort` function:", x)
    print("Now let's prove that it runs in linear time relative to array size.")
    print("This may take a while, so sit back and relax...", end='\n\n')
    ns = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    ts = [time_evensort(n) for n in ns]
    facs = [0.] + [t1/t2 for t1, t2 in zip(ts[1:], ts[:-1])]
    print("list length | evensort execution time  |  factor  ")
    print("------------|--------------------------|----------")
    for n, t, fac in zip(ns, ts, facs):
        print('{:>11d} | {:>24.21f} | {:>7.3f}'.format(n, t, fac))
    print("\nWe see that when list length is multiplied by ten, so is execution time!")

