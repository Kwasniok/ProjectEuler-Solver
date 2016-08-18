#   coding=UTF_8
#
#   number.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

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
