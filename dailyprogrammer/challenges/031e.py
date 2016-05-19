#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/031e.py

| **Challenge name:** Base 26 Multiplication (reddit_, source_)
| **Challenge number:** 31
| **Difficulty:** Easy
| **Submission date:** 2012-03-27
| **Status:** Complete

Description
-----------

Write a function that takes two base-26 numbers in which digits are represented by letters with
``A=0, B=1, … Z=25`` and returns their product using the same notation. As an example,
``CSGHJ * CBA = FNEUZJA``.

Your task is to write the base-26 multiplication function.

Try to be very efficient in your code!

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 031e
    First base 26 number (A - Z): CSGHJ
    Second base 26 number (A - Z): CBA
    Multiplication of both numbers: FNEUZJA

Module contents
---------------

| *var* challenges.031e.\ **map_nrs2ltrs** *(dict(int: str, ...))*
|     dictionary mapping the numbers 0 - 25 to the letters A - Z

| *var* challenges.031e.\ **map_ltrs2nrs** *(dict(int: str, ...))*
|     dictionary mapping the letters A - Z to the numbers 0 - 25
"""

from plugins import utils

map_nrs2ltrs = {
    nr: ltr for nr, ltr in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
}
map_ltrs2nrs = {
    ltr: nr for nr, ltr in map_nrs2ltrs.items()
}


class EnhancedInt(object):
    """A class representing an enhanced integer object.

    This class' main purpose is to enhance the built-in integer object with several useful methods
    and the ability to perform arithmetic operations with two integers in arbitrary bases.

    .. note:: For now this class only supports **positive** integers in arbitrary base.

    :param digits: digits of the number as integer (for arbitrary base up to 10), string with
                   digits separated by a colon (for any arbitrary base) or list of digits (for any
                   arbitrary base)
    :type digits: int, str or list(int, ...)
    :param int base: base in which the enhanced integer is represented (default 10)
    :raise: TypeError if initialized with an integer for bases higher than 10
    :raise: ValueError if the enhanced integer is invalid (digit-values equal to or higher than
            base)

    Example::

        >>> print(EnhancedInt(12432525))
        12432525 (b10)
        >>> print(EnhancedInt(57332215, 8))
        57332215 (b8)
        >>> print(EnhancedInt('6:45:85:25', 125))
        6:45:85:25 (b125)
        >>> print(EnhancedInt(12432525, 15))
        Traceback (most recent call last):
          ...
        TypeError: Improperly defined digit-values in base 15: '12432525'.
        For bases higher than 10, digits should be separated with a colon or should be a list of integers.
        >>> print(EnhancedInt(12432525, 2))
        Traceback (most recent call last):
          ...
        ValueError: Invalid number in base 2: '12432525'
    """


    def __init__(self, digits, base=10):
        """Create a new enhanced integer."""
        if base > 10 and isinstance(digits, int):
            errmsg = "Improperly defined digit-values in base {}: '{}'.\n"
            errmsg += "For bases higher than 10, digits should be separated with a colon "
            errmsg += "or should be a list of integers."
            raise TypeError(errmsg.format(base, digits))
        elif isinstance(digits, int):
            self.digits = [int(digit) for digit in str(digits)]
        elif isinstance(digits, str):
            self.digits = [int(digit) for digit in digits.split(':')]
        else:
            self.digits = digits
        self.base = base

        if not self.__valid__():
            raise ValueError("Invalid number in base {}: '{}'".format(base, digits))


    def __valid__(self):
        """Determine if the enhanced integer is valid.

        An enhanced integer is valid if all digits are smaller than the base.
        """
        return all([digit < self.base for digit in self.digits])


    def __str__(self):
        """Format the enhanced integer as a string."""
        nr = {True: ':', False: ''}[self.base > 10].join([str(digit) for digit in self.digits])
        return '{} (b{})'.format(nr, self.base)


    def __mul__(self, other):
        """Multiply two enhanced integers with arbitrary (possibly different) bases.

        Note that the returned enhanced string has the same base as self (the first number).
        """
        result = self.__class__(self.base10()*other.base10())
        result.convert(self.base)
        return result


    def base10(self):
        """Return the conversion of the enhanced integer to base 10 as an integer.

        :return: conversion of the enhanced integer to base 10
        :rtype: int

        Example::

            >>> EnhancedInt('6:45:85:25', 125).base10()
            12432525
        """
        base10 = 0
        for power, digit in enumerate(self.digits[::-1]):
            base10 += digit * self.base**power
        return base10


    def convert(self, newbase):
        """Convert the enhanced integer to another base.

        :param int newbase: the base to which the enhanced integer should be converted

        Example::

            >>> nr = EnhancedInt(12432525)
            >>> for newbase in [2, 8, 10, 125]:
            ...     nr.convert(newbase)
            ...     print(nr)
            ...
            101111011011010010001101 (b2)
            57332215 (b8)
            12432525 (b10)
            6:45:85:25 (b125)
        """
        base10 = self.base10()
        self.base = newbase
        if base10 == 0:  ## If the number is zero, only the base needs to change.
            return
        self.digits = []
        while base10 > 0:
            self.digits.insert(0, base10 % newbase)
            base10 = base10 // newbase


def run():
    """Execute the challenges.031e module."""
    nr1 = utils.get_input('First base 26 number (A - Z): ').upper()
    nr2 = utils.get_input('Second base 26 number (A - Z): ').upper()
    nr1 = EnhancedInt([map_ltrs2nrs[char] for char in nr1], 26)
    nr2 = EnhancedInt([map_ltrs2nrs[char] for char in nr2], 26)
    result = ''.join([map_nrs2ltrs[digit] for digit in (nr1 * nr2).digits])
    print("Multiplication of both numbers: {}".format(result))

