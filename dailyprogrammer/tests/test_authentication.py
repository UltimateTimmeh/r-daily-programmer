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


if __name__ == '__main__':
    unittest.main()
