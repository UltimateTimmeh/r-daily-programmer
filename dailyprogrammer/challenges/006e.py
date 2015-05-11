#!/usr/bin/python3
"""
Challenge information
---------------------

| **Challenge name:** `Calculate Pi <http://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/>`_
| **Challenge number:** 6
| **Difficulty:** Easy
| **Submission date:** 2012-02-14
| **Status:** Complete

Challenge description
---------------------

Your challenge for today is to create a program that can calculate pi accurately to at least 30
decimal places.

Try not to cheat :-).

Challenge module contents
-------------------------
"""

from plugins import pi
from plugins import textmenu


def calc_pi(func, pi_exp='3.141592653589793238462643383279'):
    """Calculate pi up to a desired precision with the provided function and compare with expected.

    The user is asked for the desired precision of the calculation of pi. Pi is then calculated
    up to that precision using the provided function, and the result is compared with the expected
    value.

    :param Callable func: the function with which pi should be calculated
    :param str pi_exp: the expected value of pi (default '3.141592653589793238462643383279')
    """
    prec_exp = len(pi_exp) - 2
    prec_calc = int(input("Desired precision for calculation of pi: "))
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
    bbp = lambda: calc_pi(pi.bbp)
    bellard = lambda: calc_pi(pi.bellard)
    chudnovsky = lambda: calc_pi(pi.chudnovsky)
    main_title = 'Choose the desired method for the calculation of pi'
    main_menuitems = [
        textmenu.TextMenuItem('1', bbp, "Bailey-Borwein-Plouffe formula"),
        textmenu.TextMenuItem('2', bellard, "Bellard's formula"),
        textmenu.TextMenuItem('3', chudnovsky, "Chudnovsky algorithm"),
        textmenu.TextMenuItem('q', 'quit', 'Quit')
    ]
    menus = {
        'main': textmenu.TextMenu(main_title, main_menuitems),
    }
    textmenu.TextMenuEngine(menus, 'main').run()
