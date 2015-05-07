#!/usr/bin/python3
"""
Unit tests for plugin textmenu
"""

import unittest

from plugins import textmenu


class TestTextMenuItem(unittest.TestCase):
    """Unit tests for class textmenu.TextMenuItem"""


    def test___init__(self):
        """Test method textmenu.TextMenuItem.__init__"""
        tmi = textmenu.TextMenuItem('1', 'action', 'Menu Item 1')
        self.assertEqual(tmi.id, '1')
        self.assertEqual(tmi.action, 'action')
        self.assertEqual(tmi.descr, 'Menu Item 1')


    def test___str__(self):
        """Test method textmenu.TextMenuItem.__str__"""
        tmi = textmenu.TextMenuItem('1', 'action', 'Menu Item 1')
        result = tmi.__str__()
        expected = "1. Menu Item 1"
        self.assertEqual(result, expected)


class TestTextMenu(unittest.TestCase):
    """Unit tests for class textmenu.TextMenu"""


    def test___str__(self):
        """Test method textmenu.TextMenu.__str__"""
        items = [
            textmenu.TextMenuItem('1', 'action', 'Menu Item 1'),
            textmenu.TextMenuItem('q', 'quit', 'Quit'),
            ]
        tm = textmenu.TextMenu('Main Menu', items)
        result = tm.__str__()
        expected = '\n'.join([
            "=== Main Menu ===",
            "1. Menu Item 1",
            "q. Quit",
            ])
        self.assertEqual(result, expected)


    def test_map_id_to_action(self):
        """Test method textmenu.TextMenu.map_id_to_action"""
        items = [
            textmenu.TextMenuItem('1', 'action', 'Menu Item 1'),
            textmenu.TextMenuItem('q', 'quit', 'Quit'),
            ]
        tm = textmenu.TextMenu('Main Menu', items)
        result = tm.map_id_to_action()
        expected = {
            '1': 'action',
            'q': 'quit',
            }
        self.assertEqual(result, expected)


    def test_is_valid_id(self):
        """Test method textmenu.TextMenu.is_valid_id"""
        items = [
            textmenu.TextMenuItem('1', 'action', 'Menu Item 1'),
            ]
        tm = textmenu.TextMenu('Main Menu', items)
        self.assertTrue(tm.is_valid_id('1'))
        self.assertFalse(tm.is_valid_id('foo'))


    def test_get_action(self):
        """Test method textmenu.TextMenu.get_action"""
        items = [
            textmenu.TextMenuItem('1', 'action', 'Menu Item 1'),
            textmenu.TextMenuItem('q', 'quit', 'Quit'),
            ]
        tm = textmenu.TextMenu('Main Menu', items)
        self.assertEqual(tm.get_action('1'), 'action')
        self.assertEqual(tm.get_action('q'), 'quit')
        with self.assertRaises(ValueError):
            tm.get_action('foo')


if __name__ == '__main__':
    unittest.main()
