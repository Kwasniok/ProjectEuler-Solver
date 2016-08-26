#   coding=UTF_8
#
#   type_number.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 23.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

def is_number(obj):
    return type(obj) in [int, long, float]
