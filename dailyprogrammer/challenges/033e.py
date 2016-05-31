#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rl24e/3302012_challenge_33_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/033e.py

| **Challenge name:** Study Tool (reddit_, source_)
| **Challenge number:** 33
| **Difficulty:** Easy
| **Submission date:** 2012-03-30
| **Status:** Complete

Description
-----------

This would be a good study tool too. I made one myself and I thought it would also be a good
challenge.

Write a program that prints a string from a list at random, expects input, checks for a right or
wrong answer, and keeps doing it until the user types "exit". If given the right answer for the
string printed, it will print another and continue on. If the answer is wrong, the correct answer
is printed and the program continues.

Bonus: Instead of defining the values in the program, the questions/answers is in a file, formatted
for easy parsing.

*Example file*::

    12 * 12?,144
    What is reddit?,website with cats
    Translate: hola,hello

Thanks to Iggyhopper for the challenge at `/r/dailyprogrammer_ideas <http://www.reddit.com/r/dailyprogrammer_ideas>`_.

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 033e
    12 * 12?
    > 144
    Correct!
    What is reddit?
    > website without cats
    Incorrect, correct answer was: website with cats
    Translate: hola
    > hello
    Correct!
    12 * 12?
    > exit

Imported plugins
----------------

| None

Module contents
---------------
"""

import os
import random

from plugins import config as cfg
from plugins import utils


def read_study_tool_file(fn):
    """Read the contents of a study too file.

    A study tool file is a simple text file that contains a question and its answer, separated by a
    comma, on each line. The file is loaded as a list containing (question, answer) couples.

    :param str fn: path to the study tool file
    :return: list containing (question, answer) couples.
    :rtype: list(list(str, str), ...)

    Example::

        >>> read_study_tool_file('input/033e_example_input.txt')
        [['12 * 12?', '144'], ['What is reddit?', 'website with cats'], ['Translate: hola', 'hello']]
    """
    with open(fn, 'r') as fil:
        lines = fil.readlines()
    return [line.strip().split(',') for line in lines]


def run():
    """Execute the challenges.033e module."""
    cont = True
    while cont:
        datafp = os.path.join(cfg.input_dir, '033e_example_input.txt')
        data = read_study_tool_file(datafp)
        random.shuffle(data)
        for question, expected in data:
            answer = utils.get_input("{}\n> ".format(question))
            if answer == 'exit':
                cont = False
                break
            if answer == expected:
                print("Correct!")
            else:
                print("Incorrect, correct answer was: {}".format(expected))

