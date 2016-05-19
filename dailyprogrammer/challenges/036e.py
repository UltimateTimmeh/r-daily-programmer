#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/ruiob/452012_challenge_36_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/036e.py

| **Challenge name:** 1000 Lockers (reddit_, source_)
| **Challenge number:** 36
| **Difficulty:** Easy
| **Submission date:** 2012-04-05
| **Status:** Complete

Description
-----------

1000 Lockers Problem.

In an imaginary high school there exist 1000 lockers labelled 1, 2, ..., 1000. All of them are
closed. 1000 students are to "toggle" a locker's state.

- The first student toggles all of them
- The second one toggles every other one (i.e, 2, 4, 6, ...)
- The third one toggles the multiples of 3 (3, 6, 9, ...) and so on until all students have
  finished.

To toggle means to close the locker if it is open, and to open it if it's closed.

How many and which lockers are open in the end?

Thanks to ladaghini for submitting this challenge to `/r/dailyprogrammer_ideas <http://www.reddit.com/r/dailyprogrammer_ideas>`_!

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 036e
    How many lockers are there? > 1000
    After toggling, there are 31 open lockers.
    These are their numbers:
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]

Module contents
---------------
"""

from plugins import utils


def locker_problem(n):
    """Simulate the locker problem for an arbitrary amount of lockers.

    A list of booleans is returned, one for each locker, where False indicates the locker is closed
    and True indicates the locker is opened after simulation of the problem.

    :param int n: the amount of lockers (and students)
    :return: list containing one boolean for each locker, where False indicates closed and True
             indicates opened
    :rtype: list(bool, ...)

    Example::

        >>> locker_problem(5)
        [True, False, False, True, False]
    """
    lockers = [False] * n
    for sn in range(n):
        lockers = [{True: not ls, False: ls}[(ln+1)%(sn+1)==0] for ln, ls in enumerate(lockers)]
    return lockers


def locker_problem2(n):
    """Solve the locker problem by directly determining each locker's state.

    Instead of simulating the toggling of each locker, each locker's end state is immediately
    determined based on whether or not the locker number is the square of an integer. A few quick
    tests have shown that this is *a lot* faster than :func:`challenges.036e.locker_problem`
    (as expected).

    :param int n: the amount of lockers (and students)
    :return: list containing one boolean for each locker, where False indicates closed and True
             indicates opened
    :rtype: list(bool, ...)

    Example::

        >>> locker_problem2(5)
        [True, False, False, True, False]
    """
    return [ln**0.5 == int(ln**0.5) for ln in range(1, n+1)]


def run():
    """Execute the challenges.036e module."""
    n = int(utils.get_input("How many lockers are there? > "))
    lockers = locker_problem2(n)
    open_lockers = [l+1 for l, s in enumerate(lockers) if s]
    msg = "After toggling, there are {} open lockers.\nThese are their numbers:\n{}"
    print(msg.format(len(open_lockers), open_lockers))

