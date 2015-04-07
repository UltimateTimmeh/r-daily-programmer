#!/usr/bin/python3
"""
Generate p random passwords with length l. Includes alphanumerical characters
and some symbols.

To use in a terminal:

$ python3.x randompassword.py p l

Where p and l are integers.
"""

import random
import sys


def generate_passwords(p, l):
    """Generate p random password consisting of l characters."""
    symbols = "abcdefghijklmnopqrstuvwxyz0123456789<>?!@#$%^&*()_+-=[];{}:"
    symbols += "ABCDEFGHILJKLMNOPQRSTUVWXYZ"
    passwords = []
    for ii in range(p):
        password = [symbols[random.randint(0,len(symbols)-1)] \
                    for jj in range(l)]
        password = ''.join(password)
        passwords.append(password)
    return passwords


if __name__ == '__main__':
    # Get the command line options.
    p = int(sys.argv[1])
    l = int(sys.argv[2])
    for password in generate_passwords(p, l):
        print(password)

# End
