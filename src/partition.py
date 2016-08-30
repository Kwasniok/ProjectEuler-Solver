#   coding=UTF_8
#
#   partition.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 26.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

## @package partition module for functions related to partitions of natural numbers

from ppe_math import list_of_divisors, distinct_prime_factors

# cache for partition_P, where cache[n] = P(n)
_part_p_cache = [1, 1, 2, 3]

## @brief returns number of possible partitions of the natural number n (including 0)
# @note The algorithm is described here: http://mathworld.wolfram.com/PartitionFunctionP.html
def partition_P(n):
    if n < len(_part_p_cache):
        return _part_p_cache[n]
    s = 0
    k = 0
    while k < n:
        s += sum(list_of_divisors(n-k)) * partition_P(k)
        k += 1
    if n == len(_part_p_cache):
        _part_p_cache.append(s/n)
    return s / n

# cache for partition_P, where cache[n] = P(n)
_part_prime_cache = [1, 0]

## @brief returns number of possible partitions in primes of the natural number n (including 0)
# @note The algorithm is described here: http://oeis.org/A000607
def num_of_prime_partitions(n):
    if n < len(_part_prime_cache):
        return _part_prime_cache[n]
    s = 0
    k = 1
    while k <= n:
        s += sum(distinct_prime_factors(k)) * num_of_prime_partitions(n-k)
        k += 1
    if n == len(_part_prime_cache):
        _part_prime_cache.append(s/n)
    return s / n
