#   coding=UTF_8
#
#   input_format.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

import re
from colours import *
from date import Date
from util import listToFancyStr

# Each input format is a list of variable length starting with the InputType
# and continuing with specifications like limits (see annotations).
# [optional] means None is supported and if used this specification will be left out.
# Each input format list must have the correct size!
# Limits (min, max, etc.) must be of the same type!

## enum for input types
class InputType:
    TUPLE_HETEROGENE = -11 # , len, 1st input format, 2nd input format, ... , len-th input format
    CHOOSE_FROM_LIST = -2 # , list of supported values
    LIST_OF = -1 # , InputFormat, minLen, maxLen
    NUMBER_INT = 1 # , min [optional], max [optional]
    #NUMBER_FLOAT = 2
    #STRING_ALL = 3
    #STRING_ALPHABET = 4
    #STRING_NUMBER = 5
    DATE = 10 # , min [optional], max [optional]

## returns the value from string according to the input format
# return format: (bool which is true if conversion was successful, converted value)
def valueFromString(ipf, s):

    if ipf[0] == InputType.NUMBER_INT:
        if re.match("^[+-]?\d+$", s):
            i = int(s)

            if ipf[1] != None and i < ipf[1]:
                return (False, "number is smaller than limit of " + dye_limit(ipf[1]) + ".")
            elif ipf[2] != None and i > ipf[2]:
                return (False, "number is larger than limit of " + dye_limit(ipf[2]) + ".")
            else:
                return (True, i)
        else:
            return (False, "input must be an " + dye_input_type("integer"))

    elif ipf[0] == InputType.LIST_OF:
        ss = s.split()

        if ipf[2] != None and len(ss) < ipf[2]:
            return (False, "more arguments needed (" + dye_warning("add ") + dye_limit(ipf[2] - len(ss)) + " more argument(s))")
        if ipf[3] != None and len(ss) > ipf[3]:
            return (False, "fewer arguments needed (" + dye_warning("remove ") + dye_limit(len(ss) - ipf[3]) + " argument(s))")

        vs = []
        i= 0
        while i < len(ss):
            v = valueFromString(ipf[1], ss[i])
            if v[0]:
                vs.append(v[1])
            else:
                return (False, "error at element " + dye_warning(i + 1) + " in list:\n" + v[1])

            i += 1

        return (True, vs)

    elif ipf[0] == InputType.CHOOSE_FROM_LIST:

        for v in ipf[1]:
            if s == str(v):
                return (True, v)

        eStr = "element " + dye_warning("not in list") + ":\n"
        eStr += listToFancyStr(ipf[1], ', ', highlightColour = Colours.INPUTVAR, startHighlight = 0, endHighlight = len(ipf[1]))
        return (False, eStr)

    elif ipf[0] == InputType.TUPLE_HETEROGENE:
        ss = s.split()

        if len(ss) < ipf[1]:
            return (False, "more arguments needed (" + dye_warning("add ") + dye_limit(ipf[1] - len(ss)) + " more argument(s))")
        if len(ss) > ipf[1]:
            return (False, "fewer arguments needed (" + dye_warning("remove ") + dye_limit(len(ss) - ipf[1]) + " argument(s))")

        vs = []
        i = 0
        while i < ipf[1]:
            v = valueFromString(ipf[i + 2], ss[i])
            if v[0]:
                vs.append(v[1])
            else:
                return (False, "error at element " + dye_warning(i + 1) + " in heterogenous tuple:\n" + v[1])
            i += 1

        return (True, vs)

    elif ipf[0] == InputType.DATE:
        if re.match("^\d{1,2}\.\d{1,2}\.\d{4,4}$", s):
            ss = s.split('.')

            day   = int(ss[0])
            month = int(ss[1])
            year  = int(ss[2])

            date = Date(year, month, day)
            date.update()

            if date.day != day or date.month != month or date.year != year:
                return (False, dye_warning("this date is not supported"))
            elif ipf[1] != None and date < ipf[1]:
                return (False, "date is before limit of " + dye_limit(ipf[1].getDateAsString()) + ".")
            elif ipf[2] != None and date > ipf[2]:
                return (False, "date is past limit of " + dye_limit(ipf[2].getDateAsString()) + ".")
            else:
                return (True, date)
        else:
            return (False, "input must be an " + dye_input_type("date") + " with format " + dye_input_type("DD.MM.YYYY"))

    else:
        return (False, " - unknown input format / " + dye_warning("program broken") + " - ")


## retruns usage text for the given input type format
def usage_text_for_input_format(ipf): #TODO: COMPLETE!

    if ipf[0] == InputType.NUMBER_INT: # or InputType.STRING_NUMBER:
        uStr = "type in an " + dye_input_type("integer") + " from "

        if ipf[1] != None:
            uStr += dye_limit(ipf[1])
        else:
            uStr += dye_limit("-infinity")
        uStr += " to "
        if ipf[2] != None:
            uStr += dye_limit(ipf[2])
        else:
            uStr += dye_limit("infinity")

        return uStr

#     elif ipf[0] == InputType.NUMBER_FLOAT:
#         uStr = "type in a " + dye_input_type("floating point number") + " from "
#
#         if ipf[1] != None:
#             uStr += dye_limit(ipf[1])
#         else:
#             uStr += dye_limit("-infinity")
#         uStr += " to "
#         if ipf[2] != None:
#             uStr += dye_limit(ipf[2])
#         else:
#             uStr += dye_limit("infinity")
#
#         return uStr
    elif ipf[0] == InputType.LIST_OF:
        uStr = "type in a " + dye_input_type("list") + " with at least " + dye_limit(ipf[2]) + " and at most " + dye_limit(ipf[3]) + " elements of the following format:\n"
        uStr += "\t" + usage_text_for_input_format(ipf[1])

        return uStr


    elif ipf[0] == InputType.CHOOSE_FROM_LIST:
        uStr = "type in one of these values:\n"
        uStr += listToFancyStr(ipf[1], ', ', highlightColour = Colours.INPUTVAR, startHighlight = 0, endHighlight = len(ipf[1]))

        return uStr

    elif ipf[0] == InputType.TUPLE_HETEROGENE:
        uStr = "type in " + dye_limit(ipf[1]) + " elements of following (distinct) formats:"
        i = 0
        while i < ipf[1]:
            uStr += "\n\t" + usage_text_for_input_format(ipf[2 + i])
            i += 1

        return uStr

    elif ipf[0] == InputType.DATE:
        uStr = "type in a " + dye_input_type("date") + " (DD.MM.YY)"

        if ipf[1] != None and ipf[2] != None:
            uStr += " between " + dye_limit(ipf[1].getDateAsString()) + " and " + dye_limit(ipf[2].getDateAsString()) + " (" + dye_highlight("including limits") + ")"
        elif ipf[1] != None:
            uStr += " past " + dye_limit(ipf[1].getDateAsString()) + " (" + dye_highlight("including limit") + ")"
        elif ipf[2] != None:
            uStr += " before " + dye_limit(ipf[2].getDateAsString()) + " (" + dye_highlight("including limit") + ")"
        else:
            pass

        return uStr

    else:
        return " - " + dye_warning("usage unknown") + " - \nTo not let you unsatisfied here you have a 42."
