#!/usr/bin/python3
"""
Module containing functions for inverting a list in blocks of
specified length.
"""


def blockinvert(_list, bl):
    """Invert items of _list in blocks with length bl."""
    nb = int(len(_list)/bl) + 1
    _list_bi = [list(_list[ii*bl:(ii+1)*bl][::-1]) for ii in range(nb)]
    _list_bi = sum(_list_bi, [])
    return _list_bi


if __name__ == '__main__':
    nelems = int(input("List length > "))
    bl = int(input("Block size > "))
    _list = range(nelems)
    _list_bi = blockinvert(_list, bl)
    print(_list_bi)
