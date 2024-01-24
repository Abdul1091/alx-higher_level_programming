#!/usr/bin/python3


def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    sam = list(a_dictionary.keys())[0]
    bdic = a_dictionary[sam]
    for k, i in a_dictionary.items():
        if i > bdic:
            bdic = i
            sam = k
    return (sam)
