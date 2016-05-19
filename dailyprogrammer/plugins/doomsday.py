#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/doomsday.py

Calculate neat properties of arbitrary dates (source_).

| *var* plugins.doomsday.\ **anchordays** *(list(int, ...))*
|     list containing the anchor days for the 1900s, 2000s, 2100s and 1800s respectively

| *var* plugins.doomsday.\ **ndays_in_months** *(dict(bool: list(int, ...), ...))*
|     dictionary containing the amount of days in each month for both normal and leap years

| *var* plugins.doomsday.\ **doomsdate_in_months** *(dict(bool: list(int, ...), ...))*
|     dictionary containing one day per month that falls on the doomsday, for both normal and
      leap years

| *var* plugins.doomsday.\ **weekdays** *(list(str, ...))*
|     list containing the names of the day of the week in order, starting at sunday
"""

import random

anchordays = [3, 2, 0, 5]

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


def century(year, mode='real'):
    """Return the century of a year in a certain mode.

    Commonly, a century is defined to start at '01 and ends at '00. But for the purpose of the
    doomsday algorithm, a mode is added where a century is defined to start at '00 and end at '99
    instead. This definition will be referred to as the 'doomsday century' of a year.

    :param int year: the year to determine the century of
    :param str mode: mode of century calculation, one of 'real' or 'doomsday' (default 'real')
    :return: the year's century
    :rtype: int

    Example::

        >>> century(2000)
        20
        >>> century(2000, mode='doomsday')
        21
    """
    return (year + {'real': 99, 'doomsday': 100}[mode]) // 100


def anchorday(year, h=False):
    """Return the year's anchor day.

    The anchor day of a year is the doomsday of the first year of that year's century.

    :param int year: the year to determine the anchor day of
    :param bool h: return the anchor day in 'human-readable' form (default False)
    :return: the year's anchor day
    :rtype: int or str

    Example::

        >>> anchorday(2015, h=True)
        'tuesday'
    """
    anchorday = anchordays[century(year, mode='doomsday') % 4]
    return {True: weekdays[anchorday], False: anchorday}[h]


def doomsday(year, h=False):
    """Return the year's doomsday.

    The doomsday of a year is a day of the week upon which certain easy-to-remember dates
    fall. For more information, see the `Doomsday rule on Wikipedia <http://en.wikipedia.org/wiki/Doomsday_rule>`_.
    Here, the explicit 'Odd+11' formula is used for calculating the offset between the
    century's anchor day and the year's doomsday.

    :param int year: the year to determine the doomsday of
    :param bool h: return the doomsday in 'human-readable' form (default False)
    :return: the year's doomsday
    :rtype: int or str

    Example::

        >>> doomsday(2015, h=True)
        'saturday'
    """
    year_short = int(str(year)[-2:])
    cse = (year_short + 11*(year_short % 2))/2  ## This is a 'common subexpression'.
    offset = -(cse + 11*(cse % 2)) % 7
    doomsday = int(anchorday(year) + offset) % 7
    return {True: weekdays[doomsday], False: doomsday}[h]


def ndays_in_month(month, year):
    """Return the amount of days in a month, depending on it being a leap year.

    :param int month: the month to determine the amount of days of
    :param int year: year in which the month falls, to determine whether or not it's a leap year
    :return: the amount of days in the month
    :rtype: int

    Example::

        >>> ndays_in_month(2, 2015)
        28
        >>> ndays_in_month(2, 2016)
        29
    """
    return ndays_in_months[is_leapyear(year)][month-1]


def doomsdate(month, leap):
    """Return the month's doomsdate, depending on it being a leap year.

    The doomsdate of a month is the easy-to-remember day of the month that falls on the
    corresponding year's doomsday.

    :param int month: the month to determine the doomsdate of
    :param bool leap: indication for whether or not the month falls in a leap year
    :return: the month's doomsdate
    :rtype: int

    Example::

        >>> doomsdate(1, False)
        3
        >>> doomsdate(1, True)
        4
    """
    return doomsdate_in_months[leap][month-1]


class Date(object):
    """A class representing a date.

    A date is characterized by a day, month and year. This class only supports the Gregorian
    calendar, not the Julian calendar, so the minimum year that is allowed is 1583.

    :param int year: the year, must be at least 1583
    :param int month: the month, must be between 1 and 12
    :param int day: the day, must be between 1 and 31 (depending on the year and month)
    :raise: ValueError if the passed combination of day-month-year is invalid

    Example::

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
        above 12) or the day is impossible for the month in that specific year.

        :return: True if the date is valid, False otherwise
        :rtype: bool

        Example::

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
        if self.day < 1 or self.day > ndays_in_month(self.month, self.year):
            return False
        return True


    def weekday(self, h=False):
        """Return the date's weekday.

        A date's weekday is the day of the week upon which the date falls.

        :param bool h: return the weekday in 'human-readable' form (default False)
        :return: the date's weekday
        :rtype: int or str

        Example::

            >>> Date(2015, 5, 13).weekday(h=True)
            'wednesday'
        """
        weekday = (doomsday(self.year)+(self.day-doomsdate(self.month, is_leapyear(self.year)))) % 7
        return {True: weekdays[weekday], False: weekday}[h]


    def cumulative_day_of_year(self):
        """Calculate the date's cumulative day of the year.

        :return: the date's cumulative day of the year
        :rtype: int

        Example::

            >>> Date(2015, 5, 13).cumulative_day_of_year()
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

            >>> print(Date.random())
            2191-3-6
        """
        year = random.randint(minyear, maxyear)
        month = random.randint(1, 12)
        day = random.randint(1, ndays_in_months[is_leapyear(year)][month-1])
        return cls(year, month, day)

