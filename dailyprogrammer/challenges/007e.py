#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/007e.py

| **Challenge name:** Morse Code (reddit_, source_)
| **Challenge number:** 7
| **Difficulty:** Easy
| **Submission date:** 2012-02-15
| **Status:** Complete

Description
-----------

Write a program that can translate Morse code in the format of `...---...`. A space will
be placed between letters and a slash will be placed between words. This is your Morse
to translate::

    .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. /
    --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. .
    -. --. . ... / - --- -.. .- -.--

For bonus, add the capability of going from a string to Morse code.
Super-bonus if your program can flash or beep the Morse.

Example run
-----------

::

    $ python3 dailyprogrammer.py 007e

    Challenge Morse sequence:
    .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--
    decodes to:
    HELLO DAILY PROGRAMMER GOOD LUCK ON THE CHALLENGES TODAY

    Message to encode? > WHAT HATH GOD WROUGHT
    Resulting Morse sequence:
    .-- .... .- - / .... .- - .... / --. --- -.. / .-- .-. --- ..- --. .... -

    Beep this (y/n)? n

Extra credit
------------

Beeping the Morse sequences is achieved by printing the system bell character ``\a`` in the
terminal. I chose this option because it is supposed to be OS independent. First, however, I
had to find a way to allow the system bell in the terminal (Debian Jessie, can't help you if
you're a Windows user), since it was apparently off by default. This is what I had to do to
set it to allow the system bell to be played in the terminal, but keep it off by default:

1. Apparently the setting for allowing the system bell in the xfce4 terminal is a 'hidden' setting.
   The only way to change this is by manually editing the terminal's configuration file.
2. Open (or create, if it does not yet exist) the file ``/home/user/.config/xfce4/terminal/terminalrc``
   in a text editor.
3. Edit the file so it contains at least the following::

    [Configuration]
    MiscBell=TRUE

.. warning:: For me, creating the terminal configuration file reset all terminal settings
   (background color changed from white to black, for example), so I had to change the preferences
   back to what they were before. Doing this did not remove the system bell setting from the
   configuration file.

4. If you log out and back in, the change should have taken effect. You can test by simply pressing
   backspace in the terminal, or by launching Python in the terminal and printing the ``\a``
   character.
5. If it does not work, then perhaps the bell is deactivated system-wide by default. You can
   check this with the command ``xset q | grep bell`` in a terminal. If 'percent' (the volume)
   is zero, then the bell is off. You can turn it on with the command ``xset b on``. Then it
   should work. If it doesn't, then I can't help you any further.
6. If the bell is activated system-wide by default, then allowing the bell in the terminal
   can get annoying. Because of this, the bell should be automatically switched off when
   opening a terminal. You can do this by adding the following lines to the ``/home/user/.bashrc``
   file::

    # Turn off system bell
    if [ -n "$DISPLAY" ]; then
      xset b off
    fi

7. If you open a terminal now, the bell should be allowed, but it will be off by default. You
   can always check the settings of the bell with the command ``xset q | grep bell``, turn it
   on with ``xset b on`` and test if it works by printing the ``\a`` character in Python. To
   deactivate the bell, use the command ``xset b off``.

Module contents
---------------
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
