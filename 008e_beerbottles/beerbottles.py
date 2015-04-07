#!/usr/bin/python3
"""
Class for printing the "99 bottles of beer" song's lyrics, with the ability
to start at an arbitrary number. You can also choose how to join the song's
lyrics, so depending on the chosen character this could be on multiple lines
or on a single line.

Usage:

./beerbottles.py b [j]

`b`    Amount of starting bottles.
`j`    Character with which to join the lyrics (default is '\n').
       To print on a single line, use space (' ').
"""

import sys


def plural(n):
    """Return an extra 's' if n is anything other than 1."""
    if n == 1:
        return ''
    else:
        return 's'


class BeerBottles(object):
    """Class for printing the '99 bottles of beer' song's lyrics."""


    def __init__(self, b, j='\n'):
        """Initialize the BeerBottles object."""
        self.bottles = b
        self.joinwith = j


    def __str__(self, wall=False):
        """Print the amount of bottles, possibly on a wall."""
        txt = "{} bottle{} of beer"
        if wall:
            txt += " on the wall."
        else:
            txt += "."
        return txt.format(self.bottles, plural(self.bottles))


    def take_and_pass(self):
        """Take a bottle and pass it around."""
        txt = "Take one down, pass it around."
        self.bottles -= 1
        return txt


    def lyrics(self, stopat=0):
        """Count down and generate the lyrics."""
        lyrics = []
        while self.bottles > stopat:
            lyrics += [
                self.__str__(wall=True),
                self.__str__(),
                self.take_and_pass(),
                self.__str__(wall=True),
                ]
        if len(lyrics) == 0:
            txt = "The minimum amount of beerbottles that should remain ({}) "
            txt += "has been reached or even passed. We can't sing anymore!"
            lyrics.append(txt.format(stopat))
        return self.joinwith.join(lyrics)


if __name__ == '__main__':
    b = int(sys.argv[1])
    j = '\n'
    if len(sys.argv) > 2:
        j = sys.argv[2]
    song = BeerBottles(b, j)
    print(song.lyrics())

# End
