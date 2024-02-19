#!/usr/bin/python3
"""checks if object is an instance of a class
or an inherited class.
Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
"""


def is_kind_of_class(obj, a_class):
    """Return True if object is an instance of a class
    or a class that the class in question inherits from otherwise
    return False.
    """
    if isinstance(obj, a_class):
        return True
    return False
