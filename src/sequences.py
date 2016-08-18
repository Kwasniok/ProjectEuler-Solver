#   coding=UTF_8
#
#   sequences.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from math import sqrt

## FIBONACCI ##

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

## COLLATZ ##

## returns the collatz chain of the natural number n as a list
# note: the collatz function is defined as:
#        { 1      if n = 1
# f(n) = { n/2    if n is even
#        { 3n+1   if n is odd
def collatz_chain(n):
    if n == 1:
        return [n]
    else:
        if n % 2 == 0:
            return [n] + collatz_chain(n / 2)
        else:
            return [n] + collatz_chain(n*3 + 1)

## returns the depth of the collatz chain of the natural numbber n
# see collatz_chain
def collatz_depth(n):
    depth = 1
    if n == 1:
        return depth
    else:
        if n % 2 == 0:
            depth += collatz_depth(n / 2)
            return depth
        else:
            # optimisation for odd numbers combines two steps (result for odd n is always even)
            depth += collatz_depth((n*3 + 1)/2) + 1
            return depth

## N-GON SEQUENCES ##

#-- Triangle Numbers --#
## returns the n-th triange number (n ≥ 1)
def triangle_number(n):
    return n * (n + 1) / 2
## returns weather the natural n is a triangle number
def is_triangle_number(n):
    return (- 0.5 + sqrt(0.25 + 2 * n)) % 1.0 == 0.0
## returns the position of the triangle number t
# note: if t is not a triangle number the result is undefined
def triangle_number_inverse(t):
    return - 0.5 + sqrt(0.25 + 2 * t)

#-- Square Numbers --#
## returns the n-th square number (n ≥ 1)
def square_number(n):
    return n ** 2
## returns weather the natural n is a triangle number
def is_square_number(n):
    return sqrt(n) % 1.0 == 0.0
## returns the position of the square number s
# note: if s is not a square number the result is undefined
def square_number_inverse(s):
    return sqrt(s)

#-- Pentagonal Numbers --#
## returns the n-th pentagonal number (n ≥ 1)
def pentagonal_number(n):
    return n * (3 * n - 1) / 2
## returns weather the natural n is a pentagonal number
def is_pentagonal_number(n):
    return ((1 + sqrt(1.0 + 24 * n)) / 6.0) % 1.0 == 0.0
## returns the position of the pentagonal number p
# note: if p is not a pentagonal number the result is undefined
def pentagonal_number_inverse(p):
    return (1 + sqrt(1.0 + 24 * p)) / 6.0

#-- Hexagonal Numbers --#
## returns the n-th hexagonal number (n ≥ 1)
def hexagonal_number(n):
    return n * (2 * n - 1)
## returns weather the natural n is a hexagonal number
def is_hexagonal_number(n):
    return ((1 + sqrt(1.0 + 8 * n)) / 4.0) % 1.0 == 0.0
## returns the position of the hexagonal number h
# note: if h is not a hexagonal number the result is undefined
def hexagonal_number_inverse(h):
    return (1 + sqrt(1.0 + 8 * h)) / 4.0

#-- Heptagonal Numbers --#
## returns the n-th heptagonal number (n ≥ 1)
def heptagonal_number(n):
    return n * (5 * n - 3) / 2
## returns weather the natural n is a heptagonal number
def is_heptagonal_number(n):
    return ((1.5 + sqrt(2.25 + 10 * n)) / 5.0) % 1.0 == 0.0
## returns the position of the heptagonal number h
# note: if h is not a heptagonal number the result is undefined
def heptagonal_number_inverse(h):
    return (1.5 + sqrt(2.25 + 10 * h)) / 5.0

#-- Octagonal Numbers --#
## returns the n-th octagonal number (n ≥ 1)
def octagonal_number(n):
    return n * (3 * n - 2)
## returns weather the natural n is a octagonal number
def is_octagonal_number(n):
    return ((2.0 + sqrt(4.0 + 12 * n)) / 6.0) % 1.0 == 0.0
## returns the position of the octagonal number o
# note: if o is not a octagonal number the result is undefined
def octagonal_number_inverse(o):
    return (2.0 + sqrt(4.0 + 12 * o)) / 6.0
