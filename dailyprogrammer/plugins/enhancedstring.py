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


    def __str__(self):
        """Format the enhanced string as a string."""
        return self.str_


    def __eq__(self, other):
        """Test if the enhanced string is equal to something else."""
        return isinstance(other, EnhancedString) and self.str_ == other.str_


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


    def lines(self):
        """Return the list of lines in the enhanced string.

        :return: list of lines
        :rtype: list(EnhancedString, ...)

        Example::

            >>> EnhancedString("This string has\\nmultiple lines!").lines()
            ['This string has', 'multiple lines!']
        """
        return [EnhancedString(line) for line in self.str_.split('\n')]


    def count_lines(self):
        """Count the amount of lines in the enhanced string.

        :return: the amount of lines in the enhanced string
        :rtype: int

        Example::

            >>> EnhancedString("This string has\\nmultiple lines!").count_lines()
            2
        """
        return len(self.lines())


    def words(self):
        """Return the list of words in the enhanced string.

        :return: list of words
        :rtype: list(EnhancedString, ...)

        Example::

            >>> EnhancedString("This string has multiple words!").words()
            ['This', 'string', 'has', 'multiple', 'words!']
        """
        return [EnhancedString(word) for word in self.str_.split()]


    def count_words(self):
        """Count the amount of words in the enhanced string.

        :return: the amount of words in the enhanced string
        :rtype: int

        Example::

            >>> EnhancedString("This string has multiple words!").count_words()
            5
        """
        return len(self.words())

