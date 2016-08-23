#   coding=UTF_8
#
#   ppe_string.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

## returns the value of a string (counts a-zA-Z only)
# Each alphabetical character in the string worths its position in the alphabet.
def worth_of_string(s):
    worth = 0
    for c in s:
        v = ord(c)
        if 64 < v and v < 91:
            worth += v - 64
        if 96 < v and v < 123:
            worth += v - 96
    return worth

## returns the corresponding (capital) character in the alphabet
def character_for_int(n):
    if n < 1 or n > 26:
        return None
    return chr(64 + n)
