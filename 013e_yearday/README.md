## Information

**Challenge name:** [Yearday](http://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/)  
**Challenge number:** 13  
**Difficulty:** Easy  
**Submission date:** 2012-02-21  
**Status:** Complete

## Description

Find the number of the year for the given date. For example, january 1st would be 1, and december 31st is 365.

For extra credit, allow it to calculate leap years, as well.

## Development notes

### 2015-04-07, 09:05

**Description**

The solution for this challenge has been implemented in the `Doomsday` class (see challenge 011e). Given
the nature of this challenge, it was only logical to make use of the existing `Doomsday` class. That class,
for example, is ready to handle leap years. Calculating the day of the year for any given date
can be done by simply adding one method, in this case `Doomsday.yearday()`.

However, another method `Doomday.is_valid()` has been added, which is executed upon initialization of
a Doomsday object. It checks whether or not the given date is valid. If not, it returns `False` and the
reason why the date is invalid. In the initialization function, this reason is raised as a ValueError.
This is just an extra check to make sure valid dates are being handled.

**Output from test run**

Following is the output of a short test performed on the `Doomsday.yearday()` method. The results were
compared with the output of the online calculator (see sources) and were found to be correct.

    $ python3.4
    >>> from doomsday import Doomsday
    >>> date = Doomsday(7,4,2015)  ## Test on the day the function was added.
    >>> date.yearday()
    97
    >>> date.year = 2000  ## Test a leap year.
    >>> date.yearday()
    98
    >>> date = Doomsday.random_date()
    >>> print(date);print(date.yearday())
    2183-5-2
    122
    >>> date = Doomsday.random_date()
    >>> print(date);print(date.yearday())
    2090-7-5
    186
    >>> date = Doomsday.random_date()
    >>> print(date);print(date.yearday())
    1891-1-3
    3

**Sources**

- [Online weekday calculator](http://www.timeanddate.com/date/weekday.html)

Looks like challenge is complete!
