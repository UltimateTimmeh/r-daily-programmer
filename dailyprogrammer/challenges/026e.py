#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qzil1/3162012_challenge_26_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/026e.py

| **Challenge name:** Filter String Duplicates (reddit_, source_)
| **Challenge number:** 26
| **Difficulty:** Easy
| **Submission date:** 2012-03-16
| **Status:** Complete

Description
-----------

You have a string "ddaaiillyypprrooggrraammeerr". We want to remove all the consecutive duplicates
and put them in a separate string, which yields two separate instances of the string
"dailyprogramer".

**Use this list for testing:**

| *input*: "balloons"
| *expected output*: "balons" "lo"

| *input*: "ddaaiillyypprrooggrraammeerr"
| *expected output*: "dailyprogramer" "dailyprogramer"

| *input*: "aabbccddeded"
| *expected output*: "abcdeded" "abcd"

| *input*: "flabby aapples"
| *expected output*: "flaby aples" "bap"

.. note:: One of the comments states that if there are multiple duplicates of a character in a row,
          all duplicates should go to the second string. So the string ``'aaaa'`` should be split
          in a first part ``'a'`` and a second part ``'aaa'``.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 026e
    Input: balloons
      Output: 'balons' 'lo'
    Input: ddaaiillyypprrooggrraammeerr
      Output: 'dailyprogramer' 'dailyprogramer'
    Input: aabbccddeded
      Output: 'abcdeded' 'abcd'
    Input: flabby aapples
      Output: 'flaby aples' 'bap'

Module contents
---------------
"""


def filter_consecutive_duplicates(str_):
    """Filter consecutive duplicates from a string.

    :param str str\_: the string that needs to be filtered
    :return: a tuple containing the filtered string and the string of removed consecutive duplicates
    :rtype: tuple(str, str)

    Example::

        >>> filter_consecutive_duplicates('balloons')
        ('balons', 'lo')
    """
    str_filtered, str_removed = [], []
    pc = ''  ## Previous character.
    for cc in str_:  ## Current character
        {True: str_filtered.append, False: str_removed.append}[cc != pc](cc)
        pc = cc
    return ''.join(str_filtered), ''.join(str_removed)


def run():
    """Execute the challenges.026e module."""
    inputs = [
        'balloons',
        'ddaaiillyypprrooggrraammeerr',
        'aabbccddeded',
        'flabby aapples',
    ]
    for input in inputs:
        print("Input: {}".format(input))
        print("  Output: '{}' '{}'".format(*filter_consecutive_duplicates(input)))

