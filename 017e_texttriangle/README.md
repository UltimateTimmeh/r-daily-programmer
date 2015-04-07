## Information

**Challenge name:** [Text triangle](http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/)  
**Challenge number:** 17  
**Difficulty:** Easy  
**Submission date:** 2012-03-04  
**Status:** Complete

## Description

Write an application which will print a triangle of stars of user-specified height, with each
line having twice as many stars as the last. sample output:

    @
    @@
    @@@@

**Hint**: In many languages, the '+' sign concatenates strings.  
**Bonus features**: print the triangle in reverse, print the triangle right justified.

## Development notes

### 2015-04-07, 16:24

**Description**

For this challenge I created a class `TextTriangle` which, based on a set of attributes, can
draw a text triangle in a specific way. The attributes of the `TextTriangle` are the following:

- `char` - *Character* - The character that will be used to print the triangle.
- `levels` - *Amount of levels* - The amount of levels in the triangle.
- `start` - *Number of elements at start* - See formula for amount of elements in each level.
- `rm` - *Recursive multiplication factor* - See formula for amount of elements in each level.
- `lm` - *Level multiplication factor* - See formula for amount of elements in each level.
- `add` - *Addition factor* - See formula for the amount of elements in each level.
- `order` - *Order of printing* - The order in which the levels will be printed ('ascending' or 'descending').
- `align` - *Printing alignment* - The alignment of the printed triangle (left, center, right).

**Formula for amount of elements in each level**:

    nelems[i] = nelems[i-1]*rm + i*lm + add
    ## i goes from 0 to levels
    ## for i = 0: nelems = start

**Output of test run**

Following is an example run that showcases the requirements for this challenge. First, the behavior
of the main challenge is showcased (i.e. 'each level has twice as many elements as the last'). Next,
the bonus features are showcased in a single example (i.e. a 'reverse' triangle with 'right'
justification). Note that the default 'height' of 5 levels is used. Finally, a nicely centered
triangle with many levels, kind of resembling a Christmas tree, is showcased.

    $ python3
    >>> from texttriangle import TextTriangle
    >>> char='@'; start=1; rm=2; lm=0; add=0
    >>> triangle = TextTriangle(char=char, start=start, rm=rm, lm=lm, add=add)
    >>> triangle.draw()
    @
    @@
    @@@@
    @@@@@@@@
    @@@@@@@@@@@@@@@@
    >>> triangle.order='descending'; triangle.align='right'
    >>> triangle.draw()
    @@@@@@@@@@@@@@@@
            @@@@@@@@
                @@@@
                  @@
                   @
    >>> triangle.order='ascending'; triangle.align='center'
    >>> triangle.levels=20; triangle.rm=1; triangle.add=2; triangle.char='^'
    >>> triangle.draw()
                       ^
                      ^^^
                     ^^^^^
                    ^^^^^^^
                   ^^^^^^^^^
                  ^^^^^^^^^^^
                 ^^^^^^^^^^^^^
                ^^^^^^^^^^^^^^^
               ^^^^^^^^^^^^^^^^^
              ^^^^^^^^^^^^^^^^^^^
             ^^^^^^^^^^^^^^^^^^^^^
            ^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^^^^^
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Challenge complete!
