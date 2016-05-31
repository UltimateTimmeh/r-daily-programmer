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

    $ python3 dailyprogrammer.py execute 007e

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

Imported plugins
----------------

| None

Module contents
---------------
"""

import subprocess
import time

from plugins import utils


class Beep(object):
    """A class representing a beeping sound.

    A beep is characterized by a pitch and beep time. There is also a sleep time,
    which allows for a pause in code execution while the beep is sounding.

    :param int pitch: beeping pitch in Hertz (default 400)
    :param int btime: beeping time in milliseconds (default 200)
    :param int stime: sleep time in milliseconds (default 250)

    Example::

        >>> Beep(200, 50, 0).play()
    """


    def __init__(self, pitch=400, btime=200, stime=250):
        """Create a new beep."""
        self.pitch = pitch
        self.btime = btime
        self.stime = stime


    def play(self):
        """Play the beep by printing a system bell character.

        For an example that uses this method, see :func:`challenges.007e.Beep`.
        """
        cmd = 'xset b 100 {} {}'.format(self.pitch, self.btime).split()
        subprocess.call(cmd)
        print('\a')
        time.sleep(self.stime/1000.)


class MorseConvention(object):
    """A class representing a Morse code convention.

    A Morse code convention is characterized by a character map (defining the relationship
    between letters and Morse sequences), a letter spacing sequence and a word spacing
    sequence. Optionally, if you want to beep Morse sequences, you can provide a beep
    map (defining beeps to be played for each possible Morse character).

    :param str ls: letter spacing sequence
    :param str ws: word spacing sequence
    :param charmap: dictionary mapping letters to Morse code sequences
    :type charmap: dict(str: str, ...)
    :param beepmap: optional dictionary mapping Morse code characters to beeps (default None)
    :type beepmap: None or dict(str: Beep, ...)

    Example::

        >>> morse_itu = MorseConvention(' '*3, ' '*7, {'A': '. ...', 'B': '... . . .'})
        >>> morse_itu.encode('ABBA')
        '. ...   ... . . .   ... . . .   . ...'
        >>> morse_itu.decode('... . . .   . ...       ... . . .   . ...')
        'BA BA'
    """


    def __init__(self, ls, ws, charmap, beepmap=None):
        """Create a new Morse code convention."""
        self.ls = ls
        self.ws = ws
        self.charmap = charmap
        self.beepmap = beepmap


    def is_valid_morse(self, morse):
        """Check if a Morse code sequence is valid in the Morse code convention.

        A Morse sequence is valid if all characters in the sequence are one of the Morse code
        characters defined in the letter spacing, word spacing or character map. In other words:
        this method only checks if there are invalid characters in the sequence, not if it can
        be decoded!

        :param str morse: Morse sequence to be validated
        :return: True if the sequence is valid, False otherwise
        :rtype: bool

        Example::

            >>> morse_itu = MorseConvention(' '*3, ' '*7, {'A': '. ...'})
            >>> morse_itu.is_valid_morse('.-')
            False
            >>> morse_itu.is_valid_morse('. . .')
            True
        """
        valid_chars = set(''.join(list(self.charmap.values())) + self.ls + self.ws)
        return all([char in valid_chars for char in morse])


    def encode(self, msg):
        """Encode a message to Morse code.

        Note that message characters which are not in the character map will be silently ignored.

        :param str msg: message to encode
        :return: encoded Morse sequence
        :rtype: str

        For an example that uses this method, see :func:`challenges.007e.MorseConvention`.
        """
        morse = ''
        for msg_word in msg.split():
            morse_word = ''
            for msg_char in msg_word:
                if msg_char in self.charmap:
                    morse_word += self.charmap[msg_char] + self.ls
            morse += morse_word.strip(self.ls) + self.ws
        return morse.strip(self.ws)


    def decode(self, morse):
        """Decode a Morse code sequence.

        Note that Morse letter sequences which are not in the character map will be silently
        ignored.

        :param str morse: Morse sequence to decode
        :return: decoded message
        :rtype: str
        :raise: ValueError if the passed Morse sequence is invalid

        For an example that uses this method, see :func:`challenges.007e.MorseConvention`.
        """
        if not self.is_valid_morse(morse):
            raise ValueError("Received invalid Morse code sequence to decode.")
        charmap_rev = {value: key for key, value in self.charmap.items()}
        msg = ''
        for morse_word in morse.split(self.ws):
            msg_word = ''
            for morse_char in morse_word.split(self.ls):
                if morse_char in charmap_rev:
                    msg_word += charmap_rev[morse_char]
            msg += msg_word + ' '
        return msg.strip()


    def beep(self, morse):
        """Beep a Morse code sequence.

        :param str morse: Morse sequence to beep
        :raise: ValueError if no beep map is defined in the Morse code convention
        :raise: ValueError if the passed Morse sequence is invalid

        Example::

            >>> beep_space = Beep(200, 200, 250)
            >>> beep_dot = Beep(400, 200, 250)
            >>> beepmap = {' ': beep_space, '.': beep_dot}
            >>> charmap = {'A': '. ...'}
            >>> morse_itu = MorseConvention(' '*3, ' '*7, charmap, beepmap)
            >>> morse_itu.beep('. ...')
        """
        if self.beepmap is None:
            raise(ValueError("No beep map defined in Morse code convention."))
        if not self.is_valid_morse(morse):
            raise ValueError("Received invalid Morse code sequence to beep.")
        for morse_char in morse:
            self.beepmap[morse_char].play()


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
    sequence = (".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. /"
                " --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. "
                ". -. --. . ... / - --- -.. .- -.--")
    msg = morse_reddit.decode(sequence)
    print("\nChallenge Morse sequence:\n{}".format(sequence))
    print("decodes to:\n{}\n".format(msg))

    # Ask for a message to encode and whether or not to beep it.
    msg = utils.get_input("Message to encode? > ").upper()
    sequence = morse_reddit.encode(msg)
    print("Resulting Morse sequence:\n{}\n".format(sequence))
    if utils.get_input("Beep this (y/n)? ").lower()[0] == 'y':
        morse_reddit.beep(sequence)

