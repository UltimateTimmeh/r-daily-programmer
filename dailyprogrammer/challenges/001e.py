#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/001e.py

| **Challenge name:** Ask Input (reddit_, source_)
| **Challenge number:** 1
| **Difficulty:** Easy
| **Submission date:** 2012-02-10
| **Status:** Complete

Description
-----------

Create a program that will ask the user's name, age, and reddit username.
Have it tell them the information back, in the format::

    Your name is (blank), you are (blank) years old, and your username is (blank).

For extra credit, have the program log this information in a file to be accessed
later.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 001e
    Name? > John Smith
    Age? > 50
    Reddit Username? > johnsmith
    Contents of User object:
        name: John Smith
        age: 50
        reddit_username: johnsmith
    Note: Data has been appended to file '/path/to/project/dailyprogrammer/output/001e_example_output.txt'

Module contents
---------------
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
