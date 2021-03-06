#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/013e.py

| **Challenge name:**  Cumulative Day of the Year (reddit_, source_)
| **Challenge number:** 13
| **Difficulty:** Easy
| **Submission date:** 2012-02-21
| **Status:** Complete

Description
-----------

Find the number of the year for the given date. For example, january 1st would be 1, and december
31st is 365.

For extra credit, allow it to calculate leap years, as well.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 013e
    Year (1583 - ...) > 2015
    Month (1 - 12) > 5
    Day (1 - 31) > 18
    2015-5-18 is day number 138 of the year 2015.

::

    $ python3 dailyprogrammer.py 013e
    Year (1583 - ...) > 2016
    Month (1 - 12) > 2
    Day (1 - 29) > 29
    2016-2-29 is day number 60 of the year 2016.

Imported plugins
----------------

| :mod:`plugins.doomsday`

Module contents
---------------
"""

from plugins import doomsday as dd
from plugins import utils


def run():
    """Execute the challenges.013e module."""
    year = int(utils.get_input("Year (1583 - ...) > "))
    month = int(utils.get_input("Month (1 - 12) > "))
    ndays = dd.ndays_in_month(month, year)
    day = int(utils.get_input("Day (1 - {}) > ".format(ndays)))
    date = dd.Date(year, month, day)
    cumulday = date.cumulative_day_of_year()
    print("{} is day number {} of the year {}.".format(date, cumulday, date.year))

