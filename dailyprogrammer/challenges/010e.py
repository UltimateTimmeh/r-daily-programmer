#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/010e.py

| **Challenge name:**  Validate Phone Number (reddit_, source_)
| **Challenge number:** 10
| **Difficulty:** Easy
| **Submission date:** 2012-02-18
| **Status:** Complete

Description
-----------

The exercise today asks you to validate a telephone number, as if written on an input form.
Telephone numbers can be written as ten digits, or with dashes, spaces, or dots between the
three segments, or with the area code parenthesized; both the area code and any white space
between segments are optional.

Thus, all of the following are valid telephone numbers:

- 1234567890
- 123-456-7890
- 123.456.7890
- (123)456-7890
- \(123) 456-7890 (note the white space following the area code)
- 456-7890

The following are not valid telephone numbers:

- 123-45-6789
- 123:4567890
- 123/456-7890.

Source: http://programmingpraxis.com/2011/12/13/validating-telephone-numbers/

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 010e
    The phone number '1234567890' is valid.
    The phone number '123-456-7890' is valid.
    The phone number '123.456.7890' is valid.
    The phone number '(123)456-7890' is valid.
    The phone number '(123) 456-7890' is valid.
    The phone number '456-7890' is valid.
    The phone number '123-45-6789' is invalid.
    The phone number '123:4567890' is invalid.
    The phone number '123/456-7980' is invalid.

Module contents
---------------
"""

from plugins.phonenumber import PhoneNumber


def run():
    """Execute the challenges.010e module."""
    numbers = [
        '1234567890',
        '123-456-7890',
        '123.456.7890',
        '(123)456-7890',
        '(123) 456-7890',
        '456-7890',
        '123-45-6789',
        '123:4567890',
        '123/456-7980',
    ]
    validation = [PhoneNumber(nr).is_valid() for nr in numbers]
    validity = {True: 'valid', False: 'invalid'}
    for nr, valid in zip(numbers, validation):
        print("The phone number '{}' is {}.".format(nr, validity[valid]))

