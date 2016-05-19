#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/002e.py

| **Challenge name:** Calculator (reddit_, source_)
| **Challenge number:** 2
| **Difficulty:** Easy
| **Submission date:** 2012-02-10
| **Status:** Complete

Description
-----------

Hello, coders! An important part of programming is being able to apply your programs,
so your challenge for today is to create a calculator application that has use in your
life. It might be an interest calculator, or it might be something that you can use in
the classroom.

For example, if you were in physics class, you might want to make a ``F = M * A`` calculation.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to
calculate ``F = M * A``, but also ``A = F/M``, and ``M = F/A``!

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 002e
    === MAIN ===
    1. Geometrical
    q. Quit
    Choose menu item > 1
    === GEOMETRICAL ===
    1. Cubes
    2. Spheres
    b. Back
    q. Quit
    Choose menu item > 2
    === SPHERES ===
    1. Surface Area
    2. Volume
    b. Back
    q. Quit
    Choose menu item > 2
    Sphere radius: 10
    The sphere's volume is: 4188.790
    Formula: 4/3*pi*r**3
    PRESS ENTER TO CONTINUE
    === SPHERES ===
    1. Surface Area
    2. Volume
    b. Back
    q. Quit
    Choose menu item > q

Module contents
---------------
"""

import math

from plugins import textmenu as tm
from plugins import utils


# Cubes
def cube_surface_area(z):
    """Calculate the surface area of a cube.

    :param float z: cube edge length
    :return: cube surface area
    :rtype: float

    Example::

        >>> cube_surface_area(3.)
        54.0
    """
    return 6*z**2


def cube_volume(z):
    """Calculate the volume of a cube.

    :param float z: cube edge length
    :return: cube volume
    :rtype: float

    Example::

        >>> cube_volume(3.)
        27.0
    """
    return z**3


# Spheres
def sphere_surface_area(r):
    """Calculate the surface area of a sphere.

    :param float r: sphere radius
    :return: sphere surface area
    :rtype: float

    Example::

        >>> sphere_surface_area(3.)
        113.09733552923255
    """
    return 4*math.pi*r**2


def sphere_volume(r):
    """Calculate the volume of a sphere.

    :param float r: sphere radius
    :return: sphere volume
    :rtype: float

    Example::

        >>> sphere_volume(3.)
        113.09733552923254
    """
    return 4/3*math.pi*r**3


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
            return float(utils.get_input(msg))
        except:
            print("You must provide a valid number!")


def calc_cube_surface_area():
    """Ask for the input required for calculating a cube's surface area and print the result."""
    z = ask_float("Cube edge length: ")
    result = cube_surface_area(z)
    print("The cube's surface area is: {0:.3f}".format(result))
    print("Formula: 6*z**2")
    utils.get_input("PRESS ENTER TO CONTINUE")


def calc_cube_volume():
    """Ask for the input required for calculating a cube's volume and print the result."""
    z = ask_float("Cube edge length: ")
    result = cube_volume(z)
    print("The cube's volume is: {0:.3f}".format(result))
    print("Formula: z**3")
    utils.get_input("PRESS ENTER TO CONTINUE")


def calc_sphere_surface_area():
    """Ask for the input required for calculating a sphere's surface area and print the result."""
    r = ask_float("Sphere radius: ")
    result = sphere_surface_area(r)
    print("The sphere's surface area is: {0:.3f}".format(result))
    print("Formula: 4*pi*r**2")
    utils.get_input("PRESS ENTER TO CONTINUE")


def calc_sphere_volume():
    """Ask for the input required for calculating a sphere's volume and print the result."""
    r = ask_float("Sphere radius: ")
    result = sphere_volume(r)
    print("The sphere's volume is: {0:.3f}".format(result))
    print("Formula: 4/3*pi*r**3")
    utils.get_input("PRESS ENTER TO CONTINUE")


# Create menus and run the calculator as a text menu engine.
def run():
    """Execute the challenges.002e module."""
    cubes_menuitems = [
        tm.TextMenuItem('1', calc_cube_surface_area, 'Surface Area'),
        tm.TextMenuItem('2', calc_cube_volume, 'Volume'),
        tm.TextMenuItem('b', 'back', 'Back'),
        tm.TextMenuItem('q', 'quit', 'Quit'),
        ]

    spheres_menuitems = [
        tm.TextMenuItem('1', calc_sphere_surface_area, 'Surface Area'),
        tm.TextMenuItem('2', calc_sphere_volume, 'Volume'),
        tm.TextMenuItem('b', 'back', 'Back'),
        tm.TextMenuItem('q', 'quit', 'Quit'),
        ]

    geometrical_menuitems = [
        tm.TextMenuItem('1', 'cubes_menu', 'Cubes'),
        tm.TextMenuItem('2', 'spheres_menu', 'Spheres'),
        tm.TextMenuItem('b', 'back', 'Back'),
        tm.TextMenuItem('q', 'quit', 'Quit'),
        ]

    main_menuitems = [
        tm.TextMenuItem('1', 'geometrical_menu', 'Geometrical'),
        tm.TextMenuItem('q', 'quit', 'Quit'),
        ]

    menus = {
        'main_menu': tm.TextMenu('MAIN', main_menuitems),
        'geometrical_menu': tm.TextMenu('GEOMETRICAL', geometrical_menuitems),
        'spheres_menu': tm.TextMenu('SPHERES', spheres_menuitems),
        'cubes_menu': tm.TextMenu('CUBES', cubes_menuitems)
        }
    calculator = tm.TextMenuEngine(menus, 'main_menu')
    calculator.run()

