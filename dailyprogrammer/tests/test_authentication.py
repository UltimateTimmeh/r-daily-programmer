#!/usr/bin/python3
"""
Unit tests for plugin authentication
"""

import unittest
import random

from plugins import authentication


class TestAuthentication(unittest.TestCase):
    """Unit tests for functions in plugin authentication"""


    def setUp(self):
        """Set up before test"""
        pass


    def tearDown(self):
        """Tear down after test"""
        pass


    def test_random_password(self):
        """Test function authentication.random_password"""
        # Test default password length.
        expected = 8
        result = len(authentication.random_password())
        self.assertEqual(result, expected)

        # Test arbitrary password length.
        expected = random.randint(10, 20)
        result = len(authentication.random_password(l=expected))
        self.assertEqual(result, expected)


    def test_hash_password(self):
        """Test function authentication.hash_password"""
        password = 'password'
        salt = '2b1d50bb859e4474a3ca5de7c87bfa82'
        expected = '608c111b63d4b98858849a1b44d46f88056b22a409bed7250269e03ff28ccdbc'
        expected += ':2b1d50bb859e4474a3ca5de7c87bfa82'
        self.assertEqual(authentication.hash_password(password, salt), expected)


    def test_validate_password(self):
        """Test function authentication.validate_password"""
        password_correct = 'password'
        password_incorrect = 'passwrd'
        password_hashed = '608c111b63d4b98858849a1b44d46f88056b22a409bed7250269e03ff28ccdbc'
        password_hashed += ':2b1d50bb859e4474a3ca5de7c87bfa82'

        self.assertFalse(authentication.validate_password(password_incorrect, password_hashed))
        self.assertTrue(authentication.validate_password(password_correct, password_hashed))


if __name__ == '__main__':
    unittest.main()
