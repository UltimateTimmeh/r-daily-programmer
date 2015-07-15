#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/s6bas/4122012_challenge_39_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/039e.py

| **Challenge name:** FizzBuzz (reddit_, source_)
| **Challenge number:** 39
| **Difficulty:** Easy
| **Submission date:** 2012-04-12
| **Status:** Complete

Description
-----------

You are to write a function that displays the numbers from 1 to an input parameter n, one per line,
except that if the current number is divisible by 3 the function should write “Fizz” instead of the
number, if the current number is divisible by 5 the function should write “Buzz” instead of the
number, and if the current number is divisible by both 3 and 5 the function should write “FizzBuzz”
instead of the number.

For instance, if n is 20, the program should write::

    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz

Taken from `programmingpraxis.com <http://www.programmingpraxis.com>`_

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 039e

    Solution to the challenge example {3: Fizz, 5: Buzz}:
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz

    Solution to the same, but with added difficulty {3: Fizz, 5: Buzz, 7: Jazz}:
    1
    2
    Fizz
    4
    Buzz
    Fizz
    Jazz
    8
    Fizz
    Buzz
    11
    Fizz
    13
    Jazz
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz
    FizzJazz
    22
    23
    Fizz
    Buzz
    26
    Fizz
    Jazz
    29
    FizzBuzz
    31
    32
    Fizz
    34
    BuzzJazz

Module contents
---------------
"""


def counting_game(n, factors={3: 'Fizz', 5: 'Buzz'}):
    """Return the solution to a general version of the FizzBuzz counting game.

    In the FizzBuzz counting game you count numbers out loud, starting at 1. Every time you
    encounter a multiple of three, you say 'Fizz' instead. Every time you encounter a multiple of
    five, you say 'Buzz' instead. If a number is a multiple of both three and five, you say
    'FizzBuzz'. This function determines the solution to this game up to a chosen number, with the
    ability to provide a custom dictionary of factors and matching replacement words.

    :param int n: the number up to which the solution needs to be determined (inclusive)
    :param factors: dictionary mapping factors to replacement words (default {3: 'Fizz', 5: 'Buzz'})
    :type factors: dict(int: str, ...)
    :return: list containing the solution
    :rtype: list(str, ...)

    Example::

        >>> counting_game(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
    """
    solution = []
    for i in range(1, n+1):
        replace = ''.join([('', word)[i%fac==0] for fac, word in factors.items()])
        if replace:
            solution.append(replace)
        else:
            solution.append(str(i))
    return solution


def run():
    """Execute the challenges.039e module."""
    print("\nSolution to the challenge example {3: Fizz, 5: Buzz}:")
    fb = counting_game(20)
    print('\n'.join(fb))
    print("\nSolution to the same, but with added difficulty {3: Fizz, 5: Buzz, 7: Jazz}:")
    fbj = counting_game(35, factors={3: 'Fizz', 5: 'Buzz', 7: 'Jazz'})
    print('\n'.join(fbj))

