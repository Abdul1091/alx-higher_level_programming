#!/usr/bin/python3
"""Defines a function that checks if object is an instance of a class.
Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    class, otherwise return false
    """
    if type(obj) == a_class:
        return True
    return False
