#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/035e.py

| **Challenge name:** Number Triangle (reddit_, source_)
| **Challenge number:** 35
| **Difficulty:** Easy
| **Submission date:** 2012-04-03
| **Status:** Complete

Description
-----------

Write a program that will take a number and print a right triangle attempting to use all numbers
from 1 to that number.

*Sample output:*

::

    Enter number: 10
    Output:
    7 8 9 10
    4 5 6
    2 3
    1

::

    Enter number:  6
    Output:
    4 5 6
    2 3
    1

::

    Enter number:  3
    Output:
    2 3
    1

::

    Enter number:  12
    Output:
    7 8 9 10
    4 5 6
    2 3
    1

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 035e
    Enter number: 6
    4 5 6
    2 3
    1

::

    $ python3 dailyprogrammer.py execute 035e
    Enter number: 12
    7  8  9  10
    4  5  6
    2  3
    1

::

    $ python3 dailyprogrammer.py execute 035e
    Enter number: 15
    11 12 13 14 15
    7  8  9  10
    4  5  6
    2  3
    1

::

    $ python3 dailyprogrammer.py execute 035e
    Enter number: 150
    121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136
    106 107 108 109 110 111 112 113 114 115 116 117 118 119 120
    92  93  94  95  96  97  98  99  100 101 102 103 104 105
    79  80  81  82  83  84  85  86  87  88  89  90  91
    67  68  69  70  71  72  73  74  75  76  77  78
    56  57  58  59  60  61  62  63  64  65  66
    46  47  48  49  50  51  52  53  54  55
    37  38  39  40  41  42  43  44  45
    29  30  31  32  33  34  35  36
    22  23  24  25  26  27  28
    16  17  18  19  20  21
    11  12  13  14  15
    7   8   9   10
    4   5   6
    2   3
    1

.. note:: The amount of triangle levels you can have for a certain number in this challenge is equal
          to the floor of its 'inverse sum of range'. For example, the sum of the range from 1 to 5
          is 15. So if you want to make a triangle containing the numbers ranging from 1 to 15, that
          triangle will have 5 levels. The sum of the range from 1 to 16 is 136. So if you want to
          make a triangle containing the numbers ranging from 1 to 150 (of which the 'inverse sum of
          range' equals roughly 16.828), that triangle will have 16 levels and will only go up to
          136.

Module contents
---------------
"""

import math

from plugins import asciiart as aa
from plugins import utils


def sum_of_range(nr):
    """Determine the sum of the range from 1 to the given number.

    :param int nr: number for which the sum must be calculated
    :return: sum of the range from 1 to the given number
    :rtype: int

    Example::

        >>> sum_of_range(5)
        15
        >>> sum_of_range(12345)
        76205685
    """
    return sum(range(1, nr+1))


def inverse_sum_of_range(sum):
    """Determine the number for which ``sum(range(1, number+1))`` equals the given sum.

    This is the inverse of the sum of the range going from 1 to a certain number, for which the
    formula is ``sum = (nr*(nr+1))/2``. Since the inverse of this equation contains a root, there
    are two possible solutions: one which uses the positive root and one which uses the negative
    root. Since only the solution with the positive root makes sense in this context, only that one
    is returned. Note that the returned number is not necessarily round.

    :param int sum: sum for which the number must be calculated
    :return: number for which ``sum(range(1, number+1))`` equals the given sum
    :rtype: float

    Example::

        >>> inverse_sum_of_range(15)
        5.0
        >>> inverse_sum_of_range(76205685)
        12345.0
        >>> inverse_sum_of_range(12)
        4.424428900898052
    """
    return (math.sqrt(8*sum+1)-1)/2


def run():
    """Execute the challenges.035e module."""
    nr = int(utils.get_input("Enter number: "))
    nlevels = math.floor(inverse_sum_of_range(nr))
    maxnr = sum_of_range(nlevels)
    char_len = len(str(maxnr)) + 1
    chars = ['{1:<{0}}'.format(char_len, n) for n in range(1, maxnr+1)]
    print(aa.TextTriangle(char=chars, nlevels=nlevels, o='v'))

