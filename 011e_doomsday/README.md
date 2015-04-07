## Information

**Challenge name:** [Doomsday](http://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/)  
**Challenge number:** 11  
**Difficulty:** Easy  
**Submission date:** 2012-02-19  
**Status:** Complete

## Description

The program should take three arguments. The first will be a day, the second will be month, and the third
will be year. Then, your program should compute the day of the week that date will fall on.

## Development notes

### 2015-03-27, 07:32

This challenge immediately reminded me of the [Doomsday Algorithm](http://en.wikipedia.org/wiki/Doomsday_rule),
a method for calculating the day of the week for any given date. You need to remember a few simple rules,
practice a little bit, and you'll be calculating the day of the week your birthday will be on next year in
no time. Neat party trick.

A few months ago I took the time to learn the "Odd+11" method of calculating the doomsday of a year. Luck has
it that I even wrote a little piece of code to help me practice the Doomsday Algorithm. So I will take that
out of the closet filled with dusty code, clean up and adjust, and that should be it.

### 2015-03-27, 09:48

**Description**

Ok, the script has been updated, and it is done. I created a `Doomsday` class, which can be initialized
by providing a day, month and year. The method `weekday()` then returns the date's day of the week. You
can also initialize an object with a random date, by using the classmethod `random_date(minyear, maxyear)`,
which will set a random date between minyear-1-1 and maxyear-12-31 (inclusive). The default minyear and
maxyear are 1800 and 2199, respectively. The code works outside of this range, for a minyear as low as
1583. Before that the Julian calendar was still in effect, and the Doomsday Algorithm won't be correct.

The `random_date()` classmethod was included to be used in a little game in which the Doomsday Algorithm
can be practiced. The code for the game is in the main body of the script, so you launch it with the
following command:

    $ python3.4 doomsday.py

The user is welcomed and then continuouly asked to type the weekday for a given random date. The user's
current streak and highscore is tracked. Stopping can be done by typing 'quit' instead of a weekday.

**Output from test run**

Following is the output of a short test performed on the `Doomsday.weekday()` method. The results were
compared with the output of the online weekday calculator (see sources) and were found to be correct.

    $ python3.4
    >>> from doomsday import Doomsday
    >>> date = Doomsday(27,3,2015)  ## Test on the day this script was created.
    >>> date.weekday()
    'friday'
    >>> date.year = 2000  ## Test a leap year.
    >>> date.weekday()
    'monday'
    >>> date = Doomsday.random_date()  ## Test a few random dates.
    >>> print(date);print(date.weekday())
    1825-12-12
    monday
    >>> date = Doomsday.random_date()
    >>> print(date);print(date.weekday())
    1986-5-5
    monday
    >>> date = Doomsday.random_date()
    >>> print(date);print(date.weekday())
    2056-11-22
    wednesday

**Sources**

- [Odd+11 Doomsday Algorithm on Wikipedia](http://en.wikipedia.org/wiki/Doomsday_rule#The_Odd.2B11_method)
- [Online weekday calculator](http://www.timeanddate.com/date/weekday.html)

Looks like challenge is complete!
