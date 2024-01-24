#!/usr/bin/python3

def roman_to_int(rom_str):
    if not isinstance(rom_str, str) or rom_str is None:
        return None

    rom_var = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ret = 0
    for i in range(len(rom_str)):
        if rom_str[i] not in rom_var:
            return None
        if i == len(rom_str) - 1:
            ret += rom_var[rom_str[i]]
        elif rom_var[rom_str[i]] < rom_var[rom_str[i + 1]]:
            ret -= rom_var[rom_str[i]]
        else:
            ret += rom_var[rom_str[i]]
    return ret
