#   coding=UTF_8
#
#   number.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

######################
# INTEGER <-> STRING #
######################

# used for digit to char conversion
_digits_for_base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

## returns the character representing the digit d
# note: d is limited to integers in range 0 ≤ d ≤ 35
def get_char_for_digit(d):
    if d < 0 or d > 35:
        return None
    return _digits_for_base[d]

## returns the digit corresponding to the character c
# note: c must be a single character from range 0-9 or A-Z (capital characters only!)
def get_digit_for_char(c):
    i = 0
    while i < 36:
        if c == _digits_for_base[i]:
            return i
        i += 1
    return None

## returns the string reresenting i in given base
# optional paramerter base must be a nautral number in range 2 ≤ base ≤ 35
def int_to_string(i, base=10):
    if i == 0:
        return '0'
    is_negative = i < 0
    i_str = ''
    if is_negative:
        i = -i
    while i != 0:
        i_str = get_char_for_digit(i % base) + i_str
        i /= base
    if is_negative:
        i_str = '-' + i_str
    return i_str

#####################################
# NUMBER <-> NUMBER LIST CONVERSION #
#####################################

## returns the digits of the integer i as list of integers
# has optional base parameter
# note: digits which are greater than 9 are represented as integers (NOT characters like 'A','B','C' etc.)
def get_digit_list(i, base=10):
    if i == 0:
        return [0]
    l = []
    is_negative = False
    if i < 0:
        # i is negative
        is_negative = True
        i = -i
    # extract digits
    while i != 0:
        l.append(i % base)
        i /= base
    # reverse for correct order
    l.reverse()
    if is_negative:
        l[0:0] = ['-']
    return l

## returns the integer represented by the digit list
# has optional base parameter
# note: digits which are greater than 9 are represented as integers (NOT characters like 'A','B','C' etc.)
def number_from_digit_list(l, base=10):
    i = 0
    is_negative = l[0] == '-'
    # skip minus sign if negative
    index = int(is_negative)
    while index < len(l):
        i *= base
        i += int(l[index])
        index += 1
    if is_negative:
        i *= -1
    return i
