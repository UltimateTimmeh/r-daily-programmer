#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_doomsday.py

Unit tests for module :mod:`plugins.doomsday` (source_).
"""

import unittest

from plugins import doomsday


class TestDoomsdayFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.doomsday`."""


    def test_is_leapyear(self):
        """Test function :func:`plugins.doomsday.is_leapyear`

        **Tested:**

        - True is returned for a year divisible by 400.
        - False is returned for a year divisible by 100 but not 400.
        - True is returned for a year divisibe by 4 but neither 100 or 400.
        - False is returned for a year that is not divisible by 4.
        """
        self.assertTrue(doomsday.is_leapyear(2000))
        self.assertFalse(doomsday.is_leapyear(2100))
        self.assertTrue(doomsday.is_leapyear(2016))
        self.assertFalse(doomsday.is_leapyear(2015))


    def test_century(self):
        """Test function :func:`plugins.doomsday.century`

        **Tested:**

        - The correct century according to the common definition is returned.
        - The correct century according to the doomsday definition is returned.
        """
        self.assertEqual(doomsday.century(2000), 20)
        self.assertEqual(doomsday.century(2000, mode='doomsday'), 21)


    def test_anchorday(self):
        """Test function :func:`plugins.doomsday.anchorday`

        **Tested:**

        - The correct anchor day of the year is returned as an integer.
        - The correct anchor day of the year is returned as a string.
        """
        self.assertEqual(doomsday.anchorday(2015), 2)
        self.assertEqual(doomsday.anchorday(2015, h=True), 'tuesday')


    def test_doomsday(self):
        """Test function :func:`plugins.doomsday.doomsday`

        **Tested:**

        - The correct doomsday of the year is returned as an integer.
        - The correct doomsday of the year is returned as a string.
        """
        self.assertEqual(doomsday.doomsday(2015), 6)
        self.assertEqual(doomsday.doomsday(2015, h=True), 'saturday')


    def test_ndays_in_month(self):
        """Test function :func:`plugins.doomsday.ndays_in_month`

        **Tested:**

        - The correct amount of days in the month is returned.
        """
        self.assertEqual(doomsday.ndays_in_month(2015, 2), 28)
        self.assertEqual(doomsday.ndays_in_month(2016, 2), 29)


    def test_doomsdate(self):
        """Test function :func:`plugins.doomsday.doomsdate`

        **Tested:**

        - The correct doomsdate of the month is returned.
        """
        self.assertEqual(doomsday.doomsdate(2015, 1), 3)
        self.assertEqual(doomsday.doomsdate(2016, 1), 4)


class TestDate(unittest.TestCase):
    """Unit tests for class :func:`plugins.doomsday.Date`."""


    def test___init__(self):
        """Test method :meth:`plugins.doomsday.Date.__init__`

        **Tested:**

        - The attributes of a valid date are correct after initialization.
        - A ValueError is raised when initializing an invalid date.
        """
        date = doomsday.Date(2015, 5, 13)
        self.assertEqual(date.year, 2015)
        self.assertEqual(date.month, 5)
        self.assertEqual(date.day, 13)
        with self.assertRaises(ValueError):
            doomsday.Date(2015, 2, 29)


    def test___str__(self):
        """Test method :meth:`plugins.doomsday.Date.__str__`

        **Tested:**

        - The returned string is correct.
        """
        date = doomsday.Date(2015, 5, 13)
        self.assertEqual(date.__str__(), '2015-5-13')


    def test_is_valid(self):
        """Test method :meth:`plugins.doomsday.Date.is_valid`

        **Tested:**

        - False is returned for a year below 1583.
        - False is returned for a month below 1.
        - False is returned for a month above 12.
        - False is returned for a day below 1.
        - False is returned for a day above the amount of days in the month.
        - True is returned for a valid day.
        """
        date = doomsday.Date(1583, 1, 1)
        date.year = 1582
        self.assertFalse(date.is_valid())
        date.year = 2015
        date.month = 0
        self.assertFalse(date.is_valid())
        date.month = 13
        self.assertFalse(date.is_valid())
        date.month = 2
        date.day = 0
        self.assertFalse(date.is_valid())
        date.day = 29
        self.assertFalse(date.is_valid())
        date.day = 28
        self.assertTrue(date.is_valid())


    def test_weekday(self):
        """Test method :meth:`plugins.doomsday.Date.weekday`

        **Tested:**

        - The correct weekday of the date is returned as an integer.
        - The correct weekday of the date is returned as a string.
        """
        date = doomsday.Date(2015, 5, 13)
        self.assertEqual(date.weekday(), 3)
        self.assertEqual(date.weekday(h=True), 'wednesday')


    def test_cumulative_day_of_year(self):
        """Test method :meth:`plugins.doomsday.Date.cumulative_day_of_year`

        **Tested:**

        - The correct cumulative day of the year for the date is returned.
        """
        date = doomsday.Date(2015, 5, 13)
        self.assertEqual(date.cumulative_day_of_year(), 133)


    def test_random(self):
        """Test classmethod :meth:`plugins.doomsday.Date.random`

        **Tested:**

        - The randomly generated date is valid (given that the year is not lower than 1583).
        """
        self.assertTrue(doomsday.Date.random().is_valid())


if __name__ == '__main__':
    unittest.main()

