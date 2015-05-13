#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/doomsday.py

Calculate neat properties of arbitrary dates (source_).

| *var* plugins.doomsday.\ **anchordays** *(list(int, ...))*
|     list containing the anchor days for the 2000s, 2100s, 1800s and 1900s respectively

| *var* plugins.doomsday.\ **ndays_in_months** *(dict(bool: list(int, ...), ...))*
|     dictionary containing the amount of days in each month for both normal and leap years

| *var* plugins.doomsday.\ **doomsdate_in_months** *(dict(bool: list(int, ...), ...))*
|     dictionary containing one day per month that falls on the doomsday, for both normal and
      leap years

| *var* plugins.doomsday.\ **weekdays** *(list(str, ...))*
|     list containing the names of the day of the week in order, starting at sunday
"""

import random

anchordays = [2, 0, 5, 3]

ndays_in_months = {
    False: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    True: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
}

doomsdate_in_months = {
    False: [3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12],
    True: [4, 29, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12],
}

weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def is_leapyear(year):
    """Determine if a year is a leap year.

    :param int year: the year
    :return: True if the year is a leap year, False otherwise
    :rtype: bool

    Example::

        >>> from doomsday import is_leapyear
        >>> is_leapyear(2015)
        False
        >>> is_leapyear(2016)
        True
        >>> is_leapyear(2100)
        False
        >>> is_leapyear(2000)
        True
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


class Date(object):
    """A class representing a date.

    A date is characterized by a day, month and year. This class only supports the Gregorian
    calendar, not the Julian calendar, so the minimum year that is allowed is 1583.

    :param int year: the year, must be at least 1583
    :param int month: the month, must be between 1 and 12
    :param int day: the day, must be between 1 and 31 (depending on the year and month)
    :raise: ValueError if the passed combination of day-month-year is invalid

    Example::

        >>> from doomsday import Date
        >>> date = Date(2015, 5, 13)
        >>> print(date)
        2015-5-13
    """

    def __init__(self, year, month, day):
        """Create a new date."""
        self.year = year
        self.month = month
        self.day = day
        if not self.is_valid():
            raise ValueError("Invalid date for Date object: {}".format(self.__str__()))


    def __str__(self):
        """Format the date as a string."""
        return '{}-{}-{}'.format(self.year, self.month, self.day)


    def is_valid(self):
        """Check if the date is valid.

        A date is invalid if the year is lower than 1583, the month is impossible (below 1 or
        above 12) or the day is impossible for the month in the year.

        :return: True if the date is valid, False otherwise
        :rtype: bool

        Example::

            >>> from doomsday import Date
            >>> date = Date(2016, 2, 29)
            >>> date.is_valid()
            True
            >>> date.year = 2015
            >>> date.is_valid()
            False
        """
        if self.year < 1583:
            return False
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1 or self.day > self.ndays_in_month():
            return False
        return True


    def century(self):
        """Return the date's century.

        For the purpose of the doomsday algorithm, a century will start at '00 and end at '99.

        :return: the date's century
        :rtype: int

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.century()
            21
        """
        return int(self.year/100)+1


    def anchorday(self, h=False):
        """Return the century's anchor day.

        The anchor day of a century is the doomsday of the first year of that century.

        :param bool h: return the anchor day in 'human-readable' form (default False)
        :return: the century's anchor day
        :rtype: int or str

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.anchorday(h=True)
            'tuesday'
        """
        anchorday = anchordays[(self.century()-1) % 4]
        if h:
            return weekdays[anchorday]
        return anchorday


    def doomsday(self, h=False):
        """Return the year's doomsday.

        The doomsday of a year is a day of the week upon which certain easy-to-remember dates
        fall. For more information, see the `Doomsday rule on Wikipedia <http://en.wikipedia.org/wiki/Doomsday_rule>`_.
        Here, the explicit 'Odd+11' formula is used for calculating the offset between the
        century's anchor day and the year's doomsday.

        :param bool h: return the doomsday in 'human-readable' form (default False)
        :return: the year's doomsday
        :rtype: int or str

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.doomsday(h=True)
            'saturday'
        """
        year = int(str(self.year)[-2:])
        cse = (year + 11*(year % 2))/2  ## This is a 'common subexpression'.
        offset = -(cse + 11*(cse % 2)) % 7
        doomsday = int(self.anchorday() + offset) % 7
        if h:
            return weekdays[doomsday]
        return doomsday


    def ndays_in_month(self):
        """Return the amount of days in the month.

        :return: the amount of days in the month
        :rtype: int

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.ndays_in_month()
            31
        """
        return ndays_in_months[is_leapyear(self.year)][self.month-1]


    def doomsdate(self):
        """Return the month's doomsdate.

        The doomsdate of a month is the easy-to-remember day of the month that falls on the
        corresponding year's doomsday.

        :return: the month's doomsdate
        :rtype: int

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.doomsdate()
            9
        """
        return doomsdate_in_months[is_leapyear(self.year)][self.month-1]


    def weekday(self, h=False):
        """Return the date's weekday.

        A date's weekday is the day of the week upon which the date falls.

        :param bool h: return the weekday in 'human-readable' form (default False)
        :return: the date's weekday
        :rtype: int or str

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.weekday(h=True)
            'wednesday'
        """
        weekday = (self.doomsday() + (self.day-self.doomsdate())) % 7
        if h:
            return  weekdays[weekday]
        return weekday


    def cumulative_day_of_year(self):
        """Calculate the date's cumulative day of the year.

        :return: the date's cumulative day of the year
        :rtype: int

        Example::

            >>> from doomsday import Date
            >>> date = Date(2015, 5, 13)
            >>> date.cumulative_day_of_year()
            133
        """
        return sum(ndays_in_months[is_leapyear(self.year)][:self.month-1]) + self.day


    @classmethod
    def random(cls, minyear=1800, maxyear=2199):
        """Create a random date.

        :param int minyear: minimum year for random date (default 1800)
        :param int maxyear: maximum year for random date (default 2199)
        :return: a random date between the minimum and the maximum year
        :rtype: Date

        Example::

            >>> from doomsday import Date
            >>> date = Date.random()
            >>> print(date)
            2191-3-6
        """
        year = random.randint(minyear, maxyear)
        month = random.randint(1, 12)
        day = random.randint(1, ndays_in_months[is_leapyear(year)][month-1])
        return cls(year, month, day)

