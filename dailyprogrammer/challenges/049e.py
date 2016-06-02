#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/tb2h0/572012_challenge_49_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/049e.py

| **Challenge name:** Monty Hall Problem (reddit_, source_)
| **Challenge number:** 49
| **Difficulty:** Easy
| **Submission date:** 2012-05-07
| **Status:** Complete

Description
-----------

The `Monty Hall Problem <http://en.wikipedia.org/wiki/Monty_Hall_problem>`_ is a probability brain
teaser that has a rather unintuitive solution.

The gist of it, taken from Wikipedia::

    Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a
    car; behind the others, goats. You pick a door, say No. 1 [but the door is not opened], and the
    host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He
    then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your
    choice?

    (clarification: the host will always reveal a goat)

Your task is to write a function that will compare the strategies of *switching* and *not switching*
over many random position iterations. Your program should output the proportion of successful
choices by each strategy. Assume that if both unpicked doors contain goats the host will open one of
those doors at random with equal probability.

If you want to, you can for simplicity's sake assume that the player picks the first door every
time. The only aspect of this scenario that needs to vary is what is behind each door.

Thanks to `/u/SleepyTurtle <https://www.reddit.com/user/SleepyTurtle>`_ for posting this idea at
`/r/dailyprogrammer_ideas <https://www.reddit.com/r/dailyprogrammer_ideas>`_! Do you have a problem
you think would be good for us? Head on over there and post it!

Example run
-----------

::

    How many doors are there > 3
    How many simulations do you want to run > 1000000
    When switching, the player wins 667896 times out of 1000000.
    When not switching, the player wins 332104 times out of 1000000.

Imported plugins
----------------

| :mod:`plugins.listtools`

Module contents
---------------
"""

import random

from plugins import listtools as lt
from plugins import utils


def simulate_monty_hall(ndoors):
    """Simulate the outcome of the Monty Hall problem with an arbitrary amount of doors.

    Execution of the Monty Hall problem is simulated using the following procedure:

        1. A list containing a single winning door and ``ndoors-1`` losing doors is randomly
           shuffled.
        2. Assume the player always originally picks the first door (the randomness is already in
           the shuffle). Now remove ``ndoors-2`` doors from the rest of the list, making sure not to
           delete the winning door. There should only be two doors left: the first one (i.e. the one
           originally picked by the player) and whichever door was not removed by the host.
        3. Supposedly switching gives the player a higher chance of winning, so return whatever is
           behind the second of the remaining doors.

    :param int ndoors: amount of doors in the Monty Hall problem
    :return: True if the player won, False otherwise
    :rtype: bool

    Example::

        >>> simulate_monty_hall(3)
        True
        >>> [simulate_monty_hall(10) for ii in range(10)]
        [True, True, True, True, True, True, False, False, True, True]
    """
    doors = [True] + [False] * (ndoors-1)
    random.shuffle(doors)

    while len(doors) > 2:
        if not doors[1]:
            del doors[1]
        else:
            del doors[-1]

    return doors[1]


def run():
    """Execute the challenges.049e module."""
    ndoors = int(utils.get_input("How many doors are there > "))
    nruns = int(utils.get_input("How many simulations do you want to run > "))
    results = [simulate_monty_hall(ndoors) for run in range(nruns)]
    counts = lt.count_items(results)
    print("When switching, the player wins {} times out of {}.".format(counts[True], nruns))
    print("When not switching, the player wins {} times out of {}.".format(counts[False], nruns))

