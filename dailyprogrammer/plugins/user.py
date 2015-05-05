#!/usr/bin/python3
"""
Storing and handling a user's information
"""

import os


class User(object):
    """A class for storing and handling a user's information."""


    def __init__(self, name, age, **kwargs):
        """Initialize the User object."""
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


    def __eq__(self, other):
        """Test if User object `self` is equal to User object `other`."""
        return isinstance(other, self.__class__) \
            and self.__dict__ == other.__dict__


    def write(self, fn, mode='a'):
        """Write the user's information to file `fn`."""
        with open(fn, mode) as output_file:
            output_file.write(str(self)+'\n')


class UserDatabase(object):
    """A class for managing a collection of users."""

    attrs_extra = ['username', 'password']


    def __init__(self, users):
        """Initialize the UserDatabase object."""
        if not all([UserDatabase.is_valid_user(user) for user in users]):
            raise ValueError("Invalid users for UserDatabase initialization!")
        self.users = users


    def add_user(self, user):
        """Add `user` to the UserDatabase."""
        if not UserDatabase.is_valid_user(user):
            raise ValueError("Invalid user for UserDatabase!")
        self.users.append(user)


    def get_users(self, attr, val):
        """Return the list of users that have `val` as the value for attribute `attr`."""
        match = []
        for user in self.users:
            if attr in user.__dict__ and getattr(user, attr) == val:
                match.append(user)
        return match


    def write(self, fn):
        """Write the contents of the UserDatabase object to file `fn`."""
        attrs_all = UserDatabase.attrs_extra + ['name', 'age']
        header = [';'.join(attrs_all)]
        data = [
            ';'.join([str(getattr(user, attr)) for attr in attrs_all]) \
                for user in self.users
        ]
        fil_contents = header + data
        with open(fn, 'w') as fil:
            fil.write('\n'.join(fil_contents) + '\n')


    @classmethod
    def read(cls, fn):
        """Load the contents of user database file `fn`."""
        # Read file contents (if file exists).
        if not os.path.isfile(fn):
            return cls([])
        with open(fn, 'r') as fil:
            fil_contents = fil.readlines()

        # Check header.
        attrs_all = UserDatabase.attrs_extra + ['name', 'age']
        header = fil_contents[0].strip().split(';')
        if not all([aa==ah for aa, ah in zip(attrs_all, header)]):
            raise ValueError("File does not contain correct header data!")

        # Process data.
        data = [line.strip().split(';') for line in fil_contents[1:]]
        users = []
        for item in data:
            if not len(item) == len(attrs_all):
                raise ValueError("Invalid dataline in user database file!")
            name = item[-2]
            age = int(item[-1])
            kwargs = {attr: val for attr, val in zip(UserDatabase.attrs_extra, item[:-2])}
            user = User(name, age, **kwargs)
            users.append(user)
        return cls(users)


    @staticmethod
    def is_valid_user(user):
        """Check if `user` is a valid entry for the UserDatabase object."""
        return isinstance(user, User) \
            and all([attr in user.__dict__ for attr in UserDatabase.attrs_extra])
