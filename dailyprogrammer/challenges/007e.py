#!/usr/bin/python3
"""
Challenge information
---------------------

| **Challenge name:** `Morse Code <http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/>`_
| **Challenge number:** 7
| **Difficulty:** Easy
| **Submission date:** 2012-02-15
| **Status:** Complete

Challenge description
---------------------

Write a program that can translate Morse code in the format of `...---...`. A space will
be placed between letters and a slash will be placed between words. This is your Morse
to translate::

    .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. /
    --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. .
    -. --. . ... / - --- -.. .- -.--

For bonus, add the capability of going from a string to Morse code.
Super-bonus if your program can flash or beep the Morse.

Challenge module contents
-------------------------
"""

from plugins.morse import Beep, MorseConvention


def run():
    """Execute the challenges.007e module."""
    # Settings for the strange 'Reddit' Morse code convention that was pulled out of
    # someone's ass for this challenge.
    ls = ' '  ## Spacing between letters in a Morse sequence.
    ws = ' / '  ## Spacing between words in a Morse sequence.
    charmap = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
    }
    beepmap = {
        ' ': Beep(pitch=200, btime=200, stime=250),
        '/': Beep(pitch=200, btime=200, stime=250),
        '.': Beep(pitch=400, btime=200, stime=250),
        '-': Beep(pitch=400, btime=600, stime=650),
    }
    morse_reddit = MorseConvention(ls, ws, charmap, beepmap)

    # Decode the challenge sequence.
    sequence = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
    msg = morse_reddit.decode(sequence)
    print("\nChallenge Morse sequence:\n{}".format(sequence))
    print("decodes to:\n{}\n".format(msg))

    # Ask for a message to encode and whether or not to beep it.
    msg = input("Message to encode? > ").upper()
    sequence = morse_reddit.encode(msg)
    print("Resulting Morse sequence:\n{}\n".format(sequence))
    if input("Beep this (y/n)? ").lower()[0] == 'y':
        morse_reddit.beep(sequence)
