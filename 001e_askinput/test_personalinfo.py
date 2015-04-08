#!/usr/bin/python3
"""
Unit tests for module personalinfo.py
"""

import os
import unittest

import personalinfo


class TestPersonalInfo(unittest.TestCase):


    def setUp(self):
        """Set up before test"""
        self.pi = personalinfo.PersonalInfo('John Smith', 50, 'John_Smith')
        self.pi_str = (
            "Your name is 'John Smith', you are 50 years " +
            "old and your Reddit username is 'John_Smith'."
            )
        self.testfile_fn = 'testoutput.txt'


    def tearDown(self):
        """Tear down after test"""
        # Delete test files.
        if os.path.isfile(self.testfile_fn):
            os.remove(self.testfile_fn)

        # Delete test attributes.
        attr_to_del = [
            'pi',
            'pi_str',
            'testfile_fn',
            ]
        for attr in attr_to_del:
            delattr(self, attr)


    def test___init__(self):
        """Test method personalinfo.PersonalInfo.__init__"""
        self.assertEqual(self.pi.name, 'John Smith')
        self.assertEqual(self.pi.age, 50)
        self.assertEqual(self.pi.reddit_username, 'John_Smith')


    def test___str__(self):
        """Test method personalinfo.PersonalInfo.__str__"""
        self.assertEqual(self.pi.__str__(), self.pi_str)


    def test_write(self):
        """Test method personalinfo.PersonalInfo.write"""
        self.pi.write(self.testfile_fn)
        with open(self.testfile_fn, 'r') as testfile:
            testline = testfile.readlines()[0]
        self.assertEqual(testline, self.pi_str+'\n')


if __name__ == '__main__':
    unittest.main()
