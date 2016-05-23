#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/sobna/4232012_challenge_42_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/042e.py

| **Challenge name:** Beer Bottle 2 (reddit_, source_)
| **Challenge number:** 42
| **Difficulty:** Easy
| **Submission date:** 2012-04-24
| **Status:** Complete

Description
-----------

Write a program that prints out the lyrics for "Ninety-nine bottles of beer", "Old McDonald had a
farm" or "12 days of Christmas".

If you choose "Ninety-nine bottles of beer", you need to spell out the number, not just write the
digits down. It's "Ninety-nine bottles of beer on the wall", not "99 bottles of beer"!

For Old McDonald, you need to include at least 6 animals: a cow, a chicken, a turkey, a kangaroo, a
T-Rex and an animal of your choosing (Old McDonald has a weird farm). The cow goes "moo", the
chicken goes "cluck", the turkey goes "gobble", the kangaroo goes "g'day mate" and the T-Rex goes
"GAAAAARGH". You can have more animals if you like.

Make your code shorter than the song it prints out!


Example run
-----------

::

    ================
    BEER BOTTLE SONG
    ================

    sixty bottles of beer on the wall, sixty bottles of beer
    you take fifteen down, pass them around,
    forty-five bottles of beer on the wall.

    forty-five bottles of beer on the wall, forty-five bottles of beer
    you take fifteen down, pass them around,
    thirty bottles of beer on the wall.

    thirty bottles of beer on the wall, thirty bottles of beer
    you take fifteen down, pass them around,
    fifteen bottles of beer on the wall.

    fifteen bottles of beer on the wall, fifteen bottles of beer
    you take fifteen down, pass them around,
    zero bottles of beer on the wall.

    ===================
    OLD MACDONALDS SONG
    ===================

    old macdonald had a farm, E-I-E-I-O
    and on that farm he had a turkey, E-I-E-I-O
    with a gobble gobble here and a gobble gobble there,
    here a gobble, there a gobble, everywhere a gobble gobble
    old macdonald had a farm, E-I-E-I-O

    old macdonald had a farm, E-I-E-I-O
    and on that farm he had a chicken, E-I-E-I-O
    with a cluck cluck here and a cluck cluck there,
    here a cluck, there a cluck, everywhere a cluck cluck
    old macdonald had a farm, E-I-E-I-O

    old macdonald had a farm, E-I-E-I-O
    and on that farm he had a kangaroo, E-I-E-I-O
    with a g'day g'day here and a g'day g'day there,
    here a g'day, there a g'day, everywhere a g'day g'day
    old macdonald had a farm, E-I-E-I-O

    old macdonald had a farm, E-I-E-I-O
    and on that farm he had a squirrel, E-I-E-I-O
    with a ... ... here and a ... ... there,
    here a ..., there a ..., everywhere a ... ...
    old macdonald had a farm, E-I-E-I-O

    old macdonald had a farm, E-I-E-I-O
    and on that farm he had a t-rex, E-I-E-I-O
    with a GAAAAARGH GAAAAARGH here and a GAAAAARGH GAAAAARGH there,
    here a GAAAAARGH, there a GAAAAARGH, everywhere a GAAAAARGH GAAAAARGH
    old macdonald had a farm, E-I-E-I-O

    old macdonald had a farm, E-I-E-I-O
    and on that farm he had a cow, E-I-E-I-O
    with a moo moo here and a moo moo there,
    here a moo, there a moo, everywhere a moo moo
    old macdonald had a farm, E-I-E-I-O

Module contents
---------------
"""

from plugins import enhancedint as ei


def bottles_of_beer(start=99, takedown=1):
    """Print the 'ninety-nine bottles of beer' song with arbitrary numbers.

    This function prints the famous beer bottle song. You can make the song start at any number
    you want, and you can have it take down as many bottles as you want in every verse. The song
    stops when the amount of bottles left on the wall is smaller than the amount of bottles
    taken down.

    :param int start: the amount of beer bottles that are on the wall at the start of the song
                      (default 99)
    :param int takedown: the amount of beer bottles that are taken down in every verse (default 1)
    """
    verse = ("{before} bottle{bmul} of beer on the wall, {before} bottle{bmul} of beer\n"
             "you take {takedown} down, pass {them} around,\n"
             "{after} bottle{amul} of beer on the wall.\n")
    takedown_ = ei.EnhancedInt(takedown).as_words()
    for ib in range(start, 0, -takedown):
        if ib < takedown:
            break
        verse_ = verse.format(
            before=ei.EnhancedInt(ib).as_words(),
            bmul = ('s', '')[ib==1],
            takedown=takedown_,
            them=('it', 'them')[takedown > 1],
            after=ei.EnhancedInt(ib-takedown).as_words(),
            amul = ('s', '')[ib-takedown==1],
        )
        print(verse_)


def old_macdonald(animals):
    """Print the 'old macdonald' song with an arbitrary dictionary of animals and sounds.

    :param dict animals: a dictionary with the animals on macdonald's farm, where the keys are the
                         animal's names and the values are the respective sounds the animals make.
    """

    verse = ("old macdonald had a farm, E-I-E-I-O\n"
             "and on that farm he had a {animal}, E-I-E-I-O\n"
             "with a {sound} {sound} here and a {sound} {sound} there,\n"
             "here a {sound}, there a {sound}, everywhere a {sound} {sound}\n"
             "old macdonald had a farm, E-I-E-I-O\n")
    for animal, sound in animals.items():
        verse_ = verse.format(
            animal=animal,
            sound=sound,
        )
        print(verse_)


def run():
    """Execute the challenges.042e module."""
    print("================")
    print("BEER BOTTLE SONG")
    print("================\n")
    bottles_of_beer(60, 15)

    print("===================")
    print("OLD MACDONALDS SONG")
    print("===================\n")
    animals = {
        'cow': 'moo',
        'chicken': 'cluck',
        'turkey': 'gobble',
        'kangaroo': "g'day",
        't-rex': 'GAAAAARGH',
        'squirrel': '...',
    }
    old_macdonald(animals)

