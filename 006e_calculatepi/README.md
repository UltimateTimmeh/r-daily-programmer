## Information

**Challenge name:** [Calculate pi](http://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/)  
**Challenge number:** 6  
**Difficulty:** Easy  
**Submission date:** 2012-02-14  
**Status:** Complete

## Description

Your challenge for today is to create a program that can calculate pi accurately to at least 30 decimal
places. 

Try not to cheat :-).

## Development notes

*<2015-02-28, 19:14>*  
I implemented three different formulas to calculate pi. The user can choose which formula, and the desired
precision. The actual value of pi (up to 74 decimal numbers) is printed as well to check if the calculated
number is correct. In my experience the first n-2 digits are accurate, but the final two digits (taking into
account rounding) are not always correct. In other words, if you want to accurately calculate the first
30 digits of pi, then you should request a calculation for the first 32 digits. This challenge is complete.

PS: [I couldn't do this one without cheating](http://thelivingpearl.com/2013/05/28/computing-pi-with-python/)
