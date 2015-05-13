#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/011e.py

| **Challenge name:**  Doomsday Algorithm (reddit_, source_)
| **Challenge number:** 11
| **Difficulty:** Easy
| **Submission date:** 2012-02-19
| **Status:** Complete

Description
-----------

The program should take three arguments. The first will be a day, the second will be month, and the third
will be year. Then, your program should compute the day of the week that date will fall on.

Example run
-----------

::

    $ python3 dailyprogrammer.py 011e
    Year (1583 - ...) > 2015
    Month (1 - 12) > 5
    Day (1 - 31) > 13
    2015-5-13 is a wednesday

Module contents
---------------
"""

from plugins.doomsday import Date


def run():
    """Execute the challenges.010e module."""
    year = int(input("Year (1583 - ...) > "))
    month = int(input("Month (1 - 12) > "))
    ndays_in_month = Date(year, month, 1).ndays_in_month()
    day = int(input("Day (1 - {}) > ".format(ndays_in_month)))
    date = Date(year, month, day)
    print("{} is a {}".format(date, date.weekday(h=True)))

