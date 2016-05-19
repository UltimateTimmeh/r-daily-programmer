#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/user.py

Storing and handling a user's information (source_).
"""

import os


class User(object):
    """A class for collecting all information about a user.

    A user is a very general object which has no default attributes. However, all keyword
    arguments that are passed to it during its creation will be set as attributes. Equality
    of user objects is also implemented. Two users are equal if their attribute dictionaries
    are equal.

    :param dict \*\*kwargs: keyword arguments that will be set as attributes of the user

    Example::

        >>> name = 'John Smith'
        >>> info = {'age': 50, 'username': 'johnsmith'}
        >>> usr1 = User(name=name, **info)
        >>> usr1.name
        'John Smith'
        >>> usr1.age
        50
        >>> usr1.username
        'johnsmith'
        >>> print(usr1)
        Contents of User object:
            username: johnsmith
            name: John Smith
            age: 50
        >>> usr2 = User(name='Jane Smith', age=50)
        >>> usr3 = User(name='Jane Smith', age=50)
        >>> usr1 == usr2
        False
        >>> usr2 == usr3
        True
    """


    def __init__(self, **kwargs):
        """Create a new user."""
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        """Format a user as a string."""
        _str = ["Contents of User object:"]
        _str += ["    {}: {}".format(key, value) for key, value in self.__dict__.items()]
        return '\n'.join(_str)


    def __eq__(self, other):
        """Test equality between a user and another object.

        :param object other: the object with which the user is compared
        :return: True if the other object is the same as the user, False otherwise
        :rtype: bool
        """
        return isinstance(other, self.__class__) \
            and self.__dict__ == other.__dict__


    def write(self, fn, mode='a'):
        """Write all attributes of a user to a file.

        :param str fn: path to the file in which the user's attributes will be written
        :param str mode: how the file is to be opened, all modes that allow writing are
                         accepted (default 'a')

        Example::

            >>> usr = User(name='John Smith', age=50, username='johnsmith')
            >>> usr.write('output.txt')
            >>> with open('output.txt', 'r') as fil: print(fil.read())
            ...
            Contents of User object:
                name: John Smith
                username: johnsmith
                age: 50
        """
        with open(fn, mode) as output_file:
            output_file.write(str(self)+'\n')


class UserDatabase(object):
    """A class for managing a collection of users.

    A user database contains a list of users that are all required to have at least
    certain attributes. A user database can be searched for users that have a
    specific value for a specific attribute and can be written to or read from a
    file. A default user database is empty and has the required attributes 'username'
    and 'password'.

    :param users: a list of initial users to put in the database (default [])
    :type users: list(User, ...)
    :param attrib: the list of required user attributes (default ['username', 'password'])
    :type attrib: list(str, ...)
    :raise: ValueError if the initial list of users contains invalid objects

    Example::

        >>> usr1 = User(username='johnsmith', password='password')
        >>> usr2 = User(username='janesmith', password='possward')
        >>> userdb = UserDatabase([usr1, usr2])
        >>> print(userdb)
        User database:
            Required user attributes: ['username', 'password']
            Amount of users inside database: 2
        >>> print(userdb.users[0])
        Contents of User object:
            username: johnsmith
            password: password
    """


    def __init__(self, users=None, attrs_req=None):
        """Create a new user database."""
        if users is None:
            users = []
        if attrs_req is None:
            attrs_req = ['username', 'password']
        self.attrs_req = attrs_req
        if not all([self.is_valid_user(user) for user in users]):
            raise ValueError("Invalid users for UserDatabase initialization!")
        self.users = users


    def __str__(self):
        """Format a user database as a string."""
        _str = ['User database:']
        _str += ['    Required user attributes: {}'.format(self.attrs_req)]
        _str += ['    Amount of users inside database: {}'.format(len(self.users))]
        return '\n'.join(_str)


    def set_required_attributes(self, attrs_req):
        """Set the required user attributes.

        .. warning:: To Add: After changing the required attributes, remove users from database that
                     are no longer valid.

        :param attrs_req: the new list of required user attributes
        :type attrs_req: list(str, ...)

        Example::

            >>> userdb = UserDatabase()
            >>> print(userdb)
            User database:
                Required user attributes: ['username', 'password']
                Amount of users inside database: 0
            >>> userdb.set_required_attributes(['name', 'age'])
            >>> print(userdb)
            User database:
                Required user attributes: ['name', 'age']
                Amount of users inside database: 0
        """
        self.attrs_req = attrs_req


    def is_valid_user(self, user):
        """Check if a user is valid for the user database.

        A user is valid if it has at least the required attributes.

        :param User user: the user that is validated
        :return: True if the user is valid, False otherwise
        :rtype: bool

        Example::

            >>> usr1 = User(name='John Smith', age=50, username='johnsmith')
            >>> usr2 = User(name='Jane Smith', username='janesmith', password='possward')
            >>> userdb = UserDatabase()
            >>> userdb.is_valid_user(usr1)
            False
            >>> userdb.is_valid_user(usr2)
            True
        """
        return isinstance(user, User) \
            and all([attr in user.__dict__ for attr in self.attrs_req])


    def add_user(self, user):
        """Add a user to the user database.

        :param User user: the user that is added
        :raise: ValueError if the user is invalid

        Example::

            >>> userdb = UserDatabase()
            >>> print(userdb)
            User database:
                Required user attributes: ['username', 'password']
                Amount of users inside database: 0
            >>> usr = User(username='johnsmith', password='password')
            >>> userdb.add_user(usr)
            >>> print(userdb)
            User database:
                Required user attributes: ['username, 'password']
                Amount of users inside database: 1
        """
        if not self.is_valid_user(user):
            raise ValueError("Invalid user for UserDatabase!")
        self.users.append(user)


    def get_users(self, attr, val):
        """Return the subset of users that have a certain value for a certain attribute.

        :param str attr: user attribute to check
        :param object val: required value of the user attribute
        :return: list of users that have the specified value for the specified attribute
        :rtype: list(User, ...)

        Example::

            >>> usr1 = User(username='johnsmith', password='secret1')
            >>> usr2 = User(username='janesmith', password='secret2')
            >>> usr3 = User(username='jeansmith', password='secret1')
            >>> userdb = UserDatabase([usr1, usr2, usr3])
            >>> match = userdb.get_users('password', 'secret1')
            >>> for usr in match: print(usr.username)
            ...
            johnsmith
            jeansmith
        """
        match = []
        for user in self.users:
            if attr in user.__dict__ and getattr(user, attr) == val:
                match.append(user)
        return match


    def write(self, fn):
        """Write the contents of the user database to a file.

        The first line of the file lists the user database's required attributes. Each
        subsequent line lists the value of those attributes for the users in the database.
        Values in a line are separated by the semicolon (';').

        .. warning:: The file is opened in write mode ('w'), meaning it will overwrite any existing
                     file with the same name!

        :param str fn: path to the file in which the user database's contents will be written

        Example::

            >>> usr = User(username='johnsmith', password='secret')
            >>> userdb = UserDatabase([usr])
            >>> userdb.write('output.txt')
            >>> with open('output.txt', 'r') as fil: print(fil.read())
            ...
            username;password
            johnsmith;secret

            >>> userdb_new = UserDatabase.read('output.txt')
            >>> print(userdb_new)
            User database:
                Required user attributes: ['username', 'password']
                Amount of users inside database: 1
            >>> print(userdb_new.users[0])
            Contents of User object:
                password: secret
                username: johnsmith
        """
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
        """Read the contents of a user database file.

        For more information about the formatting of the contents of a user database file, see
        :meth:`plugins.user.UserDatabase.write`. If the specified file does not exist, an empty
        user database is returned.

        :param str fn: path to the file that is read
        :return: a user database with contents as specified in the user database file
                 or an empty user database if the specified file does not exist
        :rtype: UserDatabase

        For an example that uses this classmethod, see :meth:`plugins.user.UserDatabase.write`.
        """
        # Read file contents (if file exists).
        if not os.path.isfile(fn):
            return cls()
        with open(fn, 'r') as fil:
            fil_contents = fil.readlines()

        # Process header, which should contain the required user attributes.
        attrs_req = fil_contents[0].strip().split(';')

        # Process user lines.
        userlines = [line.strip().split(';') for line in fil_contents[1:]]
        users = []
        for userline in userlines:
            kwargs = {attr: val for attr, val in zip(attrs_req, userline)}
            user = User(**kwargs)
            users.append(user)
        return cls(users, attrs_req)

