## Information

**Challenge name:** [Ask input](http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/)  
**Challenge number:** 1  
**Difficulty:** Easy  
**Submission date:** 2012-02-10  
**Status:** Complete

## Description

Create a program that will ask the user's name, age, and reddit username.
Have it tell them the information back, in the format:

    Your name is (blank), you are (blank) years old, and your username is (blank).

For extra credit, have the program log this information in a file to be accessed later.

## Development notes

### *2015-02-26, 12:14*

This piece of code is so simple, it's not worth making anything more of it. I'll consider
this completed.

### 2015-04-08, 16:31

**Description**

Looks like I decided to make more of it after all. I basically threw out the old solution
and created a class `PersonalInfo` that has `name`, `age` and `reddit_username` as attributes.
The classmethod `PersonalInfo.ask()` can be used to initialize a `PersonalInfo` object by
asking for the three attributes. The method `PersonalInfo.__str__()` nicely formats the
object for printed output, and the `PersonalInfo.write()` method will write the formatted
info to a text file. The main body of the text does just that.

**Output from test run**

This is the output from the test run that was performed to write the enclosed 'output.txt'
file:

    $ python3
    >>> from personalinfo import PersonalInfo
    >>> pi = PersonalInfo.ask()
    Name? > John Smith
    Age? > 50
    Reddit Username? > John_Smith
    >>> print(pi)
    Your name is 'John Smith', you are 50 years old and your Reddit username is 'John_Smith'.
    >>> pi.write('output.txt')
