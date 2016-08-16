#   coding=UTF_8
#
#   prime.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from math import sqrt
from sorted_set import *

# In this file prime numbers are defined as positive integers
# which are dividable by no other natural number than 1 and itself.

## returns weather the integer is prime
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i +=1
    return True

## returns the next prime of the given integer
def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

## returns the previous prime number of the given integer
# or None if there is none
def prev_prime(n):
    if n <= 2:
        return None

    while True:
        n -= 1
        if is_prime(n):
            return n

# cache for prime numbers
_prime_ranges = []

## returns all prime numbers greater or equals to min and less or equals to max as a list in ascending order
def get_primes_in_range(min, max):

    min = next_prime(min - 1)
    max = prev_prime(max + 1)

    if max == None or max < min:
        return []

    prime_range_with_min = None
    prime_range_with_max = None

    # check for known range
    for prime_range in _prime_ranges:
        if prime_range.min() <= min and prime_range.max() >= max:
            return [p for p in prime_range if p >= min and p <= max]
        if min in prime_range:
            prime_range_with_min = prime_range
        if max in prime_range:
            prime_range_with_max = prime_range

    # search missing range for primes
    search_min = min
    search_max = max

    if prime_range_with_min != None:
        search_min = prime_range_with_min.max() + 1

    if prime_range_with_max != None:
        search_min = prime_range_with_min.min() - 1

    search_primes = []
    i = next_prime(search_min - 1)
    while i <= search_max:
        search_primes.append(i)
        i = next_prime(i)

    new_prime_range = Sorted_Set(search_primes)

    # store new range and concatinate with overlapping ranges if necessary
    if prime_range_with_min != None:
        new_prime_range = new_prime_range | prime_range_with_min
        _prime_ranges.remove(prime_range_with_min)

    if prime_range_with_max != None:
        new_prime_range = new_prime_range | prime_range_with_max
        _prime_ranges.remove(prime_range_with_max)

    _prime_ranges.append(new_prime_range)

    # return primes in preferred section

    # for empty range return empty list
    if len(new_prime_range) == 0:
        return []

    # find preferred section in (concatinated) new range
    start = 0 # index of first element greater or equal to min
    end = len(new_prime_range) - 1 # index to last element les or equal to max plus one
    while new_prime_range[start] < min:
        start += 1
    while new_prime_range[end] > max:
        end -= 1
    end += 1

    return new_prime_range[start:end]
