#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/pi.py

Various functions for accurately calculating pi to an arbitrary precision (source_).
"""

from decimal import Decimal, getcontext
from math import factorial


def trunc(dec, tr):
    """Truncate a number.

    :param Decimal dec: number to truncate
    :param int tr: amount of trailing digits to remove from the number
    :return: the truncated number
    :rtype: Decimal

    Example::

        >>> from decimal import Decimal
        >>> from pi import trunc
        >>> pi = Decimal('3.141592')
        >>> trunc(pi, 4)
        Decimal('3.14')
    """
    return Decimal(str(dec)[:-tr])


def bbp(prec=15, ptol=2):
    """Calculate pi with the Bailey-Borwein-Plouffe formula.

    See the Wikipedia entry on the `Bailey-Borwein-Plouffe formula <http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula>`_
    for more information.

    :param int prec: desired precision (default 15)
    :param int ptol: increase of precision during calculation to account for incorrect final digits,
                     will be removed after calculation to get the desired precision (default 2)
    :return: the number pi calculated to the desired precision
    :rtype: Decimal

    Example::

        >>> from pi import bbp
        >>> bbp()
        Decimal('3.141592653589793')
        >>> import math
        >>> float(bbp()) == math.pi
        True
    """
    getcontext().prec = prec + 1 + ptol
    pi = Decimal(0)
    k = 0
    while True:
        newpi = pi + (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                                           (Decimal(2)/(8*k+4)) - \
                                           (Decimal(1)/(8*k+5)) - \
                                           (Decimal(1)/(8*k+6)))
        if pi == newpi:
            break
        pi = newpi
        k += 1
    return trunc(pi, ptol)


def bellard(prec=15, ptol=2):
    """Calculate pi with Bellard's formula.

    See the Wikipedia entry on `Bellard's formula <http://en.wikipedia.org/wiki/Bellard%27s_formula>`_
    for more information.

    :param int prec: desired precision (default 15)
    :param int ptol: increase of precision during calculation to account for incorrect final digits,
                     will be removed after calculation to get the desired precision (default 2)
    :return: the number pi calculated to the desired precision
    :rtype: Decimal

    Example::

        >>> from pi import bellard
        >>> bellard()
        Decimal('3.141592653589793')
        >>> import math
        >>> float(bellard()) == math.pi
        True
    """
    getcontext().prec = prec + 1 + ptol
    pi = Decimal(0)
    k = 0
    while True:
        newpi = pi + (Decimal(-1)**k/(1024**k))*(Decimal(256)/(10*k+1) + \
                                                 Decimal(1)/(10*k+9) - \
                                                 Decimal(64)/(10*k+3) - \
                                                 Decimal(32)/(4*k+1) - \
                                                 Decimal(4)/(10*k+5) - \
                                                 Decimal(4)/(10*k+7) - \
                                                 Decimal(1)/(4*k+3))
        if pi == newpi:
            break
        pi = newpi
        k += 1
    pi = pi * 1/(2**6)
    return trunc(pi, ptol)


def chudnovsky(prec=15, ptol=2):
    """Calculate pi with the Chudnovsky algorithm.

    See the Wikipedia entry on the `Chudnovsky algorithm <http://en.wikipedia.org/wiki/Chudnovsky_algorithm>`_
    for more information.

    :param int prec: desired precision (default 15)
    :param int ptol: increase of precision during calculation to account for incorrect final digits,
                     will be removed after calculation to get the desired precision (default 2)
    :return: the number pi calculated to the desired precision
    :rtype: Decimal

    Example::

        >>> from pi import chudnovsky
        >>> chudnovsky()
        Decimal('3.141592653589793')
        >>> import math
        >>> float(chudnovsky()) == math.pi
        True
    """
    getcontext().prec = prec + 1 + ptol
    pi = Decimal(0)
    k = 0
    while True:
        newpi = pi + (Decimal(-1)**k) * (Decimal(factorial(6*k)) / \
                     ((factorial(k)**3)*(factorial(3*k))) * \
                     (13591409+545140134*k) / (640320**(3*k)))
        if pi == newpi:
            break
        pi = newpi
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return trunc(pi, ptol)
