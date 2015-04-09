#!/usr/bin/python3
"""
Unit tests for plugin formula
"""

import unittest

from plugins import formula


class TestFormula(unittest.TestCase):
    """Unit tests for functions in plugin formula"""


    def setUp(self):
        """Set up before test"""
        pass


    def tearDown(self):
        """Tear down after test"""
        pass


    def test_cube_surface_area(self):
        """Test function formula.cube_surface_area"""
        datapoints = [
            (0, 0),
            (1, 6),
            (3, 54),
            ]
        for data in datapoints:
            z = data[0]
            expected = data[1]
            result = formula.cube_surface_area(z)
            self.assertEqual(result, expected)


    def test_cube_volume(self):
        """Test function formula.cube_volume"""
        datapoints = [
            (0, 0),
            (1, 1),
            (3, 27),
            ]
        for data in datapoints:
            z = data[0]
            expected = data[1]
            result = formula.cube_volume(z)
            self.assertEqual(result, expected)


    def test_sphere_surface_area(self):
        """Test function formula.sphere_surface_area"""
        datapoints = [
            (0, '0.00'),
            (1, '12.57'),
            (3, '113.10'),
            ]
        for data in datapoints:
            r = data[0]
            expected = data[1]
            result = '{0:.2f}'.format(formula.sphere_surface_area(r))
            self.assertEqual(result, expected)


    def test_sphere_volume(self):
        """Test function formula.sphere_volume"""
        datapoints = [
            (0, '0.00'),
            (1, '4.19'),
            (3, '113.10'),
            ]
        for data in datapoints:
            r = data[0]
            expected = data[1]
            result = '{0:.2f}'.format(formula.sphere_volume(r))
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
