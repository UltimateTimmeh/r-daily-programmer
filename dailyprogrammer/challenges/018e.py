#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qit0h/352012_challenge_18_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/018e.py

| **Challenge name:**  Easy Phone Number (reddit_, source_)
| **Challenge number:** 18
| **Difficulty:** Easy
| **Submission date:** 2012-03-05
| **Status:** Complete

Description
-----------

Often times in commercials, phone numbers contain letters so that they're easy to remember
(e.g. 1-800-VERIZON). Write a program that will convert a phone number that contains letters
into a phone number with only numbers and the appropriate dash. Click `here
<http://en.wikipedia.org/wiki/Telephone_keypad>`_ to learn more about the telephone keypad.

**Example Execution**: Input: 1-800-COMCAST Output: 1-800-266-2278

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 018e
    Input: 1-800-COMCAST
    Output: 1-800-266-2278

Module contents
---------------
"""

from plugins.phonenumber import PhoneNumber


def run():
    """Execute the challenges.018e module."""
    nr = PhoneNumber(input("Input: "))
    print("Output: " + nr.transform_to_format('x-xxx-xxx-xxxx'))

