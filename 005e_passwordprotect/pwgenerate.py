#!/usr/bin/python3
"""
Function to generate random passwords of arbitrary length.
"""

import random


def generate_passwords(p, l):
    """Generate p random password consisting of l characters."""
    symbols = "abcdefghijklmnopqrstuvwxyz0123456789"
    symbols += "ABCDEFGHILJKLMNOPQRSTUVWXYZ"
    passwords = []
    for ii in range(p):
        password = [symbols[random.randint(0,len(symbols)-1)] \
                    for jj in range(l)]
        password = ''.join(password)
        passwords.append(password)
    return passwords


# End
