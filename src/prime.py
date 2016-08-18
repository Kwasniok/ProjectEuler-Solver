#   coding=UTF_8
#
#   prime.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from math import sqrt
from sorted_set import Sorted_Set

# In this file prime numbers are defined as positive integers
# which are dividable by no other natural number than 1 and itself.

# cache for prime numbers
# Cacheing is usefull if consecutive prime numbers (including the frist prime number) are used.
# The cache must contain at least first three prime numbers!
# Caching more than the frist two primes is worse in general.
# But the cache can be filled with more primes if it's an improvement for a specific algorithm.
# !!Make sure to reset the cache afterwards!!
_cached_prime_range = Sorted_Set([2, 3])

## returns weather the integer is prime
def is_prime(n):
    # check lower bound for primes
    if n < 2:
        return False
    # check if prime was cached
    if n <= _cached_prime_range.max():
        # n is in cached range
        return n in _cached_prime_range
    # n is unknown to prime cache and has to be calculated
    i = 2
    cpi = 0
    lim = sqrt(n)
    # part 1 (with cache)
    while i <= lim:
        # n can be divided by i and is therefore not prime
        if n % i == 0:
            return False
        if cpi == len(_cached_prime_range) - 1:
            break
        cpi += 1
        i = _cached_prime_range[cpi]
    # part 2 (beyond cahce)
    while i <= lim:
        if n % i == 0:
            return False
        i += 2
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
    # check lower bound for primes
    if n <= 2:
        return None
    while True:
        n -= 1
        if is_prime(n):
            return n

## chaces primes in given range
# Caching more than the frist two primes is worse in general.
# But the cache can be filled with more primes if it's an improvement for a specific algorithm.
# !!Make sure to reset the cache afterwards!!
def cache_primes_in_rage(max):
    global _cached_prime_range
    p = _cached_prime_range.max()
    max = next_prime(max - 1)
    while p <= max:
        p = next_prime(p)
        _cached_prime_range.elements.append(p)

## reset the prime number cache
def reset_prime_cache():
    global _cached_prime_range
    _cached_prime_range = Sorted_Set([2, 3])

## returns all prime numbers greater or equals to min and less or equals to max as a list in ascending order
def get_primes_in_range(min, max):
    ps = []
    p = next_prime(min - 1)
    while p <= max:
        ps.append(p)
    return ps

## returns the prime factors of the natural number n as a list in ascending order
# note: i can be recreated by taking the product of this list (empty list means i = 1)
def factorise(n):
    if n == 1:
        return []
    else:
        i = 2
        cpi = 0
        lim = sqrt(n)
        # part 1 (with cache)
        while i <= lim:
            if n % i == 0:
                # calculate remaining distinct prime factors
                ret =  distinct_prime_factors(n / i)
                ret.append(i)
                return ret
            if cpi == len(_cached_prime_range) - 1:
                break
            cpi += 1
            i = _cached_prime_range[cpi]
        # part 2 (beyond cahce)
        while i <= lim:
            if n % i == 0:
                ret =  distinct_prime_factors(n / i)
                ret.append(i)
                return ret
            i += 2
    # n has no divisor and is therefore prime
    return [n]

def distinct_prime_factors(n):
    if n == 1:
        return []
    else:
        i = 2
        cpi = 0
        lim = sqrt(n)
        # part 1 (with cache)
        while i <= lim:
            if n % i == 0:
                # n can be divided by i
                n /= i
                # divide until n cannot be divided by i
                while n % i == 0:
                    n /= i
                # calculate remaining distinct prime factors
                ret =  distinct_prime_factors(n)
                ret.append(i)
                return ret
            if cpi == len(_cached_prime_range) - 1:
                break
            cpi += 1
            i = _cached_prime_range[cpi]
        # part 2 (beyond cahce)
        while i <= lim:
            if n % i == 0:
                n /= i
                while n % i == 0:
                    n /= i
                ret =  distinct_prime_factors(n)
                ret.append(i)
                return ret
            i += 2
    # n has no divisor and is therefore prime
    return [n]
