## Information

**Challenge name:** [Block invert](http://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/)  
**Challenge number:** 14  
**Difficulty:** Easy  
**Submission date:** 2012-02-23  
**Status:** Complete

## Description

**Input:** List of elements and a block size k or some other variable of your choice.  
**Output:** Return the list of elements with every block of k elements reversed, starting from the beginning
of the list.  
**Example:** Given the list `[12, 24, 32, 44, 55, 66]` and the block size `k = 2`, the result is
`[24, 12, 44, 32, 66, 55]`.

## Development notes

### 2015-04-07, 10:31

**Description**

Very easy to do in python with list comprehension. It's possible to do it in one line without making it
very long, but for readability I have chosen to do it in three lines. It works by calculating the
amount of times the block size fits into the length of the list (plus one). Using this information
you can slice the list in a correct amount of sublists, which can be inverted and finally concatenated.

The main body of the module asks for a list length and the block size, executes the function and
prints the result.

**Output from test run**

This is a test run with a list length of 11 and a block size of 3:

    $ python3 blockinvert.py 
    List length > 11
    Block size > 3
    [2, 1, 0, 5, 4, 3, 8, 7, 6, 10, 9]

Seems to be correct. Challenge complete!
