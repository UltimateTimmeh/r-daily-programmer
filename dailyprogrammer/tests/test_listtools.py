#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_listtools.py

Unit tests for module :mod:`plugins.listtools` (source_).
"""

import random
import unittest

from plugins import listtools


class TestListtoolsFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.listtools`."""


    def randomrange(self, *args, **kwargs):
        """Generate a randomly shuffled range."""
        x = list(range(*args, **kwargs))
        random.shuffle(x)
        return x


    def test_swap(self):
        """Test function :func:`plugins.listtools.swap`

        **Tested:**

        - The items in the list were swapped correctly.
        """
        x = list(range(10))
        listtools.swap(x, 2, 7)
        self.assertEqual(x, [0, 1, 7, 3, 4, 5, 6, 2, 8, 9])


    def test_insertionsort(self):
        """Test function :func:`plugins.listtools.insertionsort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.insertionsort(x)
        self.assertEqual(x, expected)


    def test_selectionsort(self):
        """Test function :func:`plugins.listtools.selectionsort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.selectionsort(x)
        self.assertEqual(x, expected)


    def test_mergesort(self):
        """Test function :func:`plugins.listtools.mergesort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        x = listtools.mergesort(x)
        self.assertEqual(x, expected)


    def test_quicksort(self):
        """Test function :func:`plugins.listtools.quicksort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.quicksort(x)
        self.assertEqual(x, expected)


    def test_heapsort(self):
        """Test function :func:`plugins.listtools.heapsort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.heapsort(x)
        self.assertEqual(x, expected)


    def test_bubblesort(self):
        """Test function :func:`plugins.listtools.bubblesort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.bubblesort(x)
        self.assertEqual(x, expected)


    def test_shellsort(self):
        """Test function :func:`plugins.listtools.shellsort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.shellsort(x)
        self.assertEqual(x, expected)


    def test_combsort(self):
        """Test function :func:`plugins.listtools.combsort`

        **Tested:**

        - A randomly shuffled range from 0 to 100 is correctly sorted.
        """
        x, expected = self.randomrange(100), list(range(100))
        listtools.combsort(x)
        self.assertEqual(x, expected)


    def test_evensort(self):
        """Test function :func:`plugins.listtools.combsort`

        **Tested:**

        - The even numbers are correctly placed in front of the odd numbers.
        """
        x, expected = [4, 1, 7, 2, 6, 3, 5], [4, 6, 2, 7, 1, 3, 5]
        listtools.evensort(x)
        self.assertEqual(x, expected)


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


    def test_find_first_duplicate(self):
        """Test function :func:`plugins.listtools.find_first_duplicate`

        **Tested:**

        - If there are no duplicate items, None is returned.
        - If there is a single duplicate item, that item is returned.
        - If there are multiple duplicate items, only the first duplicate item is returned.
        """
        self.assertEqual(listtools.find_first_duplicate([0, 1, 2, 3, 4]), None)
        self.assertEqual(listtools.find_first_duplicate([0, 1, 2, 3, 4, 2]), 2)
        self.assertEqual(listtools.find_first_duplicate([0, 1, 2, 3, 3, 4, 2]), 3)


if __name__ == '__main__':
    unittest.main()
