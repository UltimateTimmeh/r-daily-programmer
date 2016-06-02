#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/teua8/592012_challenge_50_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/050e.py

| **Challenge name:** First Sum Pair (reddit_, source_)
| **Challenge number:** 50
| **Difficulty:** Easy
| **Submission date:** 2012-05-10
| **Status:** Complete

Description
-----------

Hello everyone! As of today, we have finished our 50th challenge and it has been a pleasure giving
out these challenges to you all. You have all been amazing with the solutions and seeing you all I
hope I become a good programmer like you all one day :D

If I did any mistakes in challenges please forgive me and as you may have noticed we post once in
two days or so to give you time to complete these. Really sorry if you wanted everyday posts... but
due to our busy lives, maybe sometime in future or maybe when I leave this subreddit, you may have
that in the new management :) Thank You one and all... As for now I have given today's two
challenges are from  `Google Code Jam Qualification Round Africa 2010 <http://code.google.com/codejam/contest/dashboard?c=351101#s=p0>`_

**Store Credit:**

You receive a credit C at a local store and would like to buy two items. You first walk through the
store and create a list L of all available items. From this list you would like to buy two items
that add up to the entire value of the credit. The solution you provide will consist of the two
integers indicating the positions of the items in your list (smaller number first).

*Example input and output*::

    C = 100, L = [5, 75, 25]                   -> (2, 3)  ## Python: (1, 2)
    C = 200, L = [150, 24, 79, 50, 88, 345, 3] -> (1, 4)  ## Python: (0, 3)
    C = 8,   L = [2, 1, 9, 4, 4, 56, 90, 3]    -> (4, 5)  ## Python: (3, 4)

PROBLEM A IN THE LINK. PLEASE USE IT TO CLARIFY YOUR DOUBTS

P.S: Special Thanks to the other moderators too for helping out :)

Example run
-----------

::

    Amount of cases: 3
    Credit for case 1: 100
    Item prices for case 1: 5 75 25
    Credit for case 2: 200
    Item prices for case 2: 150 24 79 50 88 345 3
    Credit for case 3: 8
    Item prices for case 3: 2 1 9 4 4 56 90 3
    Case #1: 1 2
    Case #2: 0 3
    Case #3: 3 4

Imported plugins
----------------

| :mod:`plugins.listtools`

Module contents
---------------
"""

from plugins import listtools as lt
from plugins import utils


def run():
    """Execute the challenges.050e module."""
    ncases = int(utils.get_input("Amount of cases: "))
    cases = []
    for icase in range(ncases):
        credit = int(utils.get_input("Credit for case {}: ".format(icase+1)))
        prices_raw = utils.get_input("Item prices for case {}: ".format(icase+1))
        prices = [int(price_raw) for price_raw in prices_raw.split()]
        cases.append((prices, credit))
    results = [lt.first_sum_pair(pr, cr) for pr, cr in cases]
    [print("Case #{}: {} {}".format(icase+1, *result)) for icase, result in enumerate(results)]

