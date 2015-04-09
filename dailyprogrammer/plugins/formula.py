#!/usr/bin/python3
"""
A collection of formula functions
"""

import math


##########################
## GEOMETRICAL FORMULAS ##
##########################

# Cubes


def cube_surface_area(z):
    """Calculate the surface area of a cube with edge length `z`."""
    return 6*z**2


def cube_volume(z):
    """Calculate the volume of a cube with edge length `z`."""
    return z**3


# Spheres


def sphere_surface_area(r):
    """Calculate the surface area of a sphere with radius `r`."""
    return 4*math.pi*r**2


def sphere_volume(r):
    """Calculate the volume of a sphere with radius `r`."""
    return 4/3*math.pi*r**3
