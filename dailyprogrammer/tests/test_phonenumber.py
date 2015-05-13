#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_phonenumber.py

Unit tests for module :mod:`plugins.phonenumber` (source_).
"""

import unittest

from plugins import phonenumber


class TestPhoneNumber(unittest.TestCase):
    """Unit tests for class :func:`plugins.phonenumber.PhoneNumber`."""


    def test___init__(self):
        """Test method :meth:`plugins.phonenumber.PhoneNumber.__init__`

        **Tested:**

        - The attributes of a phone number are correct after initialization.
        """
        nr = phonenumber.PhoneNumber('123-456-7890')
        self.assertEqual(nr.entered, '123-456-7890')
        self.assertEqual(nr.country, 'US')


    def test_format(self):
        """Test method :meth:`plugins.phonenumber.PhoneNumber.format`

        **Tested:**

        - The returned phone number format is correct.
        """
        nr = phonenumber.PhoneNumber('(123) 456.7890')
        self.assertEqual(nr.format(), '(xxx) xxx.xxxx')


    def test_is_valid(self):
        """Test method :meth:`plugins.phonenumber.PhoneNumber.is_valid`

        **Tested:**

        - The returned boolean correctly indicates a phone number's validity.
        """
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
        result = [phonenumber.PhoneNumber(nr).is_valid() for nr in numbers]
        expected = [True]*6 + [False]*3
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
