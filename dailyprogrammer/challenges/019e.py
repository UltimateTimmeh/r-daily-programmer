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

.. note:: The challenge is not clear about the definition of "alphanumeric characters". Does this
          include punctuation? Does it include letters with accents? Does it include spaces?
          Therefore, my output produces three numbers: the character count for the 62 pure
          alphanumeric characters (a - z, A - Z and 0 - 9), the total character count excluding
          spaces, and the total character count including spaces.

.. warning:: This solution to the challenge downloads the book's text file from the Gutenberg
             website every time it is executed. After several runs it's possible it suddenly
             starts failing. That's because the Gutenberg website notices a lot of download
             requests coming from your IP address, thinks you're a bot (which is half correct)
             and redirects the text file to a Captcha page. To continue, you should go to the
             URL of the book in a browser and solve the captcha.

::

    $ python3 dailyprogrammer.py 019e

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

    ===============
    CHARACTER COUNT
    ===============

    Individual characters
    '''''''''''''''''''''
    6: 14
    ': 1492
    I: 3722
    ;: 202
    W: 756
    S: 747
    .: 6180
    D: 192
    G: 151
    2: 35
    ": 5093
    â: 1
    5: 16
    y: 8970
    U: 28
    v: 4360
    c: 10166
    9: 13
    s: 26425
    p: 6647
    Y: 449
    b: 5878
     : 94526
    A: 724
    ?: 737
    0: 82
    /: 1
    w: 10506
    M: 724
    N: 277
    3: 15
    k: 3464
    ): 5
    m: 11052
    !: 345
    d: 18335
    7: 18
    :: 60
    4: 22
    8: 37
    J: 114
    V: 59
    (: 5
    &: 5
    n: 28362
    f: 8778
    e: 52806
    a: 34362
    à: 1
    P: 176
    C: 311
    j: 338
    u: 13060
    h: 27780
    L: 275
    é: 12
    o: 33185
    F: 180
    -: 1141
    ,: 7639
    O: 290
    i: 26357
    l: 16845
    T: 1087
    x: 541
    K: 76
    1: 63
    Z: 2
    z: 147
    Q: 20
    R: 177
    E: 158
    g: 7730
    r: 24290
    t: 37823
    è: 1
    B: 461
    H: 1217
    q: 406

    Groups of characters
    ''''''''''''''''''''
    Amount of purely alphanumeric characters: 431301
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
    chars_pure = 'abcdefghijklmnopqrstuvwxyz'
    chars_pure += chars_pure.upper() + '0123456789'
    start = 57
    end = 12681
    target_url = 'http://www.gutenberg.org/cache/epub/1661/pg1661.txt'
    book = urlopen(target_url).read().decode('utf-8')
    lines = book.split('\r\n')

    # Go over all lines, excluding the Gutenberg header and footer, book title
    # and chapter index.
    count = {}
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
            EnhancedString(line).count_characters(count)

    # Crunch the numbers.
    ## Line count
    nlines_skipped = len(lines_skipped)
    nlines_total = nlines_empty + nlines_skipped + nlines_counted
    nlines_expected = end - start

    ## Character count
    nchars_pure = sum([count[char] for char in count if char in chars_pure])
    nchars_nospace = sum([count[char] for char in count if char != ' '])
    nchars_all = sum([count[char] for char in count])

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
    print('\n' + format_header("CHARACTER COUNT", above='=', below='='))
    print('\n' + format_header("Individual characters", below="'"))
    print('\n'.join(['{}: {}'.format(char, nr) for char, nr in count.items()]))
    print('\n' + format_header("Groups of characters", below="'"))
    print("Amount of purely alphanumeric characters: {}".format(nchars_pure))
    print("Total amount of characters (without spaces): {}".format(nchars_nospace))
    print("Total amount of characters (including spaces): {}".format(nchars_all))

