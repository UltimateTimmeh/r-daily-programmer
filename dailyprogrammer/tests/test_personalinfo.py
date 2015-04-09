#!/usr/bin/python3
"""
Unit tests for module personalinfo.py
"""

import os
import shutil
import unittest

import plugins.config as cfg
from plugins.personalinfo import PersonalInfo


class TestPersonalInfo(unittest.TestCase):


    def setUp(self):
        """Set up before test"""
        self.pi = PersonalInfo('John Smith', 50, reddit_username='John_Smith')
        self.pi_str_expected = [
            "Personal information of John Smith (50 years old):",
            "name: John Smith",
            "age: 50",
            "reddit_username: John_Smith",
            ]
        os.makedirs(cfg.tmp_dir, exist_ok=True)
        self.testfile_fn = os.path.join(cfg.tmp_dir, 'testoutput.txt')


    def tearDown(self):
        """Tear down after test"""
        # Delete test files.
        if os.path.isdir(cfg.tmp_dir):
            shutil.rmtree(cfg.tmp_dir)

        # Delete test attributes.
        attr_to_del = [
            'pi',
            'pi_str_expected',
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
        received = self.pi.__str__()
        self.assertTrue(all([expected in received for expected in self.pi_str_expected]))


    def test_write(self):
        """Test method personalinfo.PersonalInfo.write"""
        self.pi.write(self.testfile_fn)
        with open(self.testfile_fn, 'r') as testfile:
            received = testfile.read()
        self.assertTrue(all([expected in received for expected in self.pi_str_expected]))


if __name__ == '__main__':
    unittest.main()
