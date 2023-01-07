#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or >= len(my_list):
        return ("None")
    else:
        reurn my_list[idx]
