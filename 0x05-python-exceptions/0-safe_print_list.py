#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    total = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)
