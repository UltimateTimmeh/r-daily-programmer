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


if __name__ == '__main__':
    unittest.main()
