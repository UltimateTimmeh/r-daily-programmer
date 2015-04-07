## Information

**Challenge name:** [Permutation](http://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/)  
**Challenge number:** 12  
**Difficulty:** Easy  
**Submission date:** 2012-02-20  
**Status:** Complete

## Description

Write a small program that can take a string (e.g. "hi!") and print all the possible permutations
of the string:

"hi!"  
"h!i"  
"ih!"  
"i!h"  
"!hi"  
"!ih"

Thanks to hewts for this challenge!

## Development notes

### 2015-04-07, 08:41

**Description**

This one can easily be solved with a recursive function. Concatenate each character of the string with
all permutations of the remaining substring. If the (sub)string is only one character long, then the list
of permutations of that (sub)string contains only that single character.

**Output from test run**

    $ python3.4 permutation.py 
    Input > hi!
    Output >
    hi!
    h!i
    ih!
    i!h
    !hi
    !ih

Challenge complete!
