#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/006e.py

| **Challenge name:** Calculate Pi (reddit_, source_)
| **Challenge number:** 6
| **Difficulty:** Easy
| **Submission date:** 2012-02-14
| **Status:** Complete

Description
-----------

Your challenge for today is to create a program that can calculate pi accurately to at least 30
decimal places.

Try not to cheat :-).

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 006e
    === Choose the desired method for the calculation of pi ===
    1. Bailey-Borwein-Plouffe formula
    2. Bellard's formula
    3. Chudnovsky algorithm
    q. Quit
    Choose menu item > 1
    Desired precision for calculation of pi: 30

    Calculation of pi up to 30 digits:
        3.141592653589793238462643383279
    Pi calculated up to 30 digits should be:
        3.141592653589793238462643383279
    The calculation appears to be correct!

    === Choose the desired method for the calculation of pi ===
    1. Bailey-Borwein-Plouffe formula
    2. Bellard's formula
    3. Chudnovsky algorithm
    q. Quit
    Choose menu item > q

Module contents
---------------
"""

from decimal import Decimal, getcontext
from math import factorial

from plugins import textmenu
from plugins import utils


def trunc(dec, tr):
    """Truncate a decimal number.

    :param Decimal dec: number to truncate
    :param int tr: amount of trailing digits to remove from the number
    :return: the truncated number
    :rtype: Decimal

    Example::

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


def calc_pi(func, pi_exp='3.141592653589793238462643383279'):
    """Calculate pi up to a desired precision with the provided function and compare with expected.

    The user is asked for the desired precision of the calculation of pi. Pi is then calculated
    up to that precision using the provided function, and the result is compared with the expected
    value.

    :param Callable func: the function with which pi should be calculated
    :param str pi_exp: the expected value of pi (default '3.141592653589793238462643383279')
    """
    prec_exp = len(pi_exp) - 2
    prec_calc = int(utils.get_input("Desired precision for calculation of pi: "))
    pi_calc = str(func(prec_calc))
    print("\nCalculation of pi up to {} digits:\n    {}".format(prec_calc, pi_calc))
    print("Pi calculated up to {} digits should be:\n    {}".format(prec_exp, pi_exp))
    if prec_calc <= prec_exp and pi_calc in pi_exp:
        print("The calculation appears to be correct!\n")
    elif prec_calc > prec_exp and pi_exp in pi_calc:
        msg = "The calculation appears to be correct (at least for the first {} digits)!\n"
        print(msg.format(prec_exp))
    else:
        print("The calculation appears to be incorrect!\n")


def run():
    """Execute the challenges.006e module."""
    # Create the menus.
    main_title = 'Choose the desired method for the calculation of pi'
    main_menuitems = [
        textmenu.TextMenuItem('1', lambda: calc_pi(bbp), "Bailey-Borwein-Plouffe formula"),
        textmenu.TextMenuItem('2', lambda: calc_pi(bellard), "Bellard's formula"),
        textmenu.TextMenuItem('3', lambda: calc_pi(chudnovsky), "Chudnovsky algorithm"),
        textmenu.TextMenuItem('q', 'quit', 'Quit')
    ]
    menus = {
        'main': textmenu.TextMenu(main_title, main_menuitems),
    }
    textmenu.TextMenuEngine(menus, 'main').run()

