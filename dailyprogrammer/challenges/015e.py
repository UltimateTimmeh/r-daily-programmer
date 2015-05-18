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

**Contents of file** ``input/015e_example_input.txt``::

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

    $ python3 dailyprogrammer.py 015e
    Input file? > input/015e_example_input.txt
    Desired alignment ('<', '>', '^')? > ^
    Output file? > output/015e_example_output.txt
    Note: Data has been written to file 'output/015e_example_output.txt'.

**Contents of file** ``output/015e_example_output.txt``::

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

from plugins.enhancedstring import EnhancedString


def run():
    """Execute the challenges.015e module."""
    # Get user input.
    text_in_fn = input("Input file? > ")
    a = input("Desired alignment ('<', '>', '^')? > ")
    text_out_fn = input("Output file? > ")

    # Read, justify and write.
    with open(text_in_fn, 'r') as text_in_file:
        text = EnhancedString(text_in_file.read())
    text.align(a)
    with open(text_out_fn, 'w') as text_out_file:
        text_out_file.write(str(text))
    print("Note: Data has been written to file '{}'.".format(text_out_fn))

