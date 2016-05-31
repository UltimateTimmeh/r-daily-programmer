#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/srowj/4252012_challenge_44_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/044e.py

| **Challenge name:** Split Sentences (reddit_, source_)
| **Challenge number:** 44
| **Difficulty:** Easy
| **Submission date:** 2012-04-25
| **Status:** Complete

Description
-----------

Write a program that divides up some input text into sentences and then determines which sentence in
the input has the most words. Print out the sentence with the most words and the number of words
that are in it. Optionally, also print out all words in that sentence that are longer than 4
characters.

Sentences can end in periods, exclamation points and question marks, but not colons or semi-colons.

If you need something to input, try Shylock's famous speech from Shakespeare's *The Merchant of
Venice*::

    If it will feed nothing else, it will feed my revenge. He hath disgrac'd me and hind'red me half
    a million; laugh'd at my losses, mock'd at my gains, scorned my nation, thwarted my bargains,
    cooled my friends, heated mine enemies. And what's his reason? I am a Jew. Hath not a Jew eyes?
    Hath not a Jew hands, organs, dimensions, senses, affections, passions, fed with the same food,
    hurt with the same weapons, subject to the same diseases, healed by the same means, warmed and
    cooled by the same winter and summer, as a Christian is? If you prick us, do we not bleed? If
    you tickle us, do we not laugh? If you poison us, do we not die? And if you wrong us, shall we
    not revenge? If we are like you in the rest, we will resemble you in that. If a Jew wrong a
    Christian, what is his humility? Revenge. If a Christian wrong a Jew, what should his sufferance
    be by Christian example? Why, revenge. The villainy you teach me I will execute; and it shall go
    hard but I will better the instruction.

Thanks to `/u/frenulem <https://www.reddit.com/user/frenulem>`_ for submitting this problem to
`/r/dailyprogrammer_ideas <https://www.reddit.com/r/dailyprogrammer_ideas>`_! Do you have a problem
that you think would be good for this subreddit? Head on over there and suggest it!

Example run
-----------

::

    This is the complete input:
    If it will feed nothing else, it will feed my revenge. He hath disgrac'd me and hind'red me half
    a million; laugh'd at my losses, mock'd at my gains, scorned my nation, thwarted my bargains,
    cooled my friends, heated mine enemies. And what's his reason? I am a Jew. Hath not a Jew eyes?
    Hath not a Jew hands, organs, dimensions, senses, affections, passions, fed with the same food,
    hurt with the same weapons, subject to the same diseases, healed by the same means, warmed and
    cooled by the same winter and summer, as a Christian is? If you prick us, do we not bleed? If
    you tickle us, do we not laugh? If you poison us, do we not die? And if you wrong us, shall we
    not revenge? If we are like you in the rest, we will resemble you in that. If a Jew wrong a
    Christian, what is his humility? Revenge. If a Christian wrong a Jew, what should his sufferance
    be by Christian example? Why, revenge. The villainy you teach me I will execute; and it shall go
    hard but I will better the instruction.

    Longest sentence in the input, with 43 words:
    Hath not a Jew hands, organs, dimensions, senses, affections, passions, fed with the same food,
    hurt with the same weapons, subject to the same diseases, healed by the same means, warmed and
    cooled by the same winter and summer, as a Christian is

    Words in this sentence longer than four characters:
    ['hands,', 'organs,', 'dimensions,', 'senses,', 'affections,', 'passions,', 'food,', 'weapons,',
    'subject', 'diseases,', 'healed', 'means,', 'warmed', 'cooled', 'winter', 'summer,',
    'Christian']

Imported plugins
----------------

| :mod:`plugins.enhancedstring`

Module contents
---------------
"""

import os

import plugins.config as cfg
from plugins import enhancedstring as es


def run():
    """Execute the challenges.044e module."""
    # Process the input.
    input_fp = os.path.join(cfg.input_dir, '044e_example_input.txt')
    with open(input_fp, 'r') as input_file:
        input = input_file.read()
    input = input.replace('\n', ' ')  ## newline characters become spaces
    input = es.EnhancedString(input)
    delimiters = '. ! ?'.split()
    sentences = [sentence.strip() for sentence in input.split(delimiters)]
    longest = max(sentences, key=lambda x: x.nwords)
    longwords = [word for word in longest.words if len(word) > 4]
    # Print the results.
    print("This is the complete input:")
    print(input, end='\n\n')
    print("Longest sentence in the input, with", longest.nwords, "words:")
    print(longest, end='\n\n')
    print("Words in this sentence longer than four characters:")
    print(longwords)

