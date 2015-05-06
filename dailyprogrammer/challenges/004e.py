#!/usr/bin/python3
"""
Challenge information
---------------------

| **Challenge name:** `Random Password <http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/>`_
| **Challenge number:** 4
| **Difficulty:** Easy
| **Submission date:** 2012-02-12
| **Status:** Complete

Challenge description
---------------------

Your challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to generate.

For even more extra credit, allow the user to specify the length of the strings he wants to
generate!

Challenge module contents
-------------------------
"""

from plugins import password


def run():
    """Execute the challenges.004e module."""
    # Ask for input.
    np = int(input("Amount of passwords > "))
    lp = int(input("Password length > "))

    # Generate the passwords.
    pwds = [password.random_password(l=lp) for ii in range(np)]
    print("===PASSWORDS===")
    print('\n'.join(["{}. {}".format(pi+1, pwd) for pi, pwd in enumerate(pwds)]))
    print("="*15)
