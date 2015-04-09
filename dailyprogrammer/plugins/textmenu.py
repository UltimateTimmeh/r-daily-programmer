#!/usr/bin/python3
"""
Create text menus and run a text menu framework
"""


class TextMenu(object):
    """A class for creating and handling a text-based menu."""

    def __init__(self, name, menuitems):
        """Initialize the text menu object."""
        self.name = name
        self.menuitems = menuitems


    def __str__(self):
        """Format the text menu as a string."""
        _str = ["=== {} ===".format(self.name)]
        _str += ["{}. {}".format(item[0], item[1]) for item in self.menuitems]
        return '\n'.join(_str)


    def map_id_to_action(self):
        """Returns a dictionary with menu item ID's mapped to the associated actions."""
        _map = {}
        for menuitem in self.menuitems:
            id, action = menuitem[0], menuitem[2]
            _map[id] = action
        return _map


    def is_valid_item(self, id):
        """Check if the passed menu item `id` is valid."""
        return id in self.map_id_to_action()


    def get_action(self, id):
        """Return the action that is associated with the passed menu item `id`."""
        if not self.is_valid_item(id):
            raise ValueError("Item '{}' is not in menu '{}'!".format(id, self.name))
        action = self.map_id_to_action()[id]
        return action


class TextMenuEngine(object):
    """An engine for running a TextMenu framework."""


    def __init__(self, menus, main):
        """Initialize the text menu engine."""
        self.main = main
        self.menus = menus


    @staticmethod
    def ask_valid_item(textmenu):
        """Repeatedly ask for an item from `textmenu` until a valid ID is received."""
        while True:
            id = input('Choose menu item > ')
            if textmenu.is_valid_item(id):
                return id
            else:
                print("That is not a valid menu item, please try again!")


    def run(self):
        """Execute the text menu engine."""
        menulayers = [self.menus[self.main]]
        while True:
            current_menu = menulayers[-1]
            print(current_menu)
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
