#!/usr/bin/python3
"""
Unit tests for module :mod:`plugins.pi`.
"""

import decimal
import math
import unittest

from plugins import pi


class TestPiFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.pi`."""


    def test_trunc(self):
        """Test function :func:`plugins.pi.trunc`

        **Tested:**

        - The number is truncated correctly.
        """
        dec = decimal.Decimal('3.141592')
        self.assertEqual(pi.trunc(dec, 4), decimal.Decimal('3.14'))


    def test_bbp(self):
        """Test function :func:`plugins.pi.bbp`

        **Tested:**

        - The returned calculation of pi is correct.
        """
        self.assertEqual(float(pi.bbp()), math.pi)


    def test_bellard(self):
        """Test function :func:`plugins.pi.bellard`

        **Tested:**

        - The returned calculation of pi is correct.
        """
        self.assertEqual(float(pi.bellard()), math.pi)


    def test_chudnovsky(self):
        """Test function :func:`plugins.pi.chudnovsky`

        **Tested:**

        - The returned calculation of pi is correct.
        """
        self.assertEqual(float(pi.chudnovsky()), math.pi)


if __name__ == '__main__':
    unittest.main()
