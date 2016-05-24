#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/enhancedint.py

Enchance the built-in int object with useful methods (source_).
"""


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
        TypeError: Improperly defined digit-values in base 15: 12432525.
        For bases higher than 10, digits should be separated with a colon or should be a list of integers.
        >>> print(EnhancedInt(12432525, 2))
        Traceback (most recent call last):
          ...
        ValueError: Invalid number in base 2: '12432525'
    """


    def __init__(self, digits, base=10):
        """Create a new enhanced integer."""
        if base > 10 and isinstance(digits, int):
            errmsg = "Improperly defined digit-values in base {}: {}.\n"
            errmsg += "For bases higher than 10, digits should be separated with a colon "
            errmsg += "or should be a list of integers."
            raise TypeError(errmsg.format(base, digits))
        if isinstance(digits, int):
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
        return self.__class__(self.base10()*other.base10()).convert(self.base)


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
        :return: the converted enhanced integer
        :rtype: EnhancedInt

        Example::

            >>> nr = EnhancedInt(12432525)
            >>> for newbase in [2, 8, 10, 125]:
            ...     print(nr.convert(newbase))
            ...
            101111011011010010001101 (b2)
            57332215 (b8)
            12432525 (b10)
            6:45:85:25 (b125)
        """
        base10 = self.base10()
        if base10 == 0:  ## If the number is zero, only the base needs to change.
            return self.__class__([0], newbase)
        newdigits = []
        while base10 > 0:
            newdigits.insert(0, base10 % newbase)
            base10 //= newbase
        return self.__class__(newdigits, newbase)


    def as_words(self):
        """Return a word representation of the integer in base 10.

        :return: a word representation of the integer in base 10
        :rtype: str

        Example::

            >>> EnhancedInt(0).as_words()
            'zero'
            >>> EnhancedInt(123456).as_words()
            'one hundred twenty-three thousand four hundred fifty-six'
            >>> nr = EnhancedInt(int(453E20))
            >>> print(nr)
            45300000000000003145728 (b10)
            >>> nr.as_words()
            'forty-five sextillion three hundred quitillion three million one hundred forty-five thousand seven hundred twenty-eight'
        """
        units = ' one two three four five six seven eight nine'.split(' ')
        teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'
        teens = teens.split()
        tens = '  twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')
        thousands = (' thousand million billion trillion quadrillion quitillion sextillion'
                     ' septillion octillion nonillion decillion undecillion duodecillion'
                     ' tredecillion quattuordecillion quindecillion sexdecillion septendecillion'
                     ' octodecillion novemdecillion vigintillion').split(' ')
        num = self.base10()
        words = []
        if num == 0:
            words.append('zero')
        else:
            if num < 0:
                words.append('minus')
                num = abs(num)
            num_str = str(num)
            groups = (len(num_str)+2) // 3
            num_str = num_str.zfill(groups*3)
            for i in range(0, groups*3, 3):
                h, t, u = map(int, num_str[i:i+3])
                g = groups - (i//3+1)
                if h >= 1:
                    words.append(units[h])
                    words.append('hundred')
                if t > 1:
                    word = tens[t]
                    if u >= 1:
                        word += '-' + units[u]
                    words.append(word)
                elif t == 1:
                    words.append(teens[u])
                elif u >= 1:
                    words.append(units[u])
                if g >= 1 and (h+t+u) > 0:
                    words.append(thousands[g])
        return ' '.join(words)

