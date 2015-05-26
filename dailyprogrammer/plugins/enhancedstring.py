#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/enhancedstring.py

Enchance the built-in string object with useful methods (source_).
"""


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


    def count_characters(self, count=None):
        """Add the prevalence of each character in the enhanced string to a dictionary.

        :param count: dictionary to which the count will be added (default None)
        :type count: None or dict
        :return: the dictionary to which the count was added
        :rtype: dict

        Example::

            >>> count = EnhancedString('aaa bb c . !').count_characters()
            >>> count
            {'a': 3, 'b': 2, 'c': 1, ' ': 4, '.': 1, '!': 1}
            >>> count = EnhancedString('a dd eeee').count_characters(count)
            >>> count
            {'a': 4, 'b': 2, 'c': 1, 'd': 2, 'e': 4, ' ': 6, '.': 1, '!': 1}
        """
        if count is None:
            count = {}
        for char in self.str_:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count

