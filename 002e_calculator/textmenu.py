#!/usr/bin/python3
"""
Text menu class module.
"""


class TextMenu(object):
    """A text-based menu.

    Initialize by providing a name, and a list of menu items.

    Example of menu items:

    menuitems = [
        ['1', 'Go to next menu', nextmenu],
        ['2', 'Perform action', action],
        ['b', 'Go back', 'back'],
        ['q', 'Quit', 'quit'],
        ]

    In this example:
        - `nextmenu` is a TextMenu object.
        - `action` is a function or something similar.
        - `'back'` is a default action for exiting this menu loop
          and going back to the menu that is up one level.
        - `'quit'` is a default action to exit this and all upper menu levels
          at once.
    """

    def __init__(self, name, menuitems):
        """Initialize the menu."""
        self.name = name
        self.menuitems = menuitems
        self.keyactions = {}

        for item in self.menuitems:
            self.keyactions[item[0]] = item[2]


    def __str__(self):
        """Print the menu items."""
        txt = "\n=== {} ===\n".format(self.name)
        txt += '\n'.join(["{}. {}".format(item[0], item[1]) for item in \
                          self.menuitems])
        return txt


    def ask_item(self):
        """Ask for an item from the menu."""
        while True:
            print(self)
            key = input("> ").lower()
            if key not in self.keyactions:
                print("'{}' is not a valid menu item! Try again.".format(key))
                continue
            action = self.keyactions[key]
            if isinstance(action, TextMenu):
                exitcode = action.ask_item()
                if exitcode == -1:
                    return -1
            elif action == 'back':
                return
            elif action == 'quit':
                return -1
            else:
                action()


# End
