#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/utils.py

Utility functions (source_).
"""


def get_input(*args, **kwargs):
    """Utility function for extending the builtin ``input`` function, so it can be mocked."""
    return input(*args, **kwargs)


def wrap_arguments(func, *args, **kwargs):
    """Wrap a function which has arguments so it becomes a function which doesn't have arguments."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

