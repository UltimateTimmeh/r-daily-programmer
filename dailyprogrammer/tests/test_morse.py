#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_morse.py

Unit tests for module :mod:`plugins.morse` (source_).
"""

import unittest

from plugins import morse


class TestBeep(unittest.TestCase):
    """Unit tests for class :func:`plugins.morse.Beep`."""


    def test___init__(self):
        """Test method :meth:`plugins.morse.Beep.__init__`

        **Tested:**

        - The attributes of a beep are correct after initialization.
        """
        beep = morse.Beep(400, 200, 250)
        self.assertEqual(beep.pitch, 400)
        self.assertEqual(beep.btime, 200)
        self.assertEqual(beep.stime, 250)


class TestMorseConvention(unittest.TestCase):
    """Unit tests for class :func:`plugins.morse.MorseConvention`."""


    def test___init__(self):
        """Test method :meth:`plugins.morse.MorseConvention.__init__`

        **Tested:**

        - The attributes of a Morse convention are correct after initialization.
        """
        morseconv = morse.MorseConvention(' '*3, ' '*7, {'A': '. ...'})
        self.assertEqual(morseconv.ls, ' '*3)
        self.assertEqual(morseconv.ws, ' '*7)
        self.assertEqual(morseconv.charmap, {'A': '. ...'})
        self.assertEqual(morseconv.beepmap, None)


    def test_is_valid_morse(self):
        """Test method :meth:`plugins.morse.MorseConvention.is_valid_morse`

        **Tested:**

        - True is returned when the passed Morse sequence is valid.
        - False is returned when the passed Morse sequence is invalid.
        """
        morseconv = morse.MorseConvention(' '*3, ' '*7, {'A': '. ...'})
        self.assertTrue(morseconv.is_valid_morse('. . .'))
        self.assertFalse(morseconv.is_valid_morse('.-'))


    def test_encode(self):
        """Test method :meth:`plugins.morse.MorseConvention.encode`

        **Tested:**

        - The returned encoded Morse sequence is correct.
        """
        morseconv = morse.MorseConvention(' '*3, ' '*7, {'A': '. ...', 'B': '... . . .'})
        self.assertEqual(morseconv.encode('ABBA'), '. ...   ... . . .   ... . . .   . ...')


    def test_decode(self):
        """Test method :meth:`plugins.morse.MorseConvention.decode`

        **Tested:**

        - The returned decoded message is correct.
        - A ValueError is raised when the passed Morse sequence is invalid.
        """
        morseconv = morse.MorseConvention(' '*3, ' '*7, {'A': '. ...', 'B': '... . . .'})
        sequence = '... . . .   . ...       ... . . .   . ...'
        expected = 'BA BA'
        self.assertEqual(morseconv.decode(sequence), expected)
        with self.assertRaises(ValueError):
            morseconv.decode('.-')


    def test_beep(self):
        """Test method :meth:`plugins.morse.MorseConvention.beep`

        **Tested:**

        - A ValueError is raised when no beepmap is specified.
        - A ValueError is raised when the passed Morse sequence is invalid.
        """
        morseconv = morse.MorseConvention(' '*3, ' '*7, {'A': '. ...'})
        with self.assertRaises(ValueError):
            morseconv.beep('.-')
        morseconv.beepmap = {' ': morse.Beep(), '.': morse.Beep()}
        with self.assertRaises(ValueError):
            morseconv.beep('.-')


if __name__ == '__main__':
    unittest.main()
