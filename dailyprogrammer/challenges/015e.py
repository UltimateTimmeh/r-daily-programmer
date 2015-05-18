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


def align_text(text, a='<'):
    """Left, right or center alignment of text.

    :param str text: the text to be aligned
    :param str a: desired alignment of the text, '<' for left, '>' for right, '^' for center
                  (default '<')
    :return: aligned text
    :rtype: str
    :raise: ValueError if the provided alignment is invalid
    """
    if a not in '<>^':
        error = "Unknown alignment: '{}'."
        raise ValueError(error.format(a))
    text_stripped = [line.strip() for line in text.split('\n')]
    max_length = max([len(line) for line in text_stripped])
    text_aligned = '\n'.join([
        '{0:{1}{2}}'.format(line, a, max_length).rstrip() for line in text_stripped
        ])
    return text_aligned


def run():
    """Execute the challenges.015e module."""
    # Get user input.
    text_in_fn = input("Input file? > ")
    a = input("Desired alignment ('<', '>', '^')? > ")
    text_out_fn = input("Output file? > ")

    # Read, justify and write.
    with open(text_in_fn, 'r') as text_in_file:
        text_in = text_in_file.read()
    text_out = align_text(text_in, a)
    with open(text_out_fn, 'w') as text_out_file:
        text_out_file.write(text_out)
    print("Note: Data has been written to file '{}'.".format(text_out_fn))

