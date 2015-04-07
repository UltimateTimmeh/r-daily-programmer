## Information

**Challenge name:** [Remove characters](http://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/)  
**Challenge number:** 16  
**Difficulty:** Easy  
**Submission date:** 2012-02-27  
**Status:** Complete

## Description

Write a function that takes two strings and removes from the first string any character that appears
in the second string. For instance, if the first string is `Daily Programmer` and the second string
is `aeiou ` the result is `DlyPrgrmmr`. Note that the second string has the [space] character in it,
so the space in "Daily Programmer" is also removed

## Development notes

### 2015-04-07, 14:12

**Description**

The `enhancedstring` module contains a class `EnhancedString`. This is a class that I will use in this
challenge (and future ones) to develop these types of useful expansions for the default `str` class. For
this challenge, the method `remove(chars)` was added. It will remove all instances of every character in
`chars` from the `EnhancedString` object's `_str` attribute. This is achieved by looping over all characters
in `chars` and replacing every instance of those characters with an empty string (`''`). I'm not sure if
this is the most optimal way to do it in Python 3 (there were definitely easier ways in Python 2 that are
now no longer available), but after some looking around it appears to be the easiest solution to this problem.

**Output of test run**

Here is the output of a test using the example from the challenge description:

    $ python3
    >>> from enhancedstring import EnhancedString
    >>> _str = EnhancedString("Daily Programmer")
    >>> print(_str)
    Daily Programmer
    >>> _str.remove('aeiou ')
    >>> print(_str)
    DlyPrgrmmr

Challenge complete.
