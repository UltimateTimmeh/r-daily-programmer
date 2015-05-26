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


if __name__ == '__main__':
    unittest.main()
