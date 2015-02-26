"""
Simple calculator, created per demand of the 2nd reddit.com/r/DailyProgrammer
easy challenge. I have made this more complex than requested, but like this it
is easily expandable. And if I was still in high school, then I probably would
have expanded, but now it doesn't seem nearly as useful as it once would have
been.
"""

from math import pi


# Define a class to handle menus.
class TextMenu(object):
    """A text-based menu."""
    
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


if __name__ == '__main__':
    # The calculator's welcome text (also explains how it works).
    welcometext = """
-----------------
SIMPLE CALCULATOR
-----------------
Welcome to this simple calculator. Use the menus to navigate to the caculation
you wish to make, then provide the requested numbers. After providing the
numbers you can see the result and the used formula. Have fun!"""
    
    
    # Define the calculation functions.
    def ask_float(txt):
        """Keep asking for a float until you get one."""
        while True:
            try:
                return float(input(txt))
            except:
                print("You must provide a valid number!")


    def cube_surface_area():
        """Calculate the surface area of a cube."""
        z = ask_float("Cube edge length: ")
        result = 6*z**2
        print("The cube's surface area is: {0:.3f}".format(result))
        print("Formula: 6*z**2")
        input("PRESS ENTER TO CONTINUE")


    def cube_volume():
        """Calculate the volume of a cube."""
        z = ask_float("Cube edge length: ")
        result = z**3
        print("The cube's volume is: {0:.3f}".format(result))
        print("Formula: z**3")
        input("PRESS ENTER TO CONTINUE")


    def sphere_surface_area():
        """Calculate the surface area of a sphere."""
        r = ask_float("Sphere radius: ")
        result = 4*pi*r**2
        print("The sphere's surface area is: {0:.3f}".format(result))
        print("Formula: 4*pi*r**2")
        input("PRESS ENTER TO CONTINUE")


    def sphere_volume():
        """Calculate the volume of a sphere."""
        r = ask_float("Sphere radius: ")
        result = 4/3*pi*r**3
        print("The sphere's volume is: {0:.3f}".format(result))
        print("Formula: 4/3*pi*r**3")
        input("PRESS ENTER TO CONTINUE")


    # Create the menus.
    cubes_menuitems = [
        ['1', 'Surface Area', cube_surface_area],
        ['2', 'Volume', cube_volume],
        ['b', 'Back', 'back'],
        ['q', 'Quit', 'quit'],
        ]
    cubes_menu = TextMenu('CUBES', cubes_menuitems)

    spheres_menuitems = [
        ['1', 'Surface Area', sphere_surface_area],
        ['2', 'Volume', sphere_volume],
        ['b', 'Back', 'back'],
        ['q', 'Quit', 'quit'],
        ]
    spheres_menu = TextMenu('SPHERES', spheres_menuitems)

    geometrical_menuitems = [
        ['1', 'Cubes', cubes_menu],
        ['2', 'Spheres', spheres_menu],
        ['b', 'Back', 'back'],
        ['q', 'Quit', 'quit'],
        ]
    geometrical_menu = TextMenu('GEOMETRICAL', geometrical_menuitems)

    main_menuitems = [
        ['1', 'Geometrical', geometrical_menu],
        ['q', 'Quit', 'quit'],
        ]
    main_menu = TextMenu('MAIN', main_menuitems)

    # Welcome the user, execute the main menu, print thank you note in the end.
    print(welcometext)
    main_menu.ask_item()
    print("Thank you for using the Simple Calculator! Have a good day!")

# End
