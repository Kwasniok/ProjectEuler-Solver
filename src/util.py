#   coding=UTF_8
#
#   util.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from colours import *

def listToFancyStr(L, separator = None, normalColour = None, highlightColour = None, startHighlight = None, endHighlight = None):

    # clip bounds for special dye colour
    if startHighlight < 0:
        startHighlight = 0
    if endHighlight > len(L) - 1:
        endHighlight = len(L) - 1
    if endHighlight < startHighlight:
        highlightColour = None

    s = ""

    if normalColour:
        s += normalColour

    i = 0
    while i < len(L):

        if highlightColour and i == startHighlight:
            s += highlightColour

        s += str(L[i])

        if highlightColour and i == endHighlight:
            if normalColour:
                s += normalColour
            else:
                s += Colours.END

        if (separator != None) and (i < len(L) - 1):

            if highlightColour and i >= startHighlight and i < endHighlight:
                if normalColour:
                    s += normalColour
                else:
                    s += Colours.END
                s += separator
                s += highlightColour
            else:
                s += separator

        i += 1

    if normalColour:
        s += Colours.END

    return s

def stringToCharList(str):
    L = []
    for c in str:
        L += c
    return L

def charListToString(L):
    str = ""
    for c in L:
        str += c
    return str
