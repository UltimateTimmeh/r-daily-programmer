#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/phonenumber.py

Store, validate and manage telephone numbers (source_).

.. _plugins.phonenumber.valid_formats:

| *var* plugins.phonenumber.\ **valid_formats** *(dict(str: list(str, ...), ...))*
|     dictionary mapping countries to their respective list of valid phone number formats
"""

valid_formats = {
    'US': [
        'xxxxxxx',
        'xxx-xxxx',
        'xxx.xxxx',
        'xxx xxxx',
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
    ]
}


class PhoneNumber(object):
    """A class representing a phone number.

    A phone number is characterized by an entered value (which can be a string containing anything),
    and the country in which the phone number should be valid before anything can be done with it.

    :param str entered: the phone number as it is entered by the user
    :param str country: the country in which the phone number should be validated (default 'US')

    Example::

        >>> from phonenumber import PhoneNumber
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


    def format(self):
        """Return the format of the phone number.

        The format of a phone number is defined as the number, as it is entered by the user, with
        all numbers replaced by the character 'x'.

        :return: the format of the phone number
        :rtype: str

        For an example that uses this method, see :func:`plugins.phonenumber.PhoneNumber`.
        """
        format = self.entered
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

