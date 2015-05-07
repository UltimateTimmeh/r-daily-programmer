#!/usr/bin/python3
"""
Challenge information
---------------------

| **Challenge name:** `Ask Input <http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/>`_
| **Challenge number:** 1
| **Difficulty:** Easy
| **Submission date:** 2012-02-10
| **Status:** Complete

Challenge description
---------------------

Create a program that will ask the user's name, age, and reddit username.
Have it tell them the information back, in the format::

    Your name is (blank), you are (blank) years old, and your username is (blank).

For extra credit, have the program log this information in a file to be accessed
later.

Challenge module contents
-------------------------
"""

import os
import plugins.config as cfg
from plugins import user


def run():
    """Execute the challenges.001e module."""
    # Ask for input.
    name = input("Name? > ")
    age = input("Age? > ")
    reddit_username = input("Reddit Username? > ")

    # Create PersonalInfo object, print and write to file.
    pi = user.User(name=name, age=age, reddit_username=reddit_username)
    print(pi)
    outputfile_fn = os.path.join(cfg.output_dir, '001e_example_output.txt')
    pi.write(outputfile_fn)
    print("Note: Data has been appended to file '{}'".format(outputfile_fn))
