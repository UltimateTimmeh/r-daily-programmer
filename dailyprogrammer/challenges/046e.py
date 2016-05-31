#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/szz5y/4302012_challenge_46_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/046e.py

| **Challenge name:** Population Count (reddit_, source_)
| **Challenge number:** 46
| **Difficulty:** Easy
| **Submission date:** 2012-05-01
| **Status:** Complete

Description
-----------

The population count of a bitstring is the number of set bits (1-bits) in the string. For instance,
the population count of the number 23, which is represented in binary as 10111 is 4.

Your task is to write a function that determines the population count of a number representing a
bitstring.

Example run
-----------

.. note:: Simply using ``bin(x).count('1')`` works, but that's boring, so I made my own
          implementation using the :func:`plugins.enhancedint.EnhancedInt` class.

::

    Give me a number ('q' to quit) > 0
    0 (b2) ; 0
    Give me a number ('q' to quit) > 23
    10111 (b2) ; 4
    Give me a number ('q' to quit) > 15698
    11110101010010 (b2) ; 8
    Give me a number ('q' to quit) > 123456789
    111010110111100110100010101 (b2) ; 16
    Give me a number ('q' to quit) > q

Imported plugins
----------------

| :mod:`plugins.enhancedint`

Module contents
---------------
"""

from plugins import enhancedint as ei
from plugins import utils


def population_count(nr):
    """Return the given number's bitstring population count.

    The population count of a number's bitstring is the amount of set bits in the number's
    bitstring. This implementation uses conversion from base 10 to base 2 using the EnhancedInt
    class, after which the sum of the base 2 number's digits is returned. It's probably not the
    fastest way to do it, but it works fast even for a 1938 bit case (see the fourth example).

    :param int nr: the number of which to calculate its bitstring's population count
    :return: the population count
    :rtype: int

    Example::

        >>> population_count(0)
        0
        >>> population_count(23)
        4
        >>> population_count(123456789)
        16
        >>> population_count(12448057941136394342297748548545082997815840357634948550739612798732309975923280685245876950055614362283769710705811182976142803324242407017104841062064840113262840137625582646683068904149296501029754654149991842951570880471230098259905004533869130509989042199261339990315125973721454059973605358766253998615919997174542922163484086066438120268185904663422979603026066685824578356173882166747093246377302371176167843247359636030248569148734824287739046916641832890744168385253915508446422276378715722482359321205673933317512861336054835392844676749610712462818600179225635467147870208)
        19
    """
    return sum(ei.EnhancedInt(nr).convert(2).digits)


def run():
    """Execute the challenges.046e module."""
    while True:
        nr = utils.get_input("Give me a number ('q' to quit) > ").lower()
        if nr == 'q':
            break
        nr = int(nr)
        print(ei.EnhancedInt(nr).convert(2), ';', population_count(nr))

