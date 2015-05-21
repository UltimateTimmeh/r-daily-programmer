#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/020e.py

| **Challenge name:**  Find Primes (reddit_, source_)
| **Challenge number:** 20
| **Difficulty:** Easy
| **Submission date:** 2012-03-08
| **Status:** Complete

Description
-----------

Create a program that will find all prime numbers below 2000.

Example run
-----------

::

    $ python3 dailyprogrammer.py 020e
    Find all prime numbers up to and including: 2000
       2,    3,    5,    7,   11,   13,   17,   19,   23,   29,   31,   37,   41
      43,   47,   53,   59,   61,   67,   71,   73,   79,   83,   89,   97,  101
     103,  107,  109,  113,  127,  131,  137,  139,  149,  151,  157,  163,  167
     173,  179,  181,  191,  193,  197,  199,  211,  223,  227,  229,  233,  239
     241,  251,  257,  263,  269,  271,  277,  281,  283,  293,  307,  311,  313
     317,  331,  337,  347,  349,  353,  359,  367,  373,  379,  383,  389,  397
     401,  409,  419,  421,  431,  433,  439,  443,  449,  457,  461,  463,  467
     479,  487,  491,  499,  503,  509,  521,  523,  541,  547,  557,  563,  569
     571,  577,  587,  593,  599,  601,  607,  613,  617,  619,  631,  641,  643
     647,  653,  659,  661,  673,  677,  683,  691,  701,  709,  719,  727,  733
     739,  743,  751,  757,  761,  769,  773,  787,  797,  809,  811,  821,  823
     827,  829,  839,  853,  857,  859,  863,  877,  881,  883,  887,  907,  911
     919,  929,  937,  941,  947,  953,  967,  971,  977,  983,  991,  997, 1009
    1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091
    1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187
    1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283
    1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381
    1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481
    1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567
    1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657
    1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753
    1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871
    1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979
    1987, 1993, 1997, 1999

Module contents
---------------
"""


def sieve_of_eratosthenes(limit):
    """Find all primes up to a certain limit.

    This function makes use of the `Sieve of Eratosthenes <http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`_
    to find all prime numbers up to a certain limit.

    :param int limit: upper limit of the algorithm
    :return: list of prime numbers up to the given limit
    :rtype: list

    Example::

        >>> sieve_of_eratosthenes(50)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    if limit <= 1:
        return []
    nrs = list(range(limit + 1))
    i = 2
    while i*i <= limit:
        if nrs[i] == 0:
            i += 1
            continue
        elim = i*i
        while elim <= limit:
            nrs[elim] = 0
            elim += i
        i += 1
    primes = [nr for nr in nrs if nr > 1]
    return primes


def run():
    """Execute the challenges.020e module."""
    limit = int(input("Find all prime numbers up to and including: "))
    primes = sieve_of_eratosthenes(limit)
    end = {True: '\n', False: ', '}
    for i, prime in enumerate(primes):
        print(str(prime).rjust(4), end=end[(i+1)%13==0 or (i+1)==len(primes)])

