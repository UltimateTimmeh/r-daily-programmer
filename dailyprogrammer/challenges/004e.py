#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/004e.py

| **Challenge name:** Random Password (reddit_, source_)
| **Challenge number:** 4
| **Difficulty:** Easy
| **Submission date:** 2012-02-12
| **Status:** Complete

Description
-----------

Your challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to generate.

For even more extra credit, allow the user to specify the length of the strings he wants to
generate!

Example run
-----------

::

    $ python3 dailyprogrammer.py 004e
    Amount of passwords > 5
    Password length > 20
    ===PASSWORDS===
    1. 11m9vLgygmq0P3rqW1yz
    2. Fsp1xRUQUOdkPoRh84Iv
    3. LuF6eilXUKLYK5e43Pdz
    4. 505ZwrKawfJ7mW90Llek
    5. snvga7R4B1wa1EFWqIG2
    ===============

Module contents
---------------
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
