#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qp3ub/392012_challenge_21_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/021e.py

| **Challenge name:**  Next Permutation (reddit_, source_)
| **Challenge number:** 21
| **Difficulty:** Easy
| **Submission date:** 2012-03-09
| **Status:** Complete

Description
-----------

Input: a number

Output: the next higher number that uses the same set of digits.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 021e
    Number: 93765.44321
    Next higher permutation of this number: 94123.34567

Module contents
---------------
"""


def deconstruct_number(number):
    """Deconstruct a number into a list of digits and the location of the dot (if any).

    :param number: the number to deconstruct
    :type number: int or float
    :return: tuple with the list containing the number's digits and the location of the number's
             dot (if any)
    :rtype: tuple(list(int, ...), None or int)

    Example::

        >>> deconstruct_number(123)
        ([1, 2, 3], None)
        >>> deconstruct_number(456.123)
        ([4, 5, 6, 1, 2, 3], 3)
    """
    dot = None
    digits = []
    for n, digit in enumerate(str(number)):
        if digit == '.':
            dot = n
        else:
            digits.append(int(digit))
    return digits, dot


def construct_number(digits, dot=None):
    """Construct a number from a list of digits and the location of the dot (if any).

    :param digits: the list of digits
    :type digits: list(int, ...)
    :param dot: the location of the number's dot (if any) (default None)
    :type dot: None or int
    :return: the reconstructed number
    :rtype: int or float

    Example::

        >>> construct_number([1, 2, 3])
        123
        >>> construct_number([4, 5, 6, 1, 2, 3], dot=3)
        456.123
    """
    digits = [str(digit) for digit in digits]
    if dot is None:
        return int(''.join(digits))
    else:
        digits.insert(dot, '.')
        return float(''.join(digits))


def next_permutation(number):
    """Determine the next higher permutation of an integer or float number.

    :param number: number of which next higher permutation should be computed
    :type number: int or float
    :return: the next higher permutation of the number
    :rtype: int or float

    Example::

        >>> next_permutation(123)
        132
        >>> next_permutation(321)
        321
        >>> next_permutation(123.4321)
        124.1233
    """
    # Deconstruct the number.
    number, dot = deconstruct_number(number)  ## Deconstruct the number.
    # Find the first digit that is not ordered from low to high.
    i = len(number)-2
    while i >= 0 and number[i] >= number[i+1]:
        i -= 1
    if i == -1:  ## All digits are ordered, there is no next higher permutation!
        return construct_number(number, dot=dot)
    # Find the first digit in the ordered subsequence that is higher than the first unordered digit.
    j = len(number) - 1
    while number[j] <= number[i]:
        j -= 1
    # Swap these two digits.
    backup = number[i]
    number[i] = number[j]
    number[j] = backup
    # Reverse the ordered subsequence and return the result.
    number = number[:i+1] + number[i+1:][::-1]
    return construct_number(number, dot=dot)


def run():
    """Execute the challenges.021e module."""
    number = input("Number: ")
    number = {True: float, False: int}['.' in number](number)
    newnumber = next_permutation(number)
    if newnumber != number:
        print("Next higher permutation of this number: {}".format(newnumber))
    else:
        print("There is no next higher permutation for this number!")

