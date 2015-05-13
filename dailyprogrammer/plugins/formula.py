#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/formula.py

A collection of basic formulas (source_).
"""

import math


##########################
## GEOMETRICAL FORMULAS ##
##########################


# Cubes
def cube_surface_area(z):
    """Calculate the surface area of a cube.

    :param float z: cube edge length
    :return: cube surface area
    :rtype: float

    Example::

        >>> from formula import cube_surface_area
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

        >>> from formula import cube_volume
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

        >>> from formula import sphere_surface_area
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

        >>> from formula import sphere_volume
        >>> sphere_volume(3.)
        113.09733552923254
    """
    return 4/3*math.pi*r**3
