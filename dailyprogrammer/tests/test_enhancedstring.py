#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_enhancedstring.py

Unit tests for module :mod:`plugins.enhancedstring` (source_).
"""

import unittest

from plugins import enhancedstring


class TestEnhancedString(unittest.TestCase):
    """Unit tests for class :func:`plugins.enhancedstring.EnhancedString`."""


    def test___init__(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.__init__`

        **Tested:**

        - The attributes of an enhanced string are correct after initialization.
        """
        str_ = enhancedstring.EnhancedString('test123')
        self.assertEqual(str_.str_, 'test123')


    def test___str__(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.__str__`

        **Tested:**

        - The returned string is correct.
        """
        str_ = enhancedstring.EnhancedString('test123')
        self.assertEqual(str_.__str__(), 'test123')


    def test___eq__(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.__str__`

        **Tested:**

        - False is returned when it should.
        - True is returned when it should.
        """
        s0 = enhancedstring.EnhancedString("This is an enhanced string.")
        s1 = "This is a regular string."
        s2 = enhancedstring.EnhancedString("This is another enhanced string.")
        s3 = enhancedstring.EnhancedString("This is an enhanced string.")
        self.assertFalse(s0 == s1)
        self.assertFalse(s0 == s2)
        self.assertTrue(s0 == s3)


    def test_remove(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.remove`

        **Tested:**

        - The passed characters are correctly removed from the enhanced string.
        """
        str_ = enhancedstring.EnhancedString('abcdaabbccddaaabbbcccddd')
        str_.remove('bc')
        self.assertEqual(str(str_), 'adaaddaaaddd')


    def test_align(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.align`

        **Tested:**

        - Center alignment works properly.
        - Right alignment works properly.
        - Left alignment workds properly.
        """
        str_ = enhancedstring.EnhancedString('a\nbcd\nefghi')
        str_.align('^')
        self.assertEqual(str(str_), '  a\n bcd\nefghi')
        str_.align('>')
        self.assertEqual(str(str_), '    a\n  bcd\nefghi')
        str_.align('<')
        self.assertEqual(str(str_), 'a\nbcd\nefghi')


    def test_count_characters(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.count_characters`

        **Tested:**

        - The character count has been correctly added to a new dictionary.
        - The character count has been correctly added to an existing dictionary.
        - The dictionary to which a count is added is not changed in-place.
        """
        s1 = enhancedstring.EnhancedString('aaa bb c . !')
        s2 = enhancedstring.EnhancedString('a dd eeee')
        count1 = s1.count_characters()
        self.assertEqual(count1, {'a': 3, 'b': 2, 'c': 1, ' ': 4, '.': 1, '!': 1})
        count2 = s2.count_characters(counts=count1)
        self.assertEqual(count2, {'a': 4, 'b': 2, 'c': 1, 'd': 2, 'e': 4, ' ': 6, '.': 1, '!': 1})
        self.assertEqual(count1, {'a': 3, 'b': 2, 'c': 1, ' ': 4, '.': 1, '!': 1})


    def test_is_palindrome(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.is_palindrome`

        **Tested:**

        - Returns True for a simple palindrome consisting only of alphanumeric characters.
        - Returns True for a palindrome containing non-alphanumeric characters.
        - Returns False for a non-palindrome.
        """
        self.assertTrue(enhancedstring.EnhancedString('racecar').is_palindrome())
        self.assertFalse(enhancedstring.EnhancedString('racetruck').is_palindrome())
        self.assertTrue(enhancedstring.EnhancedString("Dammit, I'm mad!").is_palindrome())
        self.assertFalse(enhancedstring.EnhancedString("Damn it, I'm mad!").is_palindrome())


    def test_lines(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.lines`

        **Tested:**

        - The enhanced string is correctly split in a list of enhancedstrings for each line.
        """
        s1 = enhancedstring.EnhancedString("This string has\nmultiple lines!")
        result = s1.lines()
        expected = [
            enhancedstring.EnhancedString("This string has"),
            enhancedstring.EnhancedString("multiple lines!"),
        ]
        self.assertEqual(result, expected)


    def test_count_lines(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.count_lines`

        **Tested:**

        - The returned amount of lines is correct.
        """
        s1 = enhancedstring.EnhancedString("This string has\nmultiple lines!")
        result = s1.count_lines()
        expected = 2
        self.assertEqual(result, expected)


    def test_words(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.words`

        **Tested:**

        - The enhanced string is correctly split in a list of enhancedstrings for each word.
        """
        s1 = enhancedstring.EnhancedString("This string has multiple words!")
        result = s1.words()
        expected = [
            enhancedstring.EnhancedString("This"),
            enhancedstring.EnhancedString("string"),
            enhancedstring.EnhancedString("has"),
            enhancedstring.EnhancedString("multiple"),
            enhancedstring.EnhancedString("words!"),
        ]
        self.assertEqual(result, expected)


    def test_count_words(self):
        """Test method :meth:`plugins.enhancedstring.EnhancedString.count_words`

        **Tested:**

        - The returned amount of words is correct.
        """
        s1 = enhancedstring.EnhancedString("This string has multiple words!")
        result = s1.count_words()
        expected = 5
        self.assertEqual(result, expected)

