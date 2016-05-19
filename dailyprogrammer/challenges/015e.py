#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/015e.py

| **Challenge name:**  Align Text (reddit_, source_)
| **Challenge number:** 15
| **Difficulty:** Easy
| **Submission date:** 2012-02-24
| **Status:** Complete

Description
-----------

Write a program to left or right justify a text file.

Example run
-----------

**Contents of file** ``015e_example_input.txt``::

    Short line 1
    Short line 2
    A bit longer line 1
    Short line 3
    A bit longer line 2
    This is very long line number one
    This is very long line number two
    A bit longer line 3
    This is very long line number three

**Running the challenge module**::

    $ python3 dailyprogrammer.py execute 015e
    Input file? > 015e_example_input.txt
    Desired alignment ('<', '>', '^')? > ^
    Output file? > 015e_example_output.txt
    Note: Data has been written to file '015e_example_output.txt'.

**Contents of file** ``015e_example_output.txt``::

               Short line 1
               Short line 2
            A bit longer line 1
               Short line 3
            A bit longer line 2
     This is very long line number one
     This is very long line number two
            A bit longer line 3
    This is very long line number three

Module contents
---------------
"""

import os

from plugins import config as cfg
from plugins import enhancedstring as estr
from plugins import utils


def run():
    """Execute the challenges.015e module."""
    # Get user input.
    textinfn = utils.get_input("Input file? > ")
    a = utils.get_input("Desired alignment ('<', '>', '^')? > ")
    textoutfn = utils.get_input("Output file? > ")

    # Read, align and write.
    textinfp = os.path.join(cfg.input_dir, textinfn)
    textoutfp = os.path.join(cfg.output_dir, textoutfn)
    with open(textinfp, 'r') as textinfil:
        text = estr.EnhancedString(textinfil.read())
    text.align(a)
    with open(textoutfp, 'w') as textoutfil:
        textoutfil.write(str(text))
    print("Note: Data has been written to file '{}'.".format(textoutfp))

