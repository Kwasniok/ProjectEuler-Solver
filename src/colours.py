#   coding=UTF_8
#
#   colours.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

## constants for console colours
class Colours:
    RED_LIGHT   =  '\033[91m'
    GREEN_LIGHT =  '\033[92m'
    BLUE_LIGHT  =  '\033[94m'

    CYAN_LIGHT    = '\033[96m'
    MAGENTA_LIGHT = '\033[95m'
    YELLOW_LIGHT  = '\033[93m'

    RED_DARK   =  '\033[31m'
    GREEN_DARK =  '\033[32m'
    BLUE_DARK  =  '\033[44m'

    CYAN_DARK    = '\033[36m'
    MAGENTA_DARK = '\033[35m'
    YELLOW_DARK  = '\033[33m'

    BLACK  = '\033[0m'

    HEADER  = BLUE_LIGHT
    INFO    = GREEN_LIGHT
    FAIL    = RED_DARK

    INPUTVAR  = MAGENTA_LIGHT
    RESULTVAR = CYAN_LIGHT
    WARNING   = RED_DARK
    HIGHLIGHT = BLUE_LIGHT
    LIMIT     = RED_LIGHT
    INPUTTYPE = GREEN_LIGHT

    END = BLACK

    def test(self):
        print(Colours.RED + "R" + Colours.GREEN + "G" + Colours.BLUE + "B " +
        Colours.CYAN + "C" +  Colours.MAGENTA + "M" + Colours.YELLOW + "Y " + Colours.END)

## converts object to string and adds sourrunding colour tags
def dye_input_var(s):
    return Colours.INPUTVAR + str(s) + Colours.END

## converts object to string and adds sourrunding colour tags
def dye_result_var(s):
    return Colours.RESULTVAR + str(s) + Colours.END

## converts object to string and adds sourrunding colour tags
def dye_warning(s):
    return Colours.WARNING + str(s) + Colours.END

## converts object to string and adds sourrunding colour tags
def dye_highlight(s):
    return Colours.HIGHLIGHT + str(s) + Colours.END

## converts object to string and adds sourrunding colour tags
def dye_limit(s):
    return Colours.LIMIT + str(s) + Colours.END

## converts object to string and adds sourrunding colour tags
def dye_input_type(s):
    return Colours.INPUTTYPE + str(s) + Colours.END
