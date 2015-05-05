#!/usr/bin/python3
"""
Functions for authenticating users
"""

import random


def random_password(l=8):
    """Generate a random password consisting of `l` characters."""
    symbols = "ABCDEFGHILJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols += "0123456789<>?!@#$%^&*()_+-=[];{}:"
    password = [random.choice(symbols) for ii in range(l)]
    password = ''.join(password)
    return password
