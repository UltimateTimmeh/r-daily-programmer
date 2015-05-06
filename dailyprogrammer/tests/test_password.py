#!/usr/bin/python3
"""
Unit tests for plugin password
"""

import unittest
import random

from plugins import password


class TestPassword(unittest.TestCase):
    """Unit tests for functions in plugin password"""


    def test_random_password(self):
        """Test function password.random_password"""
        # Test default password length.
        expected = 8
        result = len(password.random_password())
        self.assertEqual(result, expected)

        # Test random password length.
        expected = random.randint(10, 20)
        result = len(password.random_password(l=expected))
        self.assertEqual(result, expected)


    def test_hash_password(self):
        """Test function password.hash_password"""
        pwd = 'password'
        salt = '2b1d50bb859e4474a3ca5de7c87bfa82'
        expected = '608c111b63d4b98858849a1b44d46f88056b22a409bed7250269e03ff28ccdbc'
        expected += ':2b1d50bb859e4474a3ca5de7c87bfa82'
        self.assertEqual(password.hash_password(pwd, salt), expected)


    def test_validate_password(self):
        """Test function password.validate_password"""
        pwd_correct = 'password'
        pwd_incorrect = 'passwrd'
        pwd_hashed = '608c111b63d4b98858849a1b44d46f88056b22a409bed7250269e03ff28ccdbc'
        pwd_hashed += ':2b1d50bb859e4474a3ca5de7c87bfa82'

        self.assertFalse(password.validate_password(pwd_incorrect, pwd_hashed))
        self.assertTrue(password.validate_password(pwd_correct, pwd_hashed))


if __name__ == '__main__':
    unittest.main()
