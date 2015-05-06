#!/usr/bin/python3
"""
Challenge information
---------------------

| **Challenge name:** `Caesar Cipher <http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/>`_
| **Challenge number:** 3
| **Difficulty:** Easy
| **Submission date:** 2012-02-11
| **Status:** Complete

Challenge description
---------------------

Welcome to cipher day!

Write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore
numbers, symbols, and whitespace.

For extra credit, add a "decrypt" function to your program!

Challenge module contents
-------------------------
"""

from plugins import cipher


def run():
    """Execute the challenges.003e module."""
    # Ask for input
    msg = input("Message to encode > ")
    n = int(input("Amount of right shift > "))

    # Play with the input
    print("Original message: " + msg)
    msg_encoded = cipher.caesar(msg, n)
    print("Encoded message: " + msg_encoded)
    msg_decoded = cipher.caesar(msg_encoded, n, dir='decode')
    print("Decoded encoded message: " + msg_decoded)
    options = cipher.caesar_brute_force(msg_encoded)
    print("Brute-force-decoded encoded message:")
    print('\n'.join(options))
