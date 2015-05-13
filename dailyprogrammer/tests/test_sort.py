#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_sort.py

Unit tests for module :mod:`plugins.sort` (source_).
"""

import random
import unittest

from plugins import sort


class TestSortFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.sort`."""


    def test_swap(self):
        """Test function :func:`plugins.sort.swap`

        **Tested:**

        - The chosen items in the list are swapped correctly.
        - The returned item is the value of the first item to be swapped.
        """
        x = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(sort.swap(x, 0, 4), 'a')
        self.assertEqual(x, ['e', 'b', 'c', 'd', 'a'])


    def test_insertion(self):
        """Test function :func:`plugins.sort.insertion`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.insertion(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_selection(self):
        """Test function :func:`plugins.sort.selection`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.selection(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_merge(self):
        """Test function :func:`plugins.sort.merge`

        **Tested:**

        - The returned list is sorted correctly.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        x = sort.merge(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_quick(self):
        """Test function :func:`plugins.sort.quick`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.quick(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_heap(self):
        """Test function :func:`plugins.sort.heap`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.heap(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_bubble(self):
        """Test function :func:`plugins.sort.bubble`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.bubble(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_shell(self):
        """Test function :func:`plugins.sort.shell`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.shell(x)
        self.assertEqual(x, list(range(1, 2000)))


    def test_comb(self):
        """Test function :func:`plugins.sort.comb`

        **Tested:**

        - The passed list is correctly sorted in-place.
        """
        x = list(range(1, 2000))
        random.shuffle(x)
        sort.comb(x)
        self.assertEqual(x, list(range(1, 2000)))


if __name__ == '__main__':
    unittest.main()
