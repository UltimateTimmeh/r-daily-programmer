#!/usr/bin/python3
"""
Application with text-based menus to encode, beep and decode Morse code. Use
the menu to select the desired function and enter the text to encode (and/or
beep) or Morse to decode.
"""

import os
import subprocess
import sys
import time

# Import module from previous challenge.
sys_path = list(sys.path)
module_dir = os.path.abspath('../002e_calculator')
sys.path.insert(0, module_dir)
from textmenu import TextMenu
sys.path[:] = sys_path

# Standard Morse code conventions included in the morsecode package.
convdir = os.path.split(__file__)[0]
conventions = {
    'ITU': os.path.join(convdir, 'morse_itu.mrs'),
    'REDDIT': os.path.join(convdir, 'morse_reddit.mrs'),
    }


# Some global Morse code functions.
def valid_morse(morse):
    """Check if a string of Morse code is valid.

    A Morse code string is valid if it only contains blanks and dots.
    """
    return all([cc in [' ', '.'] for cc in morse])


def beep_morse(morse, bp=100, bt=200, dp=400, dt=200):
    """Beep the passed string of Morse code."""
    if not valid_morse(morse):
        print("Invalid Morse in Morse code string to beep.")
        return

    cmd = 'xset b 100 {} {}'
    for cc in morse:
        if cc == ' ':
            subprocess.call(cmd.format(bp,bt).split())
            print('\a')
            time.sleep(bt/1000.)
        elif cc == '.':
            subprocess.call(cmd.format(dp,dt).split())
            print('.\a')
            time.sleep(dt/1000.)
    subprocess.call('xset b off'.split())


# Morse code convention class.
class MorseConvention(object):
    """A class containing a Morse encoding convention."""


    def __init__(self, convention='ITU'):
        """Initialize the Morse object."""
        if os.path.isfile(convention):
            self.load(convention)
        elif convention in conventions:
            self.set(convention)
        else:
            error = "'{}' is not a standard Morse code convention or a valid "
            error += "path to a custom Morse code convention file!"
            raise ValueError(error.format(convention))


    def __str__(self):
        """Format Morse object as a string."""
        title = "Morse code convention '{}':".format(self.codename)
        line = "="*len(title)
        txt = [line,title,line]
        keys_sorted = list(self.text2morse.keys())
        keys_sorted.sort()
        for key in keys_sorted:
            txt.append("'{}' = '{}'".format(key, self.text2morse[key]))
        txt.append(line)
        txt = '\n' + '\n'.join(txt)
        return txt


    def set(self, convention):
        """Set the chosen standard convention."""
        if convention in conventions:
            self.load(conventions[convention])
        else:
            error = "'{}' is not a standard Morse code convention!"
            raise ValueError(error.format(convention))


    def load(self, fn):
        """Load a Morse code convention from a file."""
        # Load Morse code convention file.
        with open(fn, 'r') as morse_file:
            code_lines = [line[:-1] for line in morse_file.readlines()]

        # Process Morse code convention file lines..
        self.codename = None
        self.text2morse = {}
        for ll,line in enumerate(code_lines):
            if line[0] == '#':
                continue
            elif line[:2] == 'MC':
                self.codename = line[3:]
                continue
            elif line[:2] == 'CS':
                key = ''
                value = line[3:]
            elif line[1] == '=':
                key = line[0]
                value = line[2:]
                if not valid_morse(value):
                    error = "Invalid Morse character in Morse code convention "
                    error += "file '{}'."
                    raise ValueError(error.format(fn))
            else:
                error = "Invalid line (#{}) in Morse code convention file '{}'"
                raise ValueError(error.format(ll+1, fn))
            self.text2morse[key] = value
        self.morse2text = {value: key for key, value in self.text2morse.items()}

        # Make sure the codename is specified.
        if self.codename is None:
            error = "No code name in Morse code convention file '{}'"
            raise ValueError(error.format(fn))

        # Make sure there is a character spacing value.
        if '' not in self.text2morse:
            error = "No character spacing convention in "
            error += "Morse code convention file '{}'"
            raise ValueError(error.format(fn))


    def encode(self, text):
        """Encode a piece of text into morse."""

        # Encode the passed string of text.
        text = text.upper()
        morse = []
        for tw in text.split(' '):
            mw = []
            for tc in tw:
                if tc in self.text2morse:
                    mw.append(self.text2morse[tc])
                else:
                    warning = "WARNING: Text character '{}' not in Morse code "
                    warning += "convention. Ignoring."
                    print(warning.format(tc))
                    continue
            mw = self.text2morse[''].join(mw)
            morse.append(mw)
        morse = self.text2morse[' '].join(morse)
        return morse


    def decode(self, morse):
        """Decode a piece of Morse code to text."""

        # Make sure the passed string is valid Morse code.
        if not valid_morse(morse):
            return "Invalid Morse character in Morse string to decode."

        # Decode the string using the loaded Morse code convention.
        text = []
        for mw in morse.split(self.text2morse[' ']):
            tw = ''
            for mc in mw.split(self.text2morse['']):
                if mc in self.morse2text:
                    tw += self.morse2text[mc]
                else:
                    warning = "WARNING: Morse sequence '{}' not in Morse code "
                    warning += "convention. Ignoring."
                    print(warning.format(mc))
            text.append(tw)
        text = ' '.join(text)
        return text


def encode_text(action='print'):
    """Encode and print or beep text."""
    # Check if Morse code convention is set.
    if morseconvention is None:
        print("\nWARNING: No Morse code convention has been set!")
        return input("<Press ENTER to continue>")

    # Ask for text and encode.
    text = input("Text to encode > ")
    morse = morseconvention.encode(text)

    # Print or beep morse.
    if action == 'print':
        print("\n{}\n<{}>\n{}".format(text, morseconvention.codename, morse))
    elif action == 'beep':
        beep_morse(morse)
    else:
        print("\nWARNING: Invalid action '{}'.".format(action))
    input("<Press ENTER to continue>")


def decode_morse():
    """Decode and print morse."""
    # Check if Morse code convention is set.
    if morseconvention is None:
        print("\nWARNING: No Morse code convention has been set!")
        return input("<Press ENTER to continue>")

    # Ask for Morse, decode and print.
    morse = input("Morse to decode > ")
    text = morseconvention.decode(morse)
    print("\n{}\n<{}>\n{}".format(morse, morseconvention.codename, text))
    input("<Press ENTER to continue>")


if __name__ == '__main__':
    # Set default Morse code convention.
    morseconvention = MorseConvention()

    # Create menus and launch main.
    convention_menuitems = [
        ['1', 'International', lambda: morseconvention.set('ITU')],
        ['b', 'Back', 'back'],
        ['q', 'Quit', 'quit'],
        ]
    convention_menu = TextMenu('MORSE CODE CONVENTION MENU', convention_menuitems)

    main_menuitems = [
        ['1', 'Choose Morse code convention', convention_menu.ask_item],
        ['2', 'Encode and print', encode_text],
        ['3', 'Encode and beep', lambda: encode_text(action='beep')],
        ['4', 'Decode', decode_morse],
        ['q', 'Quit', 'quit'],
        ]
    main_menu = TextMenu('MAIN MENU', main_menuitems)
    main_menu.ask_item()

# End
