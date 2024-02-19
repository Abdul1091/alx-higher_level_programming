#!/usr/bin/python3
"""This module defines an inherited list class MyList."""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
