#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qlwrc/372012_challenge_19_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/019e.py

| **Challenge name:**  Character Count (reddit_, source_)
| **Challenge number:** 19
| **Difficulty:** Easy
| **Submission date:** 2012-03-07
| **Status:** Complete

Description
-----------

Challenge #19 will use `The Adventures of Sherlock Holmes <http://www.gutenberg.org/cache/epub/1661/pg1661.txt>`_
from `Project Gutenberg <http://www.gutenberg.org>`_.

Write a program that counts the number of alphanumeric characters there are in The Adventures of
Sherlock Holmes. Exclude the Project Gutenberg header and footer, book title, story titles, and
chapters. Post your code and the alphanumeric character count.

Example run
-----------

.. warning:: This solution to the challenge downloads the book's text file from the Gutenberg
             website every time it is executed. After several runs it's possible it suddenly
             starts failing. That's because the Gutenberg website notices a lot of download
             requests coming from your IP address, thinks you're a bot (which is half correct)
             and redirects the text file to a Captcha page. To continue, you should go to the
             URL of the book in a browser and solve the captcha.

::

    $ python3 dailyprogrammer.py execute 019e

    =====
    LINES
    =====

    Line count
    ''''''''''
    Analysis started on line 57 and stopped on line 12681
    Amount of empty lines: 2564
    Amount of skipped, non-empty lines: 15
    Amount of counted lines: 10045
    Total amount of lines: 12624
    Expected amount of lines: 12624

    Skipped, non-empty lines
    ''''''''''''''''''''''''
    ADVENTURE I. A SCANDAL IN BOHEMIA
    I.
    II.
    III.
    ADVENTURE II. THE RED-HEADED LEAGUE
    ADVENTURE III. A CASE OF IDENTITY
    ADVENTURE IV. THE BOSCOMBE VALLEY MYSTERY
    ADVENTURE V. THE FIVE ORANGE PIPS
    ADVENTURE VI. THE MAN WITH THE TWISTED LIP
    VII. THE ADVENTURE OF THE BLUE CARBUNCLE
    VIII. THE ADVENTURE OF THE SPECKLED BAND
    IX. THE ADVENTURE OF THE ENGINEER'S THUMB
    X. THE ADVENTURE OF THE NOBLE BACHELOR
    XI. THE ADVENTURE OF THE BERYL CORONET
    XII. THE ADVENTURE OF THE COPPER BEECHES

    ================
    CHARACTER COUNTS
    ================

    Individual characters
    '''''''''''''''''''''
    .: 6180
    (: 5
    1: 63
    6: 14
    j: 338
    ;: 202
    ': 1492
    c: 10166
    W: 756
    é: 12
    t: 37823
    ,: 7639
    O: 290
    J: 114
    x: 541
    K: 76
    8: 37
    o: 33185
    Z: 2
    g: 7730
    ?: 737
    U: 28
    r: 24290
    y: 8970
    :: 60
    L: 275
    -: 1141
    E: 158
    f: 8778
    7: 18
    3: 15
    i: 26357
    F: 180
    P: 176
    D: 192
    G: 151
    Y: 449
     : 94526
    0: 82
    â: 1
    q: 406
    ": 5093
    s: 26425
    S: 747
    m: 11052
    e: 52806
    B: 461
    à: 1
    T: 1087
    A: 724
    k: 3464
    4: 22
    /: 1
    R: 177
    u: 13060
    v: 4360
    h: 27780
    p: 6647
    n: 28362
    5: 16
    a: 34362
    d: 18335
    H: 1217
    N: 277
    &: 5
    V: 59
    M: 724
    I: 3722
    !: 345
    è: 1
    C: 311
    l: 16845
    ): 5
    9: 13
    z: 147
    w: 10506
    Q: 20
    b: 5878
    2: 35

    Groups of characters
    ''''''''''''''''''''
    Amount of alphanumeric characters: 431316
    Total amount of characters (without spaces): 454221
    Total amount of characters (including spaces): 548747

Module contents
---------------
"""

from urllib.request import urlopen

from plugins.enhancedstring import EnhancedString


def format_header(title, above='', below=''):
    """Format a title as a header with lines.

    :param str title: title of the header
    :param str above: character used for the line above the title (default '')
    :param str below: character used for the line below tht title (default '')
    :return: the header
    :rtype: str

    Example::

        >>> header = format_header('MAIN SECTION', above='=', below='=')
        >>> print(header)
        ============
        MAIN SECTION
        ============
    """
    header = [above*len(title), title, below*len(title)]
    return '\n'.join([line for line in header if line != ''])


def run():
    """Execute the challenges.019e module."""
    # Load the text file from the URL and split in lines.
    start = 57
    end = 12681
    target_url = 'http://www.gutenberg.org/cache/epub/1661/pg1661.txt'
    book = urlopen(target_url).read().decode('utf-8')
    lines = book.split('\r\n')

    # Go over all lines, excluding the Gutenberg header and footer, book title
    # and chapter index.
    counts = {}
    nlines_empty = 0
    lines_skipped = []
    nlines_counted = 0
    for line in lines[start:end]:
        if line == '':  ## Skip empty lines.
            nlines_empty += 1
        elif line == line.upper() and line[0] in 'IVXA':  ## Allcaps lines that start with one of 'IVXA' should be story or chapter titles.
            lines_skipped.append(line)
        else:  ## If none of the previous, then the line should be counted.
            nlines_counted += 1
            counts = EnhancedString(line).count_characters(counts=counts)

    # Crunch the numbers.
    ## Line count
    nlines_skipped = len(lines_skipped)
    nlines_total = nlines_empty + nlines_skipped + nlines_counted
    nlines_expected = end - start

    ## Character counts
    nchars_an = sum([counts[char] for char in counts if char.isalnum()])
    nchars_nospace = sum([counts[char] for char in counts if char != ' '])
    nchars_all = sum([counts[char] for char in counts])

    # Print a report.
    print('\n' + format_header("LINES", above='=', below='='))
    print('\n' + format_header("Line count", below="'"))
    print("Analysis started on line {} and stopped on line {}".format(start, end))
    print("Amount of empty lines: {}".format(nlines_empty))
    print("Amount of skipped, non-empty lines: {}".format(nlines_skipped))
    print("Amount of counted lines: {}".format(nlines_counted))
    print("Total amount of lines: {}".format(nlines_total))
    print("Expected amount of lines: {}".format(nlines_expected))
    print('\n' + format_header("Skipped, non-empty lines", below="'"))
    print('\n'.join(lines_skipped))
    print('\n' + format_header("CHARACTER COUNTS", above='=', below='='))
    print('\n' + format_header("Individual characters", below="'"))
    print('\n'.join(['{}: {}'.format(char, nr) for char, nr in counts.items()]))
    print('\n' + format_header("Groups of characters", below="'"))
    print("Amount of alphanumeric characters: {}".format(nchars_an))
    print("Total amount of characters (without spaces): {}".format(nchars_nospace))
    print("Total amount of characters (including spaces): {}".format(nchars_all))

