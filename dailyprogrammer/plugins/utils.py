#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/utils.py

Utility functions (source_).
"""


def get_input(*args, **kwargs):
    """Wrapper function for the builtin ``input`` function, so it can be mocked."""
    return input(*args, **kwargs)

