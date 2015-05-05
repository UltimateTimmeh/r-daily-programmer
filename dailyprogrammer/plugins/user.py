#!/usr/bin/python3
"""
Storing and handling a user's information
"""


class User(object):
    """A class for storing and handling a user's information."""


    def __init__(self, name, age, **kwargs):
        """Initialize the user object."""
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        """Format a string representation of the user."""
        _str = [
            "Personal information of {name} ({age} years old):".format(**self.__dict__)
            ]
        _str += ["    {}: {}".format(key, value) for key, value in self.__dict__.items()]
        return '\n'.join(_str)


    def write(self, fn, mode='a'):
        """Write the user's information to file *fn*."""
        with open(fn, mode) as output_file:
            output_file.write(str(self)+'\n')
