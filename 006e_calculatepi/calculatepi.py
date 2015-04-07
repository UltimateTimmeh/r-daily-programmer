#!/usr/bin/python3
"""
Accurately calculate pi to a certain precision using the desired formula.

Usage: python3.4 calculatepi.py <formula> <prec>
"""

from decimal import Decimal, getcontext
from math import factorial
import sys


def bbp():
    """Use Bailey-Borwein-Plouffe's formula to calculate pi."""
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
    return pi


def bellard():
    """Use Bellard's formula to calculate pi."""
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
    return pi


def chudnovsky():
    """Use Chudnovsky's formula to calculate pi."""
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
    return pi


if __name__ == '__main__':

    # Make sure the usage is correct.
    if len(sys.argv) != 3:
        sys.exit("Argument error, use: python3.4 calculatepi.py <formula> <prec>")

    # Extract sys.argv values.
    formula = sys.argv[1]
    precision = int(sys.argv[2])

    # Check if requested formula exists.
    formulas = {
        'bbp': bbp,
        'bellard': bellard,
        'chudnovsky': chudnovsky,
        }
    if formula not in formulas:
        sys.exit("Formula error: formula '{}' does not exist.".format(formula))
    else:
        print("\nUsing formula '{}'...".format(formula))

    # Calculate pi and print result.
    getcontext().prec = precision+1
    pi = formulas[formula]()
    print("...pi calculated to {} decimal points is:\n    {}".format(precision, pi))

    # Compare with the first 74 digits of pi.
    with open('pi_74.txt', 'r') as pi_file:
        pi_string = pi_file.read()
    print("This is what pi should look like to 74 decimal points:")
    print("    {}".format(pi_string))


# End
