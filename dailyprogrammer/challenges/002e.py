#!/usr/bin/python3
"""
Main execution script for challenge '002Easy - Calculator'.
"""

from plugins import formula
from plugins.textmenu import TextMenu, TextMenuEngine


# Ask user input and pass to formulas.
def ask_float(msg):
    """Keep asking for a float until you get one."""
    while True:
        try:
            return float(input(msg))
        except:
            print("You must provide a valid number!")


def cube_surface_area():
    z = ask_float("Cube edge length: ")
    result = formula.cube_surface_area(z)
    print("The cube's surface area is: {0:.3f}".format(result))
    print("Formula: 6*z**2")
    input("PRESS ENTER TO CONTINUE")


def cube_volume():
    z = ask_float("Cube edge length: ")
    result = formula.cube_volume(z)
    print("The cube's volume is: {0:.3f}".format(result))
    print("Formula: z**3")
    input("PRESS ENTER TO CONTINUE")


def sphere_surface_area():
    r = ask_float("Sphere radius: ")
    result = formula.sphere_surface_area(r)
    print("The sphere's surface area is: {0:.3f}".format(result))
    print("Formula: 4*pi*r**2")
    input("PRESS ENTER TO CONTINUE")


def sphere_volume():
    r = ask_float("Sphere radius: ")
    result = formula.sphere_volume(r)
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

spheres_menuitems = [
    ['1', 'Surface Area', sphere_surface_area],
    ['2', 'Volume', sphere_volume],
    ['b', 'Back', 'back'],
    ['q', 'Quit', 'quit'],
    ]

geometrical_menuitems = [
    ['1', 'Cubes', 'cubes_menu'],
    ['2', 'Spheres', 'spheres_menu'],
    ['b', 'Back', 'back'],
    ['q', 'Quit', 'quit'],
    ]

main_menuitems = [
    ['1', 'Geometrical', 'geometrical_menu'],
    ['q', 'Quit', 'quit'],
    ]

menus = {
    'main_menu': TextMenu('MAIN', main_menuitems),
    'geometrical_menu': TextMenu('GEOMETRICAL', geometrical_menuitems),
    'spheres_menu': TextMenu('SPHERES', spheres_menuitems),
    'cubes_menu': TextMenu('CUBES', cubes_menuitems)
    }


# Create and run the calculator as a text menu engine.
def run():
    calculator = TextMenuEngine(menus, main='main_menu')
    calculator.run()
