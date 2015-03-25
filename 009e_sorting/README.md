## Information

**Challenge name:** [Sorting](http://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/)  
**Challenge number:** 9  
**Difficulty:** Easy  
**Submission date:** 2012-02-17  
**Status:** In progress

## Description

Write a program that will allow the user to input digits, and arrange them in numerical order.  
For extra credit, have it also arrange strings in alphabetical order

## Development notes

### 2015-03-12, 07:52

Sounds like a great opportunity to educate myself about sorting algorithms. I vagely remember their
existence from my first year of university, but I never really went deep into the subject. This
challenge will allow me to implement several algorithms, and perhaps even test which ones are
more efficient for smaller lists and which ones are more efficient for larger lists.

### 2015-03-25, 08:23

After a long time being busy at work and delving into sorting algorithms when I had some spare time,
I finally managed to finish the main part of this challenge. I have included the following sorting
algorithms, mostly with help from information found on Wikipedia. :

- Insertion
- Selection
- Merge
- Quick
- Heap
- Bubble
- Shell
- Comb

All of the algorithms have a 'verbose' option, which makes them print everything that is going on
in a way that could help the user understand the algorithm by being able to follow the different
steps for an example. This is hardcoded to work on a list containing 10 elements. That number appears
to be not too big and not too small for educational purposes. This functionality immediately also
'tests' the code, by checking if the resulting sorted list is what it should be. The outcome of the
test is printed at the end. Launching an example for an algorithm in verbose mode can be done with
the following command:

    $ python3.4 sorting.py test <algorithm name>

A second functionality compares each algorithm for several list sizes. First, a number of lists of
various size are created and shuffled. Then, each algorithm is fed a copy of each list (in non-verbose
mode), and the execution time is measured. Afterwards, the execution time for each algorithm and each
list size is presented in a nicely formatted table. This functionality can be executed with the
following command:

    $ python3.4 sorting.py compare

If the terminal in which you are executing this command is not big enough to view the table in a
nicely formatted way, you can also have the output of the script printed to a file by adding
`> output.txt` to the previous command.

I have not (yet) performed the extra credit, which is sorting a list of strings in alphabetical order.
If what I have read so far is correct, I would first need to research lexicographical sorting
algorithms. I might do this in the future, as this topic is really interesting, but I don't have time
for this quite yet.
