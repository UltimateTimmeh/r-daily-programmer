#!/usr/bin/python3
"""
Encode, decode and beep messages in Morse code.
"""

import subprocess
import time


class Beep(object):
    """A class representing a beeping sound.

    A beep is characterized by a pitch and beep time. There is also a sleep time,
    which allows for a pause in code execution while the beep is sounding.

    :param int pitch: beeping pitch in Hertz (default 400)
    :param int btime: beeping time in milliseconds (default 200)
    :param int stime: sleep time in milliseconds (default 250)

    Example::

        >>> from morse import Beep
        >>> Beep(200, 50, 0).play()
    """


    def __init__(self, pitch=400, btime=200, stime=250):
        """Create a new beep."""
        self.pitch = pitch
        self.btime = btime
        self.stime = stime


    def play(self):
        """Play the beep by printing a system bell character.

        For an example that uses this method, see :func:`plugins.morse.Beep`
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

        >>> from morse import MorseConvention
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

            >>> from morse import MorseConvention
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

        For an example that uses this method, see :func:`plugins.morse.MorseConvention`
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

        For an example that uses this method, see :func:`plugins.morse.MorseConvention`"""
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

            >>> from morse import Beep, MorseConvention
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
