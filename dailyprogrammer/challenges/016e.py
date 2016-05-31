#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/016e.py

| **Challenge name:**  Remove Characters (reddit_, source_)
| **Challenge number:** 16
| **Difficulty:** Easy
| **Submission date:** 2012-02-27
| **Status:** Complete

Description
-----------

Write a function that takes two strings and removes from the first string any character that appears
in the second string. For instance, if the first string is ``Daily Programmer`` and the second
string is ``ae iou`` the result is ``DlyPrgrmmr``. Note that the second string has the [space]
character in it, so the space in "Daily Programmer" is also removed.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 016e
    Input string: Daily Programmer
    Characters to remove: ae iou
    Result: DlyPrgrmmr

Imported plugins
----------------

| :mod:`plugins.enhancedstring`

Module contents
---------------
"""

from plugins import enhancedstring as estr
from plugins import utils


def run():
    """Execute the challenges.016e module."""
    str_ = estr.EnhancedString(utils.get_input("Input string: "))
    chars = utils.get_input("Characters to remove: ")
    str_.remove(chars)
    print("Result: {}".format(str_))

