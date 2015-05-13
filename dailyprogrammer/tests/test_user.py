#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_user.py

Unit tests for module :mod:`plugins.user` (source_).
"""

import os
import shutil
import unittest

import plugins.config as cfg
from plugins import user


class TestUser(unittest.TestCase):
    """Unit tests for class :func:`plugins.user.User`."""


    def setUp(self):
        """Setup before test.

        Create the directory for temporarily storing test input and output files (see
        :mod:`plugins.config`).
        """
        os.makedirs(cfg.tmp_dir, exist_ok=True)


    def tearDown(self):
        """Teardown after test.

        If it exists, recursively remove the directory for temporarily storing test input and output
        files (see :meth:`tests.test_user.TestUser.setUp`).
        """
        if os.path.isdir(cfg.tmp_dir):
            shutil.rmtree(cfg.tmp_dir)


    def test___init__(self):
        """Test method :meth:`plugins.user.User.__init__`

        **Tested:**

        - The attributes of a user are correct after initialization.
        """
        usr = user.User(
            name='John Smith',
            age=50,
            username='johnsmith',
            password='password',
        )
        self.assertEqual(usr.name, 'John Smith')
        self.assertEqual(usr.age, 50)
        self.assertEqual(usr.username, 'johnsmith')
        self.assertEqual(usr.password, 'password')


    def test___str__(self):
        """Test method :meth:`plugins.user.User.__str__`

        **Tested:**

        - The returned string is correct.
        """
        usr = user.User(
            name='John Smith',
            age=50,
            username='johnsmith',
            password='password',
        )
        result = usr.__str__()
        expected = [
            "Contents of User object:",
            "name: John Smith",
            "age: 50",
            "username: johnsmith",
            "password: password",
        ]
        self.assertTrue(all([part in result for part in expected]))


    def test___eq__(self):
        """Test method :meth:`plugins.user.User.__eq__`

        **Tested:**

        - True is returned when the two users have the same attributes and values.
        - False is returned when the two users have the same attributes but different values.
        - False is returned when the two users have different attributes, but the same values
          for the attributes that are the same.
        """
        user1 = user.User(name='John Smith', age=50, extra='extra_attribute')
        user2 = user.User(name='John Smith', age=50, extra='extra_attribute')
        user3 = user.User(name='John Smith', age=60, extra='extra_attribute')
        user4 = user.User(name='John Smith', age=50)
        user5 = user.User(name='John Smith', age=50, other='extra_attribute')
        self.assertTrue(user1==user2)
        self.assertFalse(user1==user3)
        self.assertFalse(user1==user4)
        self.assertFalse(user1==user5)


    def test_write(self):
        """Test method :meth:`plugins.user.User.write`

        **Tested:**

        - The contents of the generated file are correct.
        """
        usr = user.User(
            name='John Smith',
            age=50,
            username='johnsmith',
            password='password',
        )
        testfile_fn = os.path.join(cfg.tmp_dir, 'testoutput.txt')
        usr.write(testfile_fn)
        with open(testfile_fn, 'r') as testfile:
            result = testfile.read()
        expected = [
            "Contents of User object:",
            "name: John Smith",
            "age: 50",
            "username: johnsmith",
            "password: password",
        ]
        self.assertTrue(all([part in result for part in expected]))


class TestUserDatabase(unittest.TestCase):
    """Unit tests for class :func:`plugins.user.UserDatabase`."""


    def setUp(self):
        """Setup before test.

        Create the directory for temporarily storing test input and output files (see
        :mod:`plugins.config`).
        """
        os.makedirs(cfg.tmp_dir, exist_ok=True)


    def tearDown(self):
        """Teardown after test.

        If it exists, recursively remove the directory for temporarily storing test input and output
        files (see :meth:`tests.test_user.TestUserDatabase.setUp`).
        """
        if os.path.isdir(cfg.tmp_dir):
            shutil.rmtree(cfg.tmp_dir)


    def test___init__(self):
        """Test method :meth:`plugins.user.UserDatabase.__init__`

        **Tested:**

        - The amount of users in a user database is correct after initialization.
        - The users in a user database are correct after initialization.
        """
        userdb = user.UserDatabase(
            [
                user.User(username='un1', password='pw1'),
                user.User(username='un2', password='pw2'),
            ],
        )
        expected0 = user.User(username='un1', password='pw1')
        expected1 = user.User(username='un2', password='pw2')
        self.assertEqual(len(userdb.users), 2)
        self.assertEqual(userdb.users[0], expected0)
        self.assertEqual(userdb.users[1], expected1)


    def test___str__(self):
        """Test method :meth:`plugins.user.UserDatabase.__str__`

        **Tested:**

        - The returned string is correct.
        """
        userdb = user.UserDatabase(
            [
                user.User(username='un1', password='pw1'),
                user.User(username='un2', password='pw2'),
            ],
        )
        result = userdb.__str__()
        expected = '\n'.join([
            "User database:",
            "    Required user attributes: ['username', 'password']",
            "    Amount of users inside database: 2"
        ])
        self.assertEqual(result, expected)


    def test_set_required_attributes(self):
        """Test method :meth:`plugins.user.UserDatabase.set_required_attributes`

        **Tested:**

        - The required user attributes of a default user database are correct.
        - The required user attributes are correct after changing them to something else.
        """
        userdb = user.UserDatabase()
        self.assertEqual(userdb.attrs_req, ['username', 'password'])
        userdb.set_required_attributes(['req_attr1', 'req_attr2'])
        self.assertEqual(userdb.attrs_req, ['req_attr1', 'req_attr2'])


    def test_is_valid_user(self):
        """Test method :meth:`plugins.user.UserDatabase.is_valid_user`

        **Tested:**

        - False is returned when a non-user object is passed.
        - False is returned when an invalid user is passed.
        - True is returned when a valid user is passed.
        """
        userdb = user.UserDatabase()
        usr_invalid = user.User(name='name1', age=10)
        usr_valid = user.User(username='un1', password='pw1')

        self.assertFalse(userdb.is_valid_user(0))
        self.assertFalse(userdb.is_valid_user(usr_invalid))
        self.assertTrue(userdb.is_valid_user(usr_valid))


    def test_add_user(self):
        """Test method :meth:`plugins.user.UserDatabase.add_user`

        **Tested:**

        - The amount of users in the user database is correct before and after adding a user.
        - The last user in the user database is the one that was added.
        """
        userdb = user.UserDatabase(
            [
                user.User(username='un1', password='pw1'),
            ],
        )
        user_added = user.User(username='un2', password='pw2')
        expected = user.User(username='un2', password='pw2')

        self.assertEqual(len(userdb.users), 1)
        userdb.add_user(user_added)
        self.assertEqual(len(userdb.users), 2)
        self.assertEqual(userdb.users[-1], expected)


    def test_get_users(self):
        """Test method :meth:`plugins.user.UserDatabase.get_users`

        **Tested:**

        - If there are matches, the returned list of users is correct.
        - If there are no matches, the returned list is empty.
        """
        userdb = user.UserDatabase(
            [
                user.User(username='un1', password='pw1'),
                user.User(username='un1', password='pw2'),
                user.User(username='un2', password='pw2'),
            ],
        )
        expected1 = [
            user.User(username='un1', password='pw1'),
            user.User(username='un1', password='pw2'),
        ]
        expected2 = [
            user.User(username='un1', password='pw2'),
            user.User(username='un2', password='pw2'),
        ]
        self.assertEqual(userdb.get_users('username', 'un1'), expected1)
        self.assertEqual(userdb.get_users('password', 'pw2'), expected2)
        self.assertEqual(userdb.get_users('username', 'un3'), [])
        self.assertEqual(userdb.get_users('invalid_attr', 'val'), [])


    def test_write(self):
        """Test method :meth:`plugins.user.UserDatabase.write`

        **Tested:**

        - The contents of the generated file are correct.
        """
        userdb = user.UserDatabase(
            [
                user.User(username='un1', password='pw1'),
                user.User(username='un2', password='pw2'),
            ],
        )
        userdb_fn = os.path.join(cfg.tmp_dir, 'testuserdb.txt')
        userdb.write(userdb_fn)
        with open(userdb_fn, 'r') as userdb_fil:
            result = userdb_fil.read()
        expected = [
            "username;password",
            "un1;pw1",
            "un2;pw2",
        ]
        self.assertTrue(all([part in result for part in expected]))


    def test_read(self):
        """Test classmethod :meth:`plugins.user.UserDatabase.read`

        **Tested:**

        - The returned object is a UserDatabase object.
        - The contents of the returned user database are correct.
        """
        userdb_fn = os.path.join(cfg.tmp_dir, 'testuserdb.txt')
        contents1 = '\n'.join([
            "username;password",
            "un1;pw1",
            "un2;pw2",
        ]) + '\n'

        # Test reading of file that does not exist.
        userdb = user.UserDatabase.read(userdb_fn)
        self.assertEqual(userdb.users, [])

        # Test reading of correct file.
        with open(userdb_fn, 'w') as userdb_fil:
            userdb_fil.write(contents1)
        expected0 = user.User(username='un1', password='pw1')
        expected1 = user.User(username='un2', password='pw2')

        userdb = user.UserDatabase.read(userdb_fn)
        self.assertTrue(isinstance(userdb, user.UserDatabase))
        self.assertEqual(len(userdb.users), 2)
        self.assertEqual(userdb.users[0], expected0)
        self.assertEqual(userdb.users[1], expected1)


if __name__ == '__main__':
    unittest.main()
