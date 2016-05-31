#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/008e.py

| **Challenge name:**  Beer Bottles (reddit_, source_)
| **Challenge number:** 8
| **Difficulty:** Easy
| **Submission date:** 2012-02-16
| **Status:** Complete

Description
-----------

Write a program that will print the song "99 bottles of beer on the wall". For extra credit,
do not allow the program to print each loop on a new line.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 008e

    Multiple lines:
    99 bottles of beer on the wall, 99 bottles of beer
    Take one down and pass it around, 98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall, 1 bottle of beer.
    Take one down and pass it around, no more bottles of beer on the wall.
    No more bottles of beer on the wall, no more bottles of beer.
    Go to the store and buy some more, 99 bottles of beer on the wall.

    Single line:
    99 bottles of beer on the wall, 99 bottles of beer Take one down and pass it around, 98 bottles of beer on the wall. ... 1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.

Imported plugins
----------------

| None

Module contents
---------------
"""


def beerbottles(jc='\n'):
    """Generate the lyrics of the beer bottle song.

    :param str jc: character that will be used to join the different lines of the lyrics
                   (default '\\\\n')
    :return: single string containing the full lyrics of the song
    :rtype: str
    """
    lyrics = []
    for nr in range(99, -1, -1):
        if nr == 0:
            line1 = "No more bottles of beer on the wall, no more bottles of beer."
            line2 = "Go to the store and buy some more, 99 bottles of beer on the wall."
        elif nr == 1:
            line1 = "1 bottle of beer on the wall, 1 bottle of beer."
            line2 = "Take one down and pass it around, no more bottles of beer on the wall."
        else:
            line1 = "{nr} bottles of beer on the wall, {nr} bottles of beer".format(nr=nr)
            line2 = "Take one down and pass it around, "
            if nr-1 == 1:
                line2 += "1 bottle of beer on the wall."
            else:
                line2 += "{nr} bottles of beer on the wall.".format(nr=nr-1)
        lyrics += [line1, line2]
    return jc.join(lyrics)


def run():
    """Execute the challenges.008e module."""
    print("\nMultiple lines:")
    print(beerbottles())
    print("\nSingle line:")
    print(beerbottles(jc=' '))

