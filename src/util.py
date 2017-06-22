#   coding=UTF_8
#
#   util.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from colours import *

## returns the list as fancy string
# note: list_to_fancy_str is an alternative to the standard str() for lists
#       and is specially designed for list representations in text.
# format: L[0] seperator L[1] seperator ... seperator L[last_index]
# @param normal_colour colour of the non-highlighted elements [optional]
# @param highlight_colour colour of the highlighted elements [optional]
# @param highlight_start index of first element to be highlighted [optional, needs highlight_colour]
# @parm higlight_end index last element to be highlighted [optional, needs highlight_colour]
def list_to_fancy_str(L, separator = None, normal_colour = None, highlight_colour = None, highlight_start = None, highlight_end = None):
    # clip bounds for special dye colour
    if highlight_start < 0:
        highlight_start = 0
    if highlight_end > len(L) - 1:
        highlight_end = len(L) - 1
    if highlight_end < highlight_start:
        highlight_colour = None
    #stores the final string
    s = ""
    # start string with normal colour if needeed
    if normal_colour:
        s += normal_colour
    # for each element it and append seperator (except for last element)#
    # handles the colours as well
    i = 0
    while i < len(L):
        # checks if current element is first element to be highlighted
        if highlight_colour and i == highlight_start:
            s += highlight_colour
        # append element
        s += str(L[i])
        # checks if current element is last element to be highlighted
        if highlight_colour and i == highlight_end:
            if normal_colour:
                s += normal_colour
            else:
                s += Colours.END
        # append seperator (excpet for last element, is not highlighted)
        if (separator != None) and (i < len(L) - 1):
            if highlight_colour and i >= highlight_start and i < highlight_end:
                if normal_colour:
                    s += normal_colour
                else:
                    s += Colours.END
                s += separator
                s += highlight_colour
            else:
                s += separator
        # next
        i += 1
    # restore normal colour
    if normal_colour:
        s += Colours.END
    # return fancy string
    return s
