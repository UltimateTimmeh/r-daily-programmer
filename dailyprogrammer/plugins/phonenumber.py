#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/phonenumber.py

Store, validate and manage telephone numbers (source_).

.. _plugins.phonenumber.valid_formats:

| *var* plugins.phonenumber.\ **valid_formats** *(dict(str: list(str, ...), ...))*
|     dictionary mapping countries to their respective list of valid phone number formats

| *var* plugins.phonenumber.\ **map_l2n** *(dict(str: str, ...))*
|     dictionary mapping letters to their equivalent number on a telephone keypad
"""

valid_formats = {
    'US': [
        ## No area code (7 digits).
        'xxxxxxx',
        'xxx-xxxx',
        'xxx.xxxx',
        'xxx xxxx',
        ## With area code (10 digits).
        'xxxxxxxxxx',
        'xxx-xxx-xxxx',
        'xxx.xxx.xxxx',
        'xxx xxx xxxx',
        '(xxx)xxxxxxx',
        '(xxx)xxx-xxxx',
        '(xxx)xxx.xxxx',
        '(xxx)xxx xxxx',
        '(xxx) xxxxxxx',
        '(xxx) xxx-xxxx',
        '(xxx) xxx.xxxx',
        '(xxx) xxx xxxx',
        ## With single-digit country code (11 digits).
        'x-xxx-xxxxxxx',
        'x.xxx.xxxxxxx',
        'x xxx xxxxxxx',
        'x-xxx-xxx-xxxx',
        'x.xxx.xxx.xxxx',
        'x xxx xxx xxxx',
    ]
}

map_l2n = {l: n for l, n in zip(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '22233344455566677778889999'
)}


class PhoneNumber(object):
    """A class representing a phone number.

    A phone number is characterized by an entered value (which can be a string containing anything),
    and the country in which the phone number should be valid before anything can be done with it.

    :param str entered: the phone number as it is entered by the user
    :param str country: the country in which the phone number should be validated (default 'US')

    Example::

        >>> nr = PhoneNumber('123-45-7890')
        >>> nr.format()
        'xxx-xx-xxxx'
        >>> nr.is_valid()
        False
        >>> PhoneNumber('123-456-7890').is_valid()
        True
    """


    def __init__(self, entered, country='US'):
        """Create a new phone number."""
        self.entered = entered.upper()
        self.country = country.upper()


    def raw(self):
        """Return the raw version of the phone number.

        The raw version of a phone number is the defined as the number, as it is entered by the
        user, with all letters replaced by their respective number on a telephone keypad.

        :return: the raw version of the phone number
        :rtype: str

        Example::

            >>> nr = PhoneNumber('1-800-VERIZON')
            >>> nr.raw()
            1-800-8374966
        """
        raw = self.entered
        for ltr, nr in map_l2n.items():
            raw = raw.replace(ltr, nr)
        return raw


    def format(self):
        """Return the format of the phone number.

        The format of a phone number is defined as the number, as it is entered by the user, with
        all numbers replaced by the character 'x'.

        :return: the format of the phone number
        :rtype: str

        For an example that uses this method, see :func:`plugins.phonenumber.PhoneNumber`.
        """
        format = self.raw()
        for nr in '0123456789':
            format = format.replace(nr, 'x')
        return format


    def is_valid(self):
        """Check if the phone number is valid.

        A number is considered to be valid if its format is in the specified country's list of valid
        phone number formats (see plugins.phonenumber.valid_formats_).

        :return: True if the phone number is valid, False otherwise
        :rtype: bool

        For an example that uses this method, see :func:`plugins.phonenumber.PhoneNumber`.
        """
        if self.format() not in valid_formats[self.country]:
            return False
        return True


    def transform_to_format(self, format):
        """Transform a phone number to the desired format.

        :return: the phone number, transformed to the desired format
        :rtype: str
        :raise: ValueError if there is a mismatch between the length of the phone number and the
                length of the desired format

        Example::

            >>> nr = PhoneNumber('1-800-VERIZON')
            >>> nr.transform_to_format('x-xxx-xxx-xxxx')
            1-800-837-4966
        """
        indices = [ind for ind, char in enumerate(format) if char == 'x']
        raw_nr = [nr for nr in self.raw() if nr in '0123456789']
        if len(raw_nr) != len(indices):
            raise ValueError("Mismatch between length of number and desired format.")
        transformed = [char for char in format]
        for ind, nr in zip(indices, raw_nr):
            transformed[ind] = nr
        return ''.join(transformed)

