#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_textmenu.py

Unit tests for module :mod:`plugins.textmenu` (source_).
"""

import unittest

from plugins import textmenu


class TestTextMenuItem(unittest.TestCase):
    """Unit tests for class :func:`plugins.textmenu.TextMenuItem`."""


    def test___init__(self):
        """Test method :meth:`plugins.textmenu.TextMenuItem.__init__`

        **Tested:**

        - The attributes of a text menu item are correct after initialization.
        """
        tmi = textmenu.TextMenuItem('1', 'action', 'Menu Item 1')
        self.assertEqual(tmi.id, '1')
        self.assertEqual(tmi.action, 'action')
        self.assertEqual(tmi.descr, 'Menu Item 1')


    def test___str__(self):
        """Test method :meth:`plugins.textmenu.TextMenuItem.__str__`

        **Tested:**

        - The returned string is correct.
        """
        tmi = textmenu.TextMenuItem('1', 'action', 'Menu Item 1')
        result = tmi.__str__()
        expected = "1. Menu Item 1"
        self.assertEqual(result, expected)


class TestTextMenu(unittest.TestCase):
    """Unit tests for class :func:`plugins.textmenu.TextMenu`."""


    def test___str__(self):
        """Test method :meth:`plugins.textmenu.TextMenu.__str__`

        **Tested:**

        - The returned string is correct.
        """
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
        """Test method :meth:`plugins.textmenu.TextMenu.map_id_to_action`

        **Tested:**

        - The returned dictionary correctly maps text menu item IDs to actions.
        """
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
        """Test method :meth:`plugins.textmenu.TextMenu.is_valid_id`

        **Tested:**

        - The returned boolean is True if the passed user is valid.
        - The returned boolean is False if the passed user is invalid.
        """
        items = [
            textmenu.TextMenuItem('1', 'action', 'Menu Item 1'),
            ]
        tm = textmenu.TextMenu('Main Menu', items)
        self.assertTrue(tm.is_valid_id('1'))
        self.assertFalse(tm.is_valid_id('foo'))


    def test_get_action(self):
        """Test method :meth:`plugins.textmenu.TextMenu.get_action`

        **Tested:**

        - The returned action is correct when the passed text menu item ID exists.
        - A ValueError is raised when the passed text menu item ID does not exist.
        """
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
