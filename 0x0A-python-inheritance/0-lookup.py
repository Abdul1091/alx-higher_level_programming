#!/usr/bin/python3
"""This functions looks out for all attributes and methods of an object"""



def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
