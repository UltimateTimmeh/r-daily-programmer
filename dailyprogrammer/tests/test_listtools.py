#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_listtools.py

Unit tests for module :mod:`plugins.listtools` (source_).
"""

import unittest

from plugins import listtools


class TestListtoolsFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.listtools`."""


    def test_merge_lists(self):
        """Test function :func:`plugins.listtools.merge_lists`

        **Tested:**

        - The returned merged list is correct.
        """
        cases = [
            (['a'], ['a'], ['a']),
            (['a'], ['b'], ['a', 'b']),
            (['a'], ['a', 'a'], ['a', 'a']),
            (['a', 'b'], ['a', 'c'], ['a', 'b', 'c']),
            (['a', 'c'], ['a', 'b'], ['a', 'c', 'b']),
        ]
        for case in cases:
            self.assertEqual(listtools.merge_lists(case[0], case[1]), case[2])


    def test_split_list(self):
        """Test function :func:`plugins.listtools.split_list`

        **Tested:**

        - The returned tuple contains the correctly splitted parts of the list.
        """
        x = list(range(10))
        cases = [
            (0.5, ([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])),
            (0.2, ([0, 1], [2, 3, 4, 5, 6, 7, 8, 9])),
            (0.8, ([0, 1, 2, 3, 4, 5, 6, 7], [8, 9])),
            (1.0, ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [])),
        ]
        for case in cases:
            self.assertEqual(listtools.split_list(x, f=case[0]), case[1])


    def test_count_items(self):
        """Test function :func:`plugins.listtools.count_items`

        **Tested:**

        - The item count is correctly added to a new dictionary.
        - The item count is correctly added to an existing dictionary.
        - The dictionary to which a count is added is not changed in-place.
        """
        x1 = ['a', 'b', 'b', 'c', 'c', 'c', 'a']
        x2 = ['d', 'e', 'e', 'e', 'd', 'a', 'e']
        count1 = listtools.count_items(x1)
        self.assertEqual(count1, {'a': 2, 'b': 2, 'c': 3})
        count2 = listtools.count_items(x2, counts=count1)
        self.assertEqual(count2, {'a': 3, 'b': 2, 'c': 3, 'd': 2,  'e': 4})
        self.assertEqual(count1, {'a': 2, 'b': 2, 'c': 3})


    def test_most_prevalent_items(self):
        """Test function :func:`plugins.listtools.most_prevalent_items`

        **Tested:**

        - The returned set of most prevalent items is correct.
        """
        x1 = ['a', 'b', 'b', 'c']
        x2 = ['a', 'b', 'b', 'c', 'a']
        self.assertEqual(listtools.most_prevalent_items(x1), {'b'})
        self.assertEqual(listtools.most_prevalent_items(x2), {'a', 'b'})


if __name__ == '__main__':
    unittest.main()
