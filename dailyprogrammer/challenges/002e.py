#!/usr/bin/python3
"""
Challenge information
---------------------

| **Challenge name:** `Calculator <http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/>`_
| **Challenge number:** 2
| **Difficulty:** Easy
| **Submission date:** 2012-02-10
| **Status:** Complete

Challenge description
---------------------

Hello, coders! An important part of programming is being able to apply your programs,
so your challenge for today is to create a calculator application that has use in your
life. It might be an interest calculator, or it might be something that you can use in
the classroom.

For example, if you were in physics class, you might want to make a ``F = M * A`` calculation.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to
calculate ``F = M * A``, but also ``A = F/M``, and ``M = F/A``!

Challenge module contents
-------------------------
"""

from plugins import formula
from plugins.textmenu import TextMenu, TextMenuEngine


# Ask user input and pass to formulas.
def ask_float(msg):
    """Keep asking for a number until one is provided.

    The user is asked for input. This input is only returned if it can be converted to a float.

    :param str msg: message that will be displayed when asking for input
    :return: the float that was provided
    :rtype: float
    """
    while True:
        try:
            return float(input(msg))
        except:
            print("You must provide a valid number!")


def cube_surface_area():
    """Ask for the input required for calculating a cube's surface area and print the result."""
    z = ask_float("Cube edge length: ")
    result = formula.cube_surface_area(z)
    print("The cube's surface area is: {0:.3f}".format(result))
    print("Formula: 6*z**2")
    input("PRESS ENTER TO CONTINUE")


def cube_volume():
    """Ask for the input required for calculating a cube's volume and print the result."""
    z = ask_float("Cube edge length: ")
    result = formula.cube_volume(z)
    print("The cube's volume is: {0:.3f}".format(result))
    print("Formula: z**3")
    input("PRESS ENTER TO CONTINUE")


def sphere_surface_area():
    """Ask for the input required for calculating a sphere's surface area and print the result."""
    r = ask_float("Sphere radius: ")
    result = formula.sphere_surface_area(r)
    print("The sphere's surface area is: {0:.3f}".format(result))
    print("Formula: 4*pi*r**2")
    input("PRESS ENTER TO CONTINUE")


def sphere_volume():
    """Ask for the input required for calculating a sphere's volume and print the result."""
    r = ask_float("Sphere radius: ")
    result = formula.sphere_volume(r)
    print("The sphere's volume is: {0:.3f}".format(result))
    print("Formula: 4/3*pi*r**3")
    input("PRESS ENTER TO CONTINUE")


# Create menus and run the calculator as a text menu engine.
def run():
    """Execute the challenges.002e module."""
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
    calculator = TextMenuEngine(menus, main='main_menu')
    calculator.run()
