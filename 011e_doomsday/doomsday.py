#!/usr/bin/python3
"""
Module containing the Doomsday class, a class for storing and handling
date objects. Its main objective is to calculate the weekday for any
given date using the Doomsday algorithm.
"""

import random


class Doomsday(object):
    """Stores a (potentially random) date and can calculate the weekday."""
    # Days of the week.
    weekdays = [
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        ]

    # Amount of days in each month in a normal and leap year.
    days_in_months_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Anchor days for 2000's, 2100's, 1800's and 1900's.
    anchordays = [2, 0, 5, 3]

    # Days of the month that fall on a normal and leap year's doomsday.
    doomsdates_shared = [0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    doomsdates_normal = [3, 28] + doomsdates_shared
    doomsdates_leap = [4, 29] + doomsdates_shared


    def __init__(self, day=1, month=1, year=2015):
        """Initialize a Doomsday object."""
        self.day = day
        self.month = month
        self.year = year

        valid, error = self.is_valid()
        if not valid:
            raise ValueError(error)


    def __str__(self):
        """Format self as a string."""
        return '{}-{}-{}'.format(self.year, self.month, self.day)


    @classmethod
    def random_date(cls, minyear=1800, maxyear=2199):
        """Initiate a Doomsday object with a random date.

        The date will be between minyear-1-1 and maxyear-12-31 (inclusive).
        """
        # Make sure minyear is higher than 1582, because until then
        # the Julian calendar was used.
        minallowed = 1583
        if minyear < minallowed:
            error = "The Gregorian calendar has only been in use since {0}. "
            error += "Therefore, minyear must be at least '{0}', got '{1}'."
            raise ValueError(error.format(minallowed, minyear))
        year = random.randint(minyear,maxyear)
        month = random.randint(1,12)
        if month in [4, 6, 9, 11]:
            maxday = 30
        elif month == 2 and cls.is_leapyear(year):
            maxday = 29
        elif month==2 and not cls.is_leapyear(year):
            maxday = 28
        else:
            maxday = 31
        day = random.randint(1,maxday)
        return cls(day, month, year)


    @staticmethod
    def is_leapyear(year):
        """Determine if year is a leap year."""
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False


    def is_valid(self):
        """Check if self is a valid date. If not, give reason why."""
        # Checks independent of leap years.
        if self.year < 1583:
            error = "This class assumes the Gregorian calendar, which "
            error += "was not introduced until 1583. Therefore, the "
            error += "year must be at least 1583 (got {})."
            error = error.format(self.year)
            return False, error
        if self.month < 1 or self.month > 12:
            error = "Month must be between 1 and 12 (got {})."
            error = error.format(self.month)
            return False, error
        if self.day < 1:
            error = "Day must be at least 1 (got {})."
            error = error.format(self.day)
            return False, error

        # Checks that depend on leap years.
        if not Doomsday.is_leapyear(self.year):
            days_in_months = Doomsday.days_in_months_normal
        else:
            days_in_months = Doomsday.days_in_months_leap
        days_in_month = days_in_months[self.month-1]
        if self.day > days_in_month:
            error = "Month {} in year {} has at most {} days "
            error += "(got {})."
            error = error.format(self.month, self.year, days_in_month, self.day)
            return False, error

        # All checks passed.
        return True, ''



    def century(self):
        """Determine the century self is in."""
        return int(self.year/100)+1


    def anchorday(self):
        """Determine the anchor day of self's century."""
        return Doomsday.anchordays[(self.century()-1) % 4]


    def doomsday(self):
        """Calculate the doomsday of self.year.

        Algorithm for calculating the doomsday in your mind:
        1) Calculate the offset from the century's anchor day.
           - Add 11 to the final two digits of self.year until divisible by
             four.
           - Divide the resulting number by two.
           - Calculate the difference of the resulting number with the next
             multiple of seven.
           - This is the anchor day offset.
        2) Shifting the century's anchor day forward with this offset will
           give you the doomsday of self.year.

        However, there is an explicit formula for calculating the anchor day
        offset (see 'http://en.wikipedia.org/wiki/Doomsday_rule#The_Odd.2B11_method'),
        so it is a lot simpler in code.
        """
        year = int(str(self.year)[-2:])
        cse = (year + 11*(year % 2))/2  ## "Common SubExpression"
        offset = -(cse + 11*(cse % 2)) % 7
        return int(self.anchorday() + offset) % 7


    def weekday(self):
        """Calculate the weekday of self."""
        # Calculate the doomsdate for the current month.
        if not Doomsday.is_leapyear(self.year):
            doomsdate = Doomsday.doomsdates_normal[self.month-1]
        else:
            doomsdate = Doomsday.doomsdates_leap[self.month-1]

        # Calculate the weekay of self.
        wi = (self.doomsday() + (self.day-doomsdate)) % 7
        return Doomsday.weekdays[wi]


    def yearday(self):
        """Calculate the day of the year of self."""
        if not Doomsday.is_leapyear(self.year):
            days_in_months = Doomsday.days_in_months_normal
        else:
            days_in_months = Doomsday.days_in_months_leap
        yearday = sum(days_in_months[:self.month-1]) + self.day
        return yearday


if __name__ == '__main__':
    # Function for getting user input.
    def get_user_input():
        """Get user input and make sure it is valid."""
        weekday = input('> ').lower()
        while weekday not in Doomsday.weekdays + ['quit']:
            invalidtext = "'{}' is not a valid day of the week. Please try again."
            print(invalidtext.format(weekday))
            weekday = input('> ').lower()
        return weekday

    # Set texts to be printed.
    welcometext = '''
===========================
Doomsday Algorithm Practice
===========================
Welcome! This script allows you to practice the Doomsday Algoritm.
A random date is generated, and you have to calculate and enter the
correct day of the week for this date.
Your current streak and session highscore are tracked.
Good luck!
'''

    highscoretext = '''
------------------------------
Highscore = {}
Current streak = {}
------------------------------
'''

    goodbyetext = '''
Game over. Your highest streak was {}.
Thanks for practicing, and see you next time!
'''

    # Welcome the user and initialize scores.
    print(welcometext)
    input("<Press ENTER to start>")
    streak = 0
    highscore = 0

    # Infinite loop until the user types 'quit'.
    while True:
        # Set random date and get correct weekday.
        date = Doomsday.random_date()
        correct_weekday = date.weekday()

        # Ask the user for his weekday calculation.
        print(highscoretext.format(highscore, streak))
        print("What day of the week is {}?".format(date))
        user_weekday = get_user_input()

        # Check if the user wants to quit of if the provided day is correct.
        if user_weekday == 'quit':
            break
        if user_weekday == correct_weekday:
            print("CORRECT! ", end='')
            streak += 1
        else:
            print("WRONG! ", end='')
            streak = 0

        # Print the correct weekday.
        print("{} is a {}".format(date, correct_weekday))

        # If needed, update highscore.
        if streak > highscore:
            highscore = streak
        input('<Press ENTER to continue>')
    print(goodbyetext.format(highscore))

# End
