#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/enhancedstring.py

Enchance the built-in string object with useful methods (source_).
"""

from plugins.listtools import count_items


class EnhancedString(object):
    """A class representing an enhanced string object.

    This class' main purpose is to enhance the built-in string object with several
    useful methods.

    :param str str_: the built-in string object that needs to be enhanced
    """


    def __init__(self, str_):
        """Create a new enhanced string."""
        self.str_ = str_


    def __repr__(self):
        """Format the enhanced string as a representation."""
        return "'{}'".format(self.str_)


    def __str__(self):
        """Format the enhanced string as a string."""
        return self.str_


    def __len__(self):
        """Return the length of the enhanced string."""
        return len(self.str_)


    def __eq__(self, other):
        """Test if the enhanced string is equal to something else."""
        return isinstance(other, self.__class__) and self.str_ == other.str_


    def remove(self, chars):
        """Remove all instances of certain characters from the enhanced string.

        Note that any instance of each individual character in ``chars`` will be removed,
        not any instance of the complete ``chars`` string.

        :param str chars: string of characters to remove

        Example::

            >>> str_ = EnhancedString('abcdaabbccdd')
            >>> str_.remove('bc')
            >>> print(str_)
            adaadd
        """
        for c in chars:
            self.str_ = self.str_.replace(c, '')


    def align(self, a='<'):
        """Align the enhanced string left, center or right.

        :param str a: desired alignment of the text, '<' for left, '>' for right, '^' for center
                      (default '<')
        :raise: ValueError if the provided alignment is invalid

        Example::

            >>> str_ = EnhancedString('a\\nbcd\\nefghi')
            >>> print(str_)
            a
            bcd
            efghi
            >>> str_.align('>')
            >>> print(str_)
                a
              bcd
            efghi
            >>> str_.align('^')
            >>> print(str_)
              a
             bcd
            efghi
        """
        if a not in '<>^':
            error = "Unknown alignment: '{}'."
            raise ValueError(error.format(a))
        stripped = [line.strip() for line in self.str_.split('\n')]
        ml = max([len(line) for line in stripped])
        self.str_ = '\n'.join([
            '{0:{1}{2}}'.format(line, a, ml).rstrip() for line in stripped
            ])


    def count_characters(self, counts=None):
        """Count the prevalence of each character in the enhanced string.

        Note that, when providing a dictionary to which the count should be added, a deep copy
        of this dictionary is made and returned. The provided dictionary is not updated in-place!

        :param counts: dictionary to which the character counts will be added, if None a new
                       dictionary is created (default None)
        :type counts: None or dict
        :return: a deep copy of the provided dictionary, with updated counts for the characters
                 in the enhanced string
        :rtype: dict

        Example::

            >>> counts = EnhancedString('aaa bb c . !').count_characters()
            >>> counts
            {'.': 1, ' ': 4, 'a': 3, '!': 1, 'b': 2, 'c': 1}
            >>> EnhancedString('a dd eeee').count_characters(counts=counts)  ## The counts are added to the provided dictionary.
            {'.': 1, 'd': 2, '!': 1, 'e': 4, ' ': 6, 'a': 4, 'b': 2, 'c': 1}
            >>> counts  ## But the provided dictionary was not updated in-place!
            {'.': 1, ' ': 4, 'a': 3, '!': 1, 'b': 2, 'c': 1}
        """
        return count_items(self.str_, counts=counts)


    def is_palindrome(self):
        """Check whether or not the enhanced string is a palindrome.

        Note that only the alphanumeric characters are considered.

        :return: True if the enhanced string is a palindrome, False otherwise
        :rtype: bool

        Example::

            >>> EnhancedString("racecar").is_palindrome()
            True
            >>> EnhancedString("Dammit I'm mad!").is_palindrome()
            True
            >>> EnhancedString("Damn it, I'm mad!").is_palindrome()
            False
        """
        stripped = ''.join([c for c in self.str_ if c.isalnum()]).lower()
        return stripped == stripped[::-1]


    @property
    def lines(self):
        """Return the list of lines in the enhanced string.

        :return: list of lines
        :rtype: list(EnhancedString, ...)

        Example::

            >>> EnhancedString("This string has\\nmultiple lines!").lines()
            ['This string has', 'multiple lines!']
        """
        return [self.__class__(line) for line in self.str_.split('\n')]


    @property
    def nlines(self):
        """Count the amount of lines in the enhanced string.

        :return: the amount of lines in the enhanced string
        :rtype: int

        Example::

            >>> EnhancedString("This string has\\nmultiple lines!").count_lines()
            2
        """
        return len(self.lines)


    @property
    def words(self):
        """Return the list of words in the enhanced string.

        :return: list of words
        :rtype: list(EnhancedString, ...)

        Example::

            >>> EnhancedString("This string has multiple words!").words()
            ['This', 'string', 'has', 'multiple', 'words!']
        """
        return [self.__class__(word) for word in self.str_.split()]


    @property
    def nwords(self):
        """Count the amount of words in the enhanced string.

        :return: the amount of words in the enhanced string
        :rtype: int

        Example::

            >>> EnhancedString("This string has multiple words!").count_words()
            5
        """
        return len(self.words)


    def frame_with_ascii(self, char='*', mfl=80, a='<'):
        """Return a copy of the enhanced string, decorated with a nice ASCII frame.

        The frame will be six characters longer than the maximum line length in the enhanced string,
        and will be four lines higher than the amount of lines in the enhanced string. The desired
        maximum length of the frame can be provided, and the text will be split over multiple lines
        if necessary.

        :param str char: character used for the frame (default '*')
        :param int mfl: maximum length of the frame
        :param str a: alignment of the text inside the frame (see
                      :meth:`plugins.enhancedstring.EnhancedString.align`)
        :return: the framed enhanced string
        :rtype: EnhancedString

        Example::

            >>> text = '''Hello World!
            ... So long and thanks for all the fish...
            ... Yay, I'm a programmer now!'''
            >>> framed = EnhancedString(text).frame_with_ascii(char='@', mfl=30, a='^')
            >>> print(framed)
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @                          @
            @       Hello World!       @
            @  So long and thanks for  @
            @     all the fish...      @
            @  Yay, I'm a programmer   @
            @           now!           @
            @                          @
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """
        # Parse the arguments.
        char = char[0]  ## If multpile characters are given, keep only the first one.
        if a not in '<>^':
            error = "Unknown alignment: '{}'."
            raise ValueError(error.format(a))

        # Reformat the enhanced string so lines have at most mfl-6 characters.
        newlines = []
        for line in self.lines:
            newline = line.words[0].str_
            for word in line.words[1:]:
                concatenation = '{} {}'.format(newline, word)
                if len(concatenation) <= mfl-6:
                    newline = concatenation
                else:
                    newlines.append(newline)
                    newline = word.str_
            newlines.append(newline)

        # Add the frame to the enhanced string and return.
        mll = max([len(line) for line in newlines])  ## Maximum line length.
        border1 = char * (mll+6)
        border2 = char + ' ' * (mll+4) + char
        framedlines = ['{0}  {1:{2}{3}}  {0}'.format(char, line, a, mll) for line in newlines]
        return self.__class__('\n'.join([border1, border2] + framedlines + [border2, border1]))


# End
