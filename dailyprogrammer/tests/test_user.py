#!/usr/bin/python3
"""
Unit tests for plugin personalinfo
"""

import os
import shutil
import unittest

import plugins.config as cfg
from plugins import user


class TestUser(unittest.TestCase):
    """Unit tests for class user.User"""


    def setUp(self):
        """Set up before test"""
        os.makedirs(cfg.tmp_dir, exist_ok=True)


    def tearDown(self):
        """Tear down after test"""
        if os.path.isdir(cfg.tmp_dir):
            shutil.rmtree(cfg.tmp_dir)


    def test___init__(self):
        """Test method user.User.__init__"""
        usr = user.User(
            'John Smith',
            50,
            reddit_username='John_Smith',
            personal_attribute='personal_value',
        )
        self.assertEqual(usr.name, 'John Smith')
        self.assertEqual(usr.age, 50)
        self.assertEqual(usr.reddit_username, 'John_Smith')
        self.assertEqual(usr.personal_attribute, 'personal_value')


    def test___str__(self):
        """Test method user.User.__str__"""
        usr = user.User(
            'John Smith',
            50,
            reddit_username='John_Smith',
            personal_attribute='personal_value',
        )
        result = usr.__str__()
        expected = [
            "Personal information of John Smith (50 years old):",
            "name: John Smith",
            "age: 50",
            "reddit_username: John_Smith",
        ]
        self.assertTrue(all([part in result for part in expected]))


    def test___eq__(self):
        """Test method user.User.__eq__"""
        user1 = user.User('John Smith', 50, extra='extra_attribute')
        user2 = user.User('John Smith', 50, extra='extra_attribute')
        user3 = user.User('John Smith', 60, extra='extra_attribute')
        user4 = user.User('John Smith', 50)
        user5 = user.User('John Smith', 50, other='extra_attribute')
        self.assertTrue(user1==user2)
        self.assertFalse(user1==user3)
        self.assertFalse(user1==user4)
        self.assertFalse(user1==user5)


    def test_write(self):
        """Test method user.User.write"""
        usr = user.User(
            'John Smith',
            50,
            reddit_username='John_Smith',
            personal_attribute='personal_value',
        )
        testfile_fn = os.path.join(cfg.tmp_dir, 'testoutput.txt')
        usr.write(testfile_fn)
        with open(testfile_fn, 'r') as testfile:
            result = testfile.read()
        expected = [
            "Personal information of John Smith (50 years old):",
            "name: John Smith",
            "age: 50",
            "reddit_username: John_Smith",
        ]
        self.assertTrue(all([part in result for part in expected]))


class TestUserDatabase(unittest.TestCase):
    """Unit tests for class user.UserDatabase"""


    def setUp(self):
        """Set up before test"""
        os.makedirs(cfg.tmp_dir, exist_ok=True)


    def tearDown(self):
        """Tear down after test"""
        if os.path.isdir(cfg.tmp_dir):
            shutil.rmtree(cfg.tmp_dir)


    def test___init__(self):
        """Test method user.UserDatabase.__init__"""
        userdb = user.UserDatabase(
            [
                user.User('name1', 10, username='un1', password='pw1'),
                user.User('name2', 20, username='un2', password='pw2'),
            ],
        )
        expected0 = user.User('name1', 10, username='un1', password='pw1')
        expected1 = user.User('name2', 20, username='un2', password='pw2')
        self.assertEqual(len(userdb.users), 2)
        self.assertEqual(userdb.users[0], expected0)
        self.assertEqual(userdb.users[1], expected1)


    def test_add_user(self):
        """Test method user.UserDatabase.add_user"""
        userdb = user.UserDatabase(
            [
                user.User('name1', 10, username='un1', password='pw1'),
            ],
        )
        user_added = user.User('name2', 20, username='un2', password='pw2')

        self.assertEqual(len(userdb.users), 1)
        userdb.add_user(user_added)
        self.assertEqual(len(userdb.users), 2)
        expected1 = user.User('name2', 20, username='un2', password='pw2')
        self.assertEqual(userdb.users[1], expected1)


    def test_get_users(self):
        """Test method user.UserDatabase.get_users"""
        userdb = user.UserDatabase(
            [
                user.User('name1', 10, username='un1', password='pw'),
                user.User('name1', 20, username='un2', password='pw'),
                user.User('name2', 20, username='un1', password='pw'),
            ],
        )
        expected1 = [
            user.User('name1', 10, username='un1', password='pw'),
            user.User('name1', 20, username='un2', password='pw'),
        ]
        expected2 = [
            user.User('name1', 20, username='un2', password='pw'),
            user.User('name2', 20, username='un1', password='pw'),
        ]
        expected3 = [
            user.User('name1', 10, username='un1', password='pw'),
            user.User('name2', 20, username='un1', password='pw'),
        ]
        self.assertEqual(userdb.get_users('name', 'name1'), expected1)
        self.assertEqual(userdb.get_users('age', 20), expected2)
        self.assertEqual(userdb.get_users('username', 'un1'), expected3)
        self.assertEqual(userdb.get_users('name', 'name3'), [])
        self.assertEqual(userdb.get_users('username', 'un3'), [])
        self.assertEqual(userdb.get_users('invalid_attr', 'val'), [])


    def test_write(self):
        """Test method user.UserDatabase.write"""
        userdb = user.UserDatabase(
            [
                user.User('name1', 10, username='un1', password='pw1'),
                user.User('name2', 20, username='un2', password='pw2'),
            ],
        )
        userdb_fn = os.path.join(cfg.tmp_dir, 'testuserdb.txt')
        userdb.write(userdb_fn)
        with open(userdb_fn, 'r') as userdb_fil:
            result = userdb_fil.read()
        expected = [
            "username;password;name;age",
            "un1;pw1;name1;10",
            "un2;pw2;name2;20",
        ]
        self.assertTrue(all([part in result for part in expected]))


    def test_read(self):
        """Test classmethod user.UserDatabase.read"""
        userdb_fn = os.path.join(cfg.tmp_dir, 'testuserdb.txt')
        contents1 = "invalid_header\n"
        contents2 = '\n'.join([
            "username;password;name;age",
            "un1;pw1;name1;10",
            "un2;pw2;name2;20",
        ]) + '\n'

        # Test reading of file that does not exist.
        userdb = user.UserDatabase.read(userdb_fn)
        self.assertEqual(userdb.users, [])

        # Test reading of file with incorrect header.
        with open(userdb_fn, 'w') as userdb_fil:
            userdb_fil.write(contents1)
        with self.assertRaises(ValueError):
            user.UserDatabase.read(userdb_fn)

        # Test reading of correct file.
        with open(userdb_fn, 'w') as userdb_fil:
            userdb_fil.write(contents2)
        expected0 = user.User('name1', 10, username='un1', password='pw1')
        expected1 = user.User('name2', 20, username='un2', password='pw2')

        userdb = user.UserDatabase.read(userdb_fn)
        self.assertTrue(isinstance(userdb, user.UserDatabase))
        self.assertEqual(len(userdb.users), 2)
        self.assertEqual(userdb.users[0], expected0)
        self.assertEqual(userdb.users[1], expected1)


    def test_is_valid_user(self):
        """Test staticmethod user.UserDatabase.check_user"""
        usr_invalid = user.User('name1', 10)
        usr_valid = user.User('name1', 10, username='un1', password='pw1')

        self.assertFalse(user.UserDatabase.is_valid_user(0))
        self.assertFalse(user.UserDatabase.is_valid_user(usr_invalid))
        self.assertTrue(user.UserDatabase.is_valid_user(usr_valid))


if __name__ == '__main__':
    unittest.main()
