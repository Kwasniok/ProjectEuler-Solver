#   coding=UTF_8
#
#   search.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

## returns either the index of the value to search for or None if value is not in list
# l must be a sorted list in ascending order.
# begin and end are optional parameters. Not specifing them means set boundery of search to begin resp. end of list.
# If multiple indexes can be returned only one (not further specified) index is returned.
def binary_search_index(l, value, begin=None, end=None):
    # check bounderies
    if begin == None or begin < 0:
        begin = 0
    if end == None or end >= len(l):
        end = len(l) - 1

    while True:
        # check if search was unsuccessful
        if begin > end:
            return None
        # set middle index
        m = int((begin + end) / 2)
        # compare value with middle element (and move bounderies if necessary)
        if l[m] < value:
            begin = m + 1
        elif l[m] > value:
            end = m - 1
        else:
            return m
