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
in the second string. For instance, if the first string is `Daily Programmer` and the second string
is `aeiou ` the result is `DlyPrgrmmr`. Note that the second string has the [space] character in it,
so the space in "Daily Programmer" is also removed.

Example run
-----------

::

    $ python3 dailyprogrammer.py 016e
    Input string: Daily Programmer
    Characters to remove: ae iou
    Result: DlyPrgrmmr

Module contents
---------------
"""


class EnhancedString(object):
    """Class representing an enhanced string object.

    This class' main purpose is to enhance the built-in string object with several
    useful methods.

    :param str str_: the built-in string object that needs to be enhanced
    """


    def __init__(self, str_):
        """Create a new enhanced string."""
        self.str_ = str_


    def __str__(self):
        """Format the enhanced string as a string."""
        return self.str_


    def remove(self, chars):
        """Remove all instances of certain characters from the enhanced string.

        Note that any instance of each individual character in ``chars`` will be removed,
        not any instance of the complete ``chars`` string.

        :param str chars: string of characters to remove
        """
        for c in chars:
            self.str_ = self.str_.replace(c, '')


def run():
    """Execute the challenges.016e module."""
    str_ = EnhancedString(input("Input string: "))
    chars = input("Characters to remove: ")
    str_.remove(chars)
    print("Result: {}".format(str_))

