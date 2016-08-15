#   coding=UTF_8
#
#   version_independent_input.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

import sys

def get_line(str=""):
    if sys.version_info > (3, 0):
        return input(str)
    if sys.version_info > (2, 0):
        return raw_input(str)
