#!/usr/bin/python3
"""
Unit tests for plugin textmenu
"""

import unittest

from plugins import textmenu


class TestTextMenu(unittest.TestCase):
    """Unit tests for class textmenu.TextMenu"""


    def setUp(self):
        """Set up before test"""
        pass


    def tearDown(self):
        """Tear down after test"""
        pass


    def test___str__(self):
        """Test method textmenu.TextMenu.__str__"""
        menuitems = [
            ['1', 'Menu Item 1', 'Action 1'],
            ['q', 'Quit', 'quit'],
            ]
        tm = textmenu.TextMenu(name='Main Menu', menuitems=menuitems)
        result = tm.__str__()
        expected = '\n'.join([
            "=== Main Menu ===",
            "1. Menu Item 1",
            "q. Quit",
            ])
        self.assertEqual(result, expected)


    def test_map_id_to_action(self):
        """Test method textmenu.TextMenu.map_id_to_action"""
        menuitems = [
            ['1', 'Menu Item 1', 'Action 1'],
            ['q', 'Quit', 'quit'],
            ]
        tm = textmenu.TextMenu(name='Main Menu', menuitems=menuitems)
        result = tm.map_id_to_action()
        expected = {
            '1': 'Action 1',
            'q': 'quit',
            }
        self.assertEqual(result, expected)


    def test_is_valid_id(self):
        """Test method textmenu.TextMenu.is_valid_id"""
        menuitems = [
            ['1', 'Menu Item 1', 'Action 1'],
            ]
        tm = textmenu.TextMenu(name='Main Menu', menuitems=menuitems)
        self.assertTrue(tm.is_valid_id('1'))
        self.assertFalse(tm.is_valid_id('foo'))


    def test_get_action(self):
        """Test method textmenu.TextMenu.get_action"""
        menuitems = [
            ['1', 'Menu Item 1', 'Action 1'],
            ['q', 'Quit', 'quit'],
            ]
        tm = textmenu.TextMenu(name='Main Menu', menuitems=menuitems)
        self.assertEqual(tm.get_action('1'), 'Action 1')
        self.assertEqual(tm.get_action('q'), 'quit')
        with self.assertRaises(ValueError):
            tm.get_action('foo')


if __name__ == '__main__':
    unittest.main()
