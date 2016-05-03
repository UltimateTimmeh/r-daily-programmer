#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/shp28/4192012_challenge_41_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/041e.py

| **Challenge name:** ASCII Framing (reddit_, source_)
| **Challenge number:** 41
| **Difficulty:** Easy
| **Submission date:** 2012-04-19
| **Status:** Complete

Description
-----------

Write a program that will accept a sentence as input and then output that sentence surrounded by
some type of an ASCII decoration banner.

Sample run::

    Enter a sentence:  So long and thanks for all the fish

    Output

        *****************************************
        *                                       *
        *  So long and thanks for all the fish  *
        *                                       *
        *****************************************

Bonus:  If the sentence is too long, move words to the next line.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 041e
    Enter a sentence > So long, and thanks for all the fish!
    *******************************************
    *                                         *
    *  So long, and thanks for all the fish!  *
    *                                         *
    *******************************************
    $ python3 dailyprogrammer.py execute 041e
    Enter a sentence > This is a very long line which is surely going to be split
    into multiple lines after typing it all!
    ******************************************************************************
    *                                                                            *
    *  This is a very long line which is surely going to be split into multiple  *
    *  lines after typing it all!                                                *
    *                                                                            *
    ******************************************************************************

Module contents
---------------
"""

from plugins import enhancedstring as es


def run():
    """Execute the challenges.041e module."""
    text = input("Enter a sentence > ")
    framed = es.EnhancedString(text).frame_with_ascii()
    print(framed)

