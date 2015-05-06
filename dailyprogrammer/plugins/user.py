#!/usr/bin/python3
"""
Storing and handling a user's information
"""

import os


class User(object):
    """A class for storing and handling a user's information."""


    def __init__(self, **kwargs):
        """Initialize the User object."""
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        """Format a string representation of the User object."""
        _str = ["Contents of User object:"]
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

    def __init__(self, users=[], attrs_req=['username', 'password']):
        """Initialize the UserDatabase object."""
        self.attrs_req = attrs_req
        if not all([self.is_valid_user(user) for user in users]):
            raise ValueError("Invalid users for UserDatabase initialization!")
        self.users = users


    def set_required_attributes(self, attrs_req):
        """Set the required attributes users in the user database should have."""
        self.attrs_req = attrs_req


    def is_valid_user(self, user):
        """Check if `user` is a valid entry for the UserDatabase object."""
        return isinstance(user, User) \
            and all([attr in user.__dict__ for attr in self.attrs_req])


    def add_user(self, user):
        """Add `user` to the UserDatabase."""
        if not self.is_valid_user(user):
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
        header = [';'.join(self.attrs_req)]
        data = [
            ';'.join([str(getattr(user, attr)) for attr in self.attrs_req]) \
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
            return cls()
        with open(fn, 'r') as fil:
            fil_contents = fil.readlines()

        # Load header, which should be the required user attributes.
        header = fil_contents[0].strip().split(';')

        # Process data.
        data = [line.strip().split(';') for line in fil_contents[1:]]
        users = []
        for item in data:
            if not len(item) == len(header):
                raise ValueError("Invalid dataline in user database file!")
            kwargs = {attr: val for attr, val in zip(header, item)}
            user = User(**kwargs)
            users.append(user)
        return cls(users, attrs_req=header)
