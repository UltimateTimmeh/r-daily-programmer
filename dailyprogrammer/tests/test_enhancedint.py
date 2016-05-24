#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_enhancedint.py

Unit tests for module :mod:`plugins.enhancedint` (source_).
"""

import unittest

from plugins import enhancedint


class TestEnhancedInt(unittest.TestCase):
    """Unit tests for class :func:`plugins.enhancedint.EnhancedInt`."""


    def test___init__(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.__init__`

        **Tested:**

        - The attributes of an enhanced integer are correct after initialization with an integer.
        - The attributes of an enhanced integer are correct after initialization with an integer
          in a base smaller than 10.
        - The attributes of an enhanced integer are correct after initialization with a string.
        - The attributes of an enhanced integer are correct after initialization with a list
          of integers.
        - A TypeError is raised when initializing an enhanced integer with an integer and a base
          larger than 10.
        - A ValueError is raised when initializing an enhanced integer with digits higher than
          its base.
        """
        int_ = enhancedint.EnhancedInt(123)
        self.assertEqual(int_.digits, [1, 2, 3])
        self.assertEqual(int_.base, 10)

        int_ = enhancedint.EnhancedInt(123, base=5)
        self.assertEqual(int_.digits, [1, 2, 3])
        self.assertEqual(int_.base, 5)

        int_ = enhancedint.EnhancedInt('12:25:0', base=26)
        self.assertEqual(int_.digits, [12, 25, 0])
        self.assertEqual(int_.base, 26)

        int_ = enhancedint.EnhancedInt([124, 0, 26], base=125)
        self.assertEqual(int_.digits, [124, 0, 26])
        self.assertEqual(int_.base, 125)

        with self.assertRaises(TypeError):
            int_ = enhancedint.EnhancedInt(123, base=15)

        with self.assertRaises(ValueError):
            int_ = enhancedint.EnhancedInt('125:26:0', base=125)


    def test___valid__(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.__valid__`

        **Tested:**

        - The returned boolean is correct.
        """
        int_ = enhancedint.EnhancedInt('12:56:78', base=80)
        self.assertTrue(int_.__valid__())

        int_.base = 75
        self.assertFalse(int_.__valid__())


    def test___str__(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.__str__`

        **Tested:**

        - The returned string is correct for a number with base smaller than or equal to 10.
        - The returned string is correct for a number with base higher than 10.
        """
        str_ = enhancedint.EnhancedInt(123, base=4)
        self.assertEqual(str_.__str__(), '123 (b4)')

        str_ = enhancedint.EnhancedInt('12:36:78', base=100)
        self.assertEqual(str_.__str__(), '12:36:78 (b100)')


    def test___mul__(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.__mul__`

        **Tested:**

        - The returned object is an enhanced integer.
        - The returned enhanced integer is correct.
        """
        int1 = enhancedint.EnhancedInt(25)
        int2 = enhancedint.EnhancedInt(3)
        mul = int1*int2
        self.assertEqual(type(mul), enhancedint.EnhancedInt)
        self.assertEqual(mul.digits, [7, 5])
        self.assertEqual(mul.base, 10)

        int1 = enhancedint.EnhancedInt(25, base=6)
        int2 = enhancedint.EnhancedInt('125:63:7:0', base=150)
        mul = int1*int2
        self.assertEqual(type(mul), enhancedint.EnhancedInt)
        self.assertEqual(mul.digits, [3, 1, 5, 0, 0, 1, 5, 0, 1, 4, 0, 5, 0])
        self.assertEqual(mul.base, 6)


    def test_base10(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.base10`

        **Tested:**

        - The returned integer is correct.
        """
        int_ = enhancedint.EnhancedInt('125:63:7:0', base=150)
        self.assertEqual(int_.base10(), 423293550)


    def test_convert(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.convert`

        **Tested:**

        - The returned converted enhanced integer is correct.
        """
        int_ = enhancedint.EnhancedInt('125:63:7:0', base=150)
        result = int_.convert(6)
        self.assertEqual(result.digits, [1, 1, 0, 0, 0, 0, 3, 5, 2, 2, 1, 0])
        self.assertEqual(result.base, 6)


    def test_as_words(self):
        """Test method :meth:`plugins.enhancedint.EnhancedInt.as_words`

        **Tested:**

        - The returned string is correct.
        """
        int_ = enhancedint.EnhancedInt('125:63:7:0', base=150)
        expected = ("four hundred twenty-three million two hundred ninety-three thousand "
                    "five hundred fifty")
        self.assertEqual(int_.as_words(), expected)

        int_ = enhancedint.EnhancedInt(0)
        expected = 'zero'
        self.assertEqual(int_.as_words(), expected)

