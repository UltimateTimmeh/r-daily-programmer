#!/usr/bin/python3
"""
Module with enhanced string class, supposed to be an expansion of the
default str class with several methods that are potentially useful to
have for strings.
"""


class EnhancedString(object):
    """Enhanced string object containing useful methods for strings."""


    def __init__(self, _str):
        """Initiate EnhancedString object."""
        self._str = _str


    def __str__(self):
        """Format self as string."""
        return self._str


    def remove(self, chars):
        """Remove all instances of each character in chars from self."""
        for char in chars:
            self._str = self._str.replace(char, '')
