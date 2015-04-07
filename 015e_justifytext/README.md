## Information

**Challenge name:** [Justify text](http://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/)  
**Challenge number:** 15  
**Difficulty:** Easy  
**Submission date:** 2012-02-24  
**Status:** Complete

## Description

Write a program to left or right justify a text file

## Development notes

### 2015-04-07, 12:18

**Description**

Justification of text is easy in python with string formatting. Determine the length of the
longest line in the text and force this length together with the chosen justification on
each line. This has been implemented in the function `justify_text()` in the enclosed module.

By stripping the lines at the beginning of the function, all previous padding is removed.
This effectively means that text that was previously right or center justified is automatically
first converted to default left justification, after which any other type of justification can
be applied without issues.

The main body of the module can be used to easily apply the function to files. First the path
to a text file is requested, then a type of justification. The given text file is read, the text
is justified according to the chosen justification and the result is written to a file that has
the same path but with '_justified' appended before the file extension.

**Output of test run**

This is the output of a test run on the enclosed file 'example.txt':

    $ python3
    >>> from justifytext import justify_text
    >>> with open('example.txt', 'r') as fil:
    ...     text = fil.read()
    ... 
    >>> print(text)
    Short line 1
    Short line 2
    A bit longer line 1
    Short line 3
    A bit longer line 2
    This is very long line number one
    This is very long line number two
    A bit longer line 3
    This is very long line number three

    >>> text = justify_text(text, 'center');print(text)  ## Left justify to center justify.
               Short line 1            
               Short line 2            
            A bit longer line 1        
               Short line 3            
            A bit longer line 2        
     This is very long line number one 
     This is very long line number two 
            A bit longer line 3        
    This is very long line number three
                                       
    >>> text = justify_text(text, 'right');print(text)  ## Center justify to right justify.
                           Short line 1
                           Short line 2
                    A bit longer line 1
                           Short line 3
                    A bit longer line 2
      This is very long line number one
      This is very long line number two
                    A bit longer line 3
    This is very long line number three
                                       
    >>> text = justify_text(text, 'left');print(text)  ## Right justify to left justify.
    Short line 1                       
    Short line 2                       
    A bit longer line 1                
    Short line 3                       
    A bit longer line 2                
    This is very long line number one  
    This is very long line number two  
    A bit longer line 3                
    This is very long line number three
                                       

Challenge complete, and then some!
