# textmenu - Create text menus and run a text menu framework

## Description

This module contains the class TextMenu, representing a text-based menu object. Each text menu
has a name and a list of menu items. Printing the TextMenu object will show the menu's name in
a header and the list of menu items.

A menu item is a list containing three things:

- *The menu item's ID* - This is the string your user has to type to select that menu item.
- *The menu item's text* - This will be displayed next to the menu item's ID.
- *The menu item's action* - This is the action that will be linked to the menu item's ID.

This module also contains the class TextMenuEngine, which has the ability to run a framework or
collection of text menus. The TextMenuEngine is initialized by passing a dictionary that maps
labels to TextMenu objects. You also need to provide the label of the 'main' menu, so the engine
knows which TextMenu to show first. Using this engine, the actions associated with menu items can be
one of the following:

- A normal function, which will be executed.
- The label of another TextMenu, in which case the menu item will link to that TextMenu.
- The special action 'back', which is reserved to go back to the previous TextMenu.
- The special action 'quit', which breaks out of the engine.

To see an example of TextMenu and TextMenuEngine in action, see challenge 002e.

## Classes

### class textmenu.TextMenu(object)

A class for creating and handling a text-based menu.

- *method* **\_\_init\_\_(**name, menuitems**)**

  Initialize the text menu object.

  A TextMenu object must be initialized with the menu's `name` and a list of `menuitems`.

- *method* **\_\_str\_\_()**

  Format the text menu as a string.

  Example:

        $ python3
        >>> from textmenu import TextMenu
        >>> menuitems = [
        ...     ['1', 'Function 1', 'Action 1'],
        ...     ['q', 'Quit', 'quit'],
        ...     ]
        >>> menu = TextMenu('Main Menu', menuitems)
        >>> print(menu)
        === Main Menu ===
        1. Function 1
        q. Quit

- *method* **map\_id\_to_action()**

  Returns a dictionary with menu item ID's mapped to the associated actions.

  Example:

        $ python3
        >>> from textmenu import TextMenu
        >>> menuitems = [
        ...     ['1', 'Function 1', 'Action 1'],
        ...     ['q', 'Quit', 'quit'],
        ...     ]
        >>> menu = TextMenu('Main Menu', menuitems)
        >>> menu.map_id_to_action()
        {'q': 'quit', '1': 'Action 1'}

- *method* **is\_valid\_item(**id**)**

  Check if the passed menu item `id` is valid.

  Example:

        $ python3
        >>> from textmenu import TextMenu
        >>> menuitems = [
        ...     ['1', 'Function 1', 'Action 1'],
        ...     ['q', 'Quit', 'quit'],
        ...     ]
        >>> menu = TextMenu('Main Menu', menuitems)
        >>> menu.is_valid_item('1')
        True
        >>> menu.is_valid_item('foo')
        False

- *method* **get\_action(**id**)**

  Return the action that is associated with the passed menu item `id`.

  Will raise a ValueError if the passed menu item `id` is invalid.

  Example:

        $ python3
        >>> from textmenu import TextMenu
        >>> menuitems = [
        ...     ['1', 'Function 1', 'Action 1'],
        ...     ['q', 'Quit', 'quit'],
        ...     ]
        >>> menu = TextMenu('Main Menu', menuitems)
        >>> menu.get_action('1')
        'Action 1'

### class textmenu.TextMenuEngine(object)

An engine for running a TextMenu framework.

- *method* **\_\_init\_\_(**menus, main**)**

  Initialize the text menu engine.

  The engine must be initialized with a dictionary of `menus` and the label of the `main` menu.

- *staticmethod* **ask\_valid\_item(**textmenu**)**

  Repeatedly ask for an item from `textmenu` until a valid ID is received.

  The resulting menu item ID is returned.

- *method* **run()**

  Execute the text menu engine.
