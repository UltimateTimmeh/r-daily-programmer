#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/027e.py

| **Challenge name:** Year Info (reddit_, source_)
| **Challenge number:** 27
| **Difficulty:** Easy
| **Submission date:** 2012-03-17
| **Status:** Complete

Description
-----------

Write a program that accepts a year as input and outputs the century the year belongs in (e.g. 18th
century's year ranges are 1701 to 1800) and whether or not the year is a leap year.  Pseudocode for
leap year can be found `here <http://en.wikipedia.org/wiki/Leap_year#Algorithm>`_.

Sample run:

| Enter Year:  1996
| Century:  20
| Leap Year: Yes

| Enter Year:  1900
| Century:  19
| Leap Year:  No

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 027e
    Enter Year: 1996
    Century: 20
    Leap Year: yes

::

    $ python3 dailyprogrammer.py execute 027e
    Enter Year: 1900
    Century: 19
    Leap Year: no

Imported plugins
----------------

| :mod:`plugins.doomsday`

Module contents
---------------
"""

from plugins import doomsday as dd
from plugins import utils


def run():
    """Execute the challenges.027e module."""
    year = int(utils.get_input("Enter Year: "))
    print("Century: {}".format(dd.century(year)))
    print("Leap Year: {}".format({True: 'yes', False: 'no'}[dd.is_leapyear(year)]))

