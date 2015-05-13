#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/textmenu.py

Create text menus and run a text menu framework (source_).
"""


class TextMenuItem(object):
    """A class representing a text menu item.

    A text menu item is characterized by an ID, an action and a description. Gathering a list of
    text menu items in a text menu makes it possible to retrieve the associated action based on
    the ID (as long as the ID of each text menu item is unique). The description allows for a
    nice presentation of the text menu item in the text menu. The action can be any type of
    object, what you (can) do with it once you retrieve it from a text menu is up to the used
    text menu framework.

    :param str id: the ID of the text menu item
    :param object action: the action associated with the text menu item
    :param str descr: description of the text menu item

    Example::

        >>> from textmenu import TextMenuItem
        >>> tmi = TextMenuItem('1', 'Hello!', 'Say hello')
        >>> print(tmi)
        1. Say hello
        >>> tmi.action
        'Hello!'
    """


    def __init__(self, id, action, descr):
        """Create a new text menu item."""
        self.id = id
        self.action = action
        self.descr = descr


    def __str__(self):
        """Format a text menu item as a string."""
        return '{}. {}'.format(self.id, self.descr)


class TextMenu(object):
    """A class representing a text menu.

    :param str name: the name of the text menu
    :param items: a list of text menu items, where each has a unique ID
    :type items: list(TextMenuItem, ...)

    Example::

        >>> from textmenu import TextMenuItem, TextMenu
        >>> def say_hello(): print('Hello!')
        ...
        >>> def say_goodbye(): print('Goodbye!')
        ...
        >>> tmi1 = TextMenuItem('1', say_hello, 'Say hello')
        >>> tmi2 = TextMenuItem('2', say_goodbye, 'Say goodbye')
        >>> tm = TextMenu('Speak', [tmi1, tmi2])
        >>> print(tm)
        === Speak ===
        1. Say hello
        2. Say goodbye
        >>> action = tm.get_action('1')
        >>> action()
        Hello!
        >>> action = tm.get_action('2')
        >>> action()
        Goodbye!
    """


    def __init__(self, name, items):
        """Create a new text menu."""
        self.name = name
        self.items = items


    def __str__(self):
        """Format a text menu as a string."""
        _str = ["=== {} ===".format(self.name)]
        _str += [tmi.__str__() for tmi in self.items]
        return '\n'.join(_str)


    def map_id_to_action(self):
        """Map the text menu item IDs to the associated actions.

        :return: a dictionary that maps the IDs of the text menu's items to the associated action
        :rtype: dict(str: object, ...)

        Example::

            >>> from textmenu import TextMenuItem, TextMenu
            >>> def say_hello(): print('Hello!')
            ...
            >>> def say_goodbye(): print('Goodbye!')
            ...
            >>> tmi1 = TextMenuItem('1', 'Hello!', 'Say hello')
            >>> tmi2 = TextMenuItem('2', 'Goodbye!', 'Say goodbye')
            >>> tm = TextMenu('Speak', [tmi1, tmi2])
            >>> tm.map_id_to_action()
            {'1': 'Hello!', '2': 'Goodbye!'}
        """
        return {tmi.id: tmi.action for tmi in self.items}


    def is_valid_id(self, id):
        """Test if the passed ID belongs to any of the text menu's items.

        :param str id: ID that is tested
        :return: True if the passed ID belongs to one of the text menu's items, False otherwise
        :rtype: bool

        Example::

            >>> from textmenu import TextMenuItem, TextMenu
            >>> def say_hello(): print('Hello!')
            ...
            >>> def say_goodbye(): print('Goodbye!')
            ...
            >>> tmi1 = TextMenuItem('1', say_hello, 'Say hello')
            >>> tm = TextMenu('Speak', [tmi1])
            >>> tm.is_valid_id('1')
            True
            >>> tm.is_valid_id('2')
            False
        """
        return id in self.map_id_to_action()


    def get_action(self, id):
        """Retrieve the action that is associated with the text menu item that has a certain ID.

        :param str id: ID of a text menu item in the text menu
        :return: action associated with the text menu item that has ID '``id``'
        :rtype: object
        :raise: ValueError if the passed ID is invalid (see :meth:`plugins.textmenu.TextMenu.is_valid_id`)

        For an example that uses this method, see :func:`plugins.textmenu.TextMenu`.
        """
        if not self.is_valid_id(id):
            raise ValueError("Item '{}' is not in menu '{}'!".format(id, self.name))
        return self.map_id_to_action()[id]


class TextMenuEngine(object):
    """An engine for running a collection of interconnected text menus.

    This engine allows for the creation of an interconnected text menu framework. The engine
    requires a dictionary of text menus paired with unique keys. By making the action of a
    text menu item the key of a text menu, the text menu item will link to that menu.

    There are two special actions:

    - ``'back'`` -- this action will implicitly link a text menu to its parent
    - ``'quit'`` -- this action will break out of the menu engine

    :param menus: a dictionary pairing text menus with (unique) keys
    :type menus: dict(str: TextMenu, ...)
    :param str main: key of the 'main' menu, which will be shown first when starting the engine

    Example::

        >>> from textmenu import TextMenuItem, TextMenu, TextMenuEngine
        >>> def say_hello(): print('Hello!')
        ...
        >>> tm_main = TextMenu('Main', [
        ...     TextMenuItem('1', 'tm_speak', 'Speak Menu'),
        ...     TextMenuItem('q', 'quit', 'Quit'),
        ... ])
        >>> tm_speak = TextMenu('Speak', [
        ...     TextMenuItem('1', say_hello, 'Say hello'),
        ...     TextMenuItem('b', 'back', 'Back to Main Menu'),
        ...     TextMenuItem('q', 'quit', 'Quit'),
        ... ])
        >>> menus = {'tm_main': tm_main, 'tm_speak': tm_speak}
        >>> tme = TextMenuEngine(menus, 'tm_main')
        >>> tme.run()
        === Main ===
        1. Speak Menu
        q. Quit
        Choose menu item > 1
        === Speak ===
        1. Say hello
        b. Back to Main Menu
        q. Quit
        Choose menu item > 1
        Hello!
        === Speak ===
        1. Say hello
        b. Back to Main Menu
        q. Quit
        Choose menu item > b
        === Main ===
        1. Speak Menu
        q. Quit
        Choose menu item > q
    """


    def __init__(self, menus, main):
        """Create a new text menu engine."""
        self.menus = menus
        self.main = main


    @staticmethod
    def ask_valid_item(tm):
        """Repeatedly ask for an item from a text menu until a valid item ID is received.

        :param TextMenu tm: the text menu from which an item should be selected
        :return: ID of the selected text menu item
        :rtype: str

        Example::

            >>> from textmenu import TextMenuItem, TextMenu, TextMenuEngine
            >>> tm = TextMenu('Menu', [
            ...     TextMenuItem('1', 'action', 'Menu Item 1'),
            ... ])
            >>> TextMenuEngine.ask_valid_item(tm)
            === Menu ===
            1. Menu Item 1
            Choose menu item > 2
            That is not a valid menu item, please try again!
            Choose menu item > 1
            '1'
        """
        print(tm)
        while True:
            id = input('Choose menu item > ')
            if tm.is_valid_id(id):
                return id
            else:
                print("That is not a valid menu item, please try again!")


    def run(self):
        """Execute the text menu engine.

        For an example that uses this method, see :func:`plugins.textmenu.TextMenuEngine`
        """
        menulayers = [self.menus[self.main]]
        while True:
            current_menu = menulayers[-1]
            id = TextMenuEngine.ask_valid_item(current_menu)
            action = current_menu.get_action(id)
            if action in self.menus:
                new_menu = self.menus[action]
                menulayers.append(new_menu)
            elif action == 'back':
                menulayers.pop()
            elif action == 'quit':
                break
            else:
                action()
