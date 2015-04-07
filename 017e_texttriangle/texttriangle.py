#!/usr/bin/python3
"""
Module containing TextTriangle class, a class capable of printing a text
triangle with chosen character, base length, skip and alignment.
"""

from justifytext import justify_text


class TextTriangle(object):
    """Class capable of printing a text triangle with various options."""


    def __init__(self,
        char='*', levels=5, start=1, rm=0, lm=1, add=1,
        order='ascending', align='left',
        ):
        """Initialize the TextTriangle object."""
        self.char = char
        self.levels = levels
        self.start = start
        self.rm = rm
        self.lm = lm
        self.add = add
        self.order = order
        self.align = align


    def __str__(self):
        """Print the triangle's properties."""
        _str = ["Triangle properties:"]
        _str += ["===================="]
        for key, value in self.__dict__.items():
            _str += ["   - {}: {}".format(key, value)]
        return '\n'.join(_str)


    def draw(self):
        # Compose the triangle.
        triangle = [self.char*self.start]
        for ii in range(1, self.levels):
            nelems = len(triangle[-1])*self.rm + ii*self.lm + self.add
            triangle += [self.char*nelems]

        # Format the triangle.
        if self.order == 'descending':
            triangle = triangle [::-1]
        triangle = justify_text('\n'.join(triangle), self.align)

        # Print the triangle.
        print(triangle)
