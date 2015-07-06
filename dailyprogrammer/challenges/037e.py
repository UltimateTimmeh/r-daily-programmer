#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/037e.py

| **Challenge name:** File Line Count (reddit_, source_)
| **Challenge number:** 37
| **Difficulty:** Easy
| **Submission date:** 2012-04-08
| **Status:** Complete

Description
-----------

write a program that takes

input :  a file as an argument

output: counts the total number of lines.

for bonus, also count the number of words in the file.


Example run
-----------

Contents of 037e_example_input.txt::

    This is an example of text with
    multiple lines. Some lines have
    several words. Others only
    one.
    Others even have

    none!
    Note that this text starts and ends
    with a newline character, so it has
    twelve lines and 40 words.

Example run::

    $ python3 dailyprogrammer.py execute 037e
    Amount of lines in file: 12
    Amount of words in file: 40

Module contents
---------------
"""

from plugins.enhancedstring import EnhancedString


def run():
    """Execute the challenges.037e module."""
    with open("input/037e_example_input.txt", 'r') as fil:
        text = EnhancedString(fil.read())
    print("Amount of lines in file: {}".format(text.count_lines()))
    print("Amount of words in file: {}".format(text.count_words()))

