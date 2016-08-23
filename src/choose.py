#   coding=UTF_8
#
#   choose.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from ppe_math import binomial_coefficient as nCr

## returns i-th variation to choose m (nautral number) elements from sequence seq (list or string)
#  where i = 1 is the frist and i = nCr(len(seq), m) is the last variation
# @param i must be a an integer in range 1 ≤ i ≤ nCr(len(seq), m)
# @param reverse begin with last variation (optional, default is False)
# note: This algorithm assumes that all elements in seq are distinct.
# note: The order of elements is preserved.
# note: The order of variations is determined by the following scheme:
#       The highest index is kept as low as possible as well as the second highest index etc..
#       e.g.:     i \ seq: A B C D
#       (m = 2)   1        X X
#                 2        X   X
#                 3          X X
#                 4        X     X
#                 5          X   X
#                 6            X X
#       (where X marks a chosen index)
#       When reversed the lowest index is NOT always set as high as possible etc.!
def choose(i, m, seq, reverse=False):
    n = len(seq)
    # check parameters
    if m < 1 or m > n or i < 1 or i > nCr(n, m):
        return None
    # check if order is reversed
    if reverse:
        i = nCr(n, m) + 1 - i
    # internal recursive function
    def _choose(i, m, seq, n):
        # stop condition (no more elements to choose)
        if m  == 0:
            if type(seq) == list:
                return []
            if type(seq) == str:
                return ""
        # find index for first element to choose
        k = n
        for q in range(n, m - 1, -1):
            l = nCr(q, m)
            if i <= l:
                k = q
            else:
                break
        # get new chosen element
        if type(seq) == list:
            ret = [seq[k - 1]]
        if type(seq) == str:
            ret = seq[k-1]
        # calculate values for remaining elements to choose
        if k > m:
            i -= nCr(k - 1, m)
        m -= 1
        n = k - 1
        # recursive call for remaining elements to be chosen
        return _choose(i, m, seq, n) + ret
    # return result
    return _choose(i, m, seq, n)

## returns i-th variation to choose m (nautral number) elements from range(n)
#  where i = 1 is the frist and i = nCr(len(seq), m) is the last variation
# @param i must be a an integer in range 1 ≤ i ≤ nCr(len(seq), m)
# @param reverse begin with last variation (optional, default is False)
# note: This algorithm assumes that all elements in seq are distinct.
# note: The order of elements is preserved.
# note: The order of variations is determined by the following scheme:
#       The highest index is kept as low as possible as well as the second highest index etc..
#       e.g.:     i \ seq: 0 1 2 3
#       (m = 2)   1        X X
#       (n = 4)   2        X   X
#                 3          X X
#                 4        X     X
#                 5          X   X
#                 6            X X
#       (where X marks a chosen index)
#       When reversed the lowest index is NOT always set as high as possible etc.!
def choose_from_range(i, m, n, reverse=False):
    # check parameters
    if m < 1 or m > n or i < 1 or i > nCr(n, m):
        return None
    # check if order is reversed
    if reverse:
        i = nCr(n, m) + 1 - i
    # internal recursive function
    def _choose(i, m, n):
        # stop condition (no more elements to choose)
        if m  == 0:
            return []
        # find index for first element to choose
        k = n
        for q in range(n, m - 1, -1):
            l = nCr(q, m)
            if i <= l:
                k = q
            else:
                break
            ret = [k - 1]
        # calculate values for remaining elements to choose
        if k > m:
            i -= nCr(k - 1, m)
        m -= 1
        n = k - 1
        # recursive call for remaining elements to be chosen
        return _choose(i, m, n) + ret
    # return result
    return _choose(i, m, n)
