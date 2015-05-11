#!/usr/bin/python3
"""
Unit tests for module :mod:`plugins.formula`.
"""

import unittest

from plugins import formula


class TestFormulaFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.formula`."""


    def test_cube_surface_area(self):
        """Test function :func:`plugins.formula.cube_surface_area`

        **Tested:**

        - The returned cube surface area is correct.
        """
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
        """Test function :func:`plugins.formula.cube_volume`

        **Tested:**

        - The returned cube volume is correct.
        """
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
        """Test function :func:`plugins.formula.sphere_surface_area`

        **Tested:**

        - The returned sphere surface area is correct.
        """
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
        """Test function :func:`plugins.formula.sphere_volume`

        **Tested:**

        - The returned sphere volume is correct.
        """
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
