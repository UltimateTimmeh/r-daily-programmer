#!/usr/bin/python3
"""
Unit tests for module :mod:`plugins.password`.
"""

import unittest
import random

from plugins import password


class TestPasswordFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.password`."""


    def test_random_password(self):
        """Test :func:`plugins.password.random_password`

        **Tested:**

        - The returned password length is correct when not passing a required length.
        - The returned password length is correct when passing a random required length.
        """
        # Test default password length.
        expected = 8
        result = len(password.random_password())
        self.assertEqual(result, expected)

        # Test random password length.
        expected = random.randint(10, 20)
        result = len(password.random_password(l=expected))
        self.assertEqual(result, expected)


    def test_hash_password(self):
        """Test :func:`plugins.password.hash_password`

        **Tested:**

        - The returned concatenation of hashed password and salt is correct.
        """
        pwd = 'password'
        salt = '2b1d50bb859e4474a3ca5de7c87bfa82'
        expected = '608c111b63d4b98858849a1b44d46f88056b22a409bed7250269e03ff28ccdbc'
        expected += ':2b1d50bb859e4474a3ca5de7c87bfa82'
        self.assertEqual(password.hash_password(pwd, salt), expected)


    def test_validate_password(self):
        """Test :func:`plugins.password.validate_password`

        **Tested:**

        - The returned boolean is False when a non-matching password and hash+salt couple
          are passed.
        - The returned boolean is True when a matching password and hash+salt are passed.
        """
        pwd_correct = 'password'
        pwd_incorrect = 'passwrd'
        pwd_hashed = '608c111b63d4b98858849a1b44d46f88056b22a409bed7250269e03ff28ccdbc'
        pwd_hashed += ':2b1d50bb859e4474a3ca5de7c87bfa82'

        self.assertFalse(password.validate_password(pwd_incorrect, pwd_hashed))
        self.assertTrue(password.validate_password(pwd_correct, pwd_hashed))


if __name__ == '__main__':
    unittest.main()
