#!/usr/bin/python3
"""Define a function that checks if object is an instance of a class 
that inherited from the specified class or not.

Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
