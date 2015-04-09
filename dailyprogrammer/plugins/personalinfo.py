#!/usr/bin/python3
"""
Storing and handling personal information
"""


class PersonalInfo(object):
    """A class for storing and handling personal information."""


    def __init__(self, name, age, **kwargs):
        """Initialize the personal information object."""
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        """Format a string representation of the personal information."""
        _str = [
            "Personal information of {name} ({age} years old):".format(**self.__dict__)
            ]
        _str += ["    {}: {}".format(key, value) for key, value in self.__dict__.items()]
        return '\n'.join(_str)


    def write(self, fn, mode='a'):
        """Write the personal information to file *fn*."""
        with open(fn, mode) as output_file:
            output_file.write(str(self)+'\n')
