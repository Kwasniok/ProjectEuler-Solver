#   coding=UTF_8
#
#   ppe_math.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from math import sqrt
import copy
from prime import is_prime, next_prime, factorise, distinct_prime_factors
from fraction import Fraction
from number import get_digit_list

##############
# PROPERTIES #
##############

## returns True is number is dividable by 2
def is_even(number):
    return number % 2 == 0

## returns True if the natural number n is abundant
# note n is abundant :<=> sum of proper divisors of n minus n is greater than n
def is_abundant(number):
    return sum_of_all_proper_divisors_of(number) - number > number

## returns True if the natural number n is deficient
# note n is deficient :<=> sum of proper divisors of n minus n is less than n
def is_deficient(number):
    return sum_of_all_proper_divisors_of(number) - number < number

## returns True if the natural number n is pandigital
# n is pandigital :<=> digits of n are a permutation of 123456789[0]
# has optional parameter include_zero
def is_pandigital(n, include_zero = False, base=10):
    # create digit list for n
    n_digits = get_digit_list(n)
    # optimized compare
    if len(n_digits) != base - 1 + int(include_zero):
        return False
    d = 1 - int(include_zero)
    while d < base:
        # check if digit d appears once in n
        appeared_once = False
        for n_d in n_digits:
            if n_d == d:
                if appeared_once:
                    # d appeares twice in n
                    return False
                appeared_once = True
        if not appeared_once:
            # d does not appear in n
            return False
        d += 1
    return True

## returns whether the natural number in i a palindrome (in given base)
# n is palindrome in base b :<=> digits of n are symmetric in base b
# (first digit equals last, second digit equals second to last, etc.)
def is_palindrome(n, base=10):
    # convert n to list of its digits in given base
    n_ds = get_digit_list(n, base)
    # compare digits in list
    for i in range(0, len(n_ds) / 2):
        if n_ds[i] != n_ds[-(i+1)]:
            return False
    return True

## extension of factorise for integers
# includes a leading -1 if i is negative
# see: factorise in prime.py
def factorise_int(i):
    if i < 0:
        # i is negative
        ret = factorise(-i)
        ret[0:0] = [-1]
        return ret
    else:
        return factorise(i)

## returns the totient for the natural number n ≥ 1
# this function implements: φ(n) = n * product[p is a prime factor of n]{1 - 1/p}
def totient(n):
    n_dpfs = distinct_prime_factors(n)
    mult = 1
    div = 1
    for p in n_dpfs:
        mult *= p - 1
        div *= p
    return n * mult / div

## returns the totient for the natural number n ≥ 1 when the distinct prime factors are known
# this function implements: φ(n) = n * product[p is a prime factor of n]{1 - 1/p}
def totient_from_distinct_prime_factors(n, ps):
    mult = 1
    div = 1
    for p in ps:
        mult *= p - 1
        div *= p
    return n * mult / div

## returns the highest common factor
# might be n (resp. m) if m (resp. n) can be divided by the other natural number
def highest_common_factor(n, m):
    #eclidian algorithm
    a = max(n, m)
    b = min(n, m)
    while True:
        r = a % b
        if r == 0:
             return b
        a = b
        b = r

## returns if the natural numbers n and m are relative prime
def are_relative_prime(n, m):
    return highest_common_factor(n, m) == 1

## returns the amount of proper divisors of the natural number n
def number_of_divisors(n):
    divs = 0
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            divs += 1
        i += 1
    divs *= 2
    return divs

## returns a list of divisors of the natural number n in ascending order
# note: includes trivial divisor n and 1
# see list_of_proper_divisors
def list_of_divisors(n):
    divs = []
    i = 1
    s = sqrt(n)
    while i < s:
        if n % i == 0:
            divs.append(i)
            divs.append(n / i)
        i += 1
    if n % s == 0:
        divs.append(int(s))
    divs.sort()
    return divs

## returns a list of divisors of the natural number n in ascending order
# note: excludes trivial divisor n, includes proper divisor 1
# see list_of_divisors
def list_of_proper_divisors(n):
    divs = [1]
    i = 2
    s = sqrt(n)
    while i < s:
        if n % i == 0:
            divs.append(i)
            divs.append(n / i)
        i += 1
    if n % s == 0 and n != 1:
        divs.append(int(s))
    divs.sort()
    return divs

## returns a list of divisors of the natural number n in ascending order
# where each divisor d fullfills min ≤ d ≤ max
# note: includes trivial divisor n and 1
# see list_of_proper_divisors
def list_of_divisors_in_range(n, min, max):
    divs = []
    i = 1
    s = sqrt(n)
    while i < s:
        if n % i == 0:
            if i >= min and i <= max:
                divs.append(i)
            if n / i >= min and n / i <= max:
                divs.append(n / i)
            if i > max:
                break
        i += 1
    if n % s == 0 and s >= min and s <= max:
        divs.append(int(s))
    divs.sort()
    return divs

## returns sum of divisors all of the natural number n in ascending order
# note: excludes trivial divisor n, includes proper divisor 1
# see list_of_proper_divisors
def sum_of_proper_divisors(n):
    sum = 1
    i = 2
    s = sqrt(n)
    while i < s:
        if n % i == 0:
            sum += i + n/i
        i += 1
    if n % s == 0 and n != 1:
        sum += int(s)
    return sum

#############
# FUNCTIONS #
#############

## returns n! for the natural number 0 ≤ n
def faculty(n):
    if n == 0:
        return 1
    ret = 1
    while n != 1:
        ret *= n
        n -= 1
    return ret

## returns nCr
def binomial_coefficient(n,r):
	if n >= r:
		return faculty(n) / (faculty(r)*faculty(n-r))
