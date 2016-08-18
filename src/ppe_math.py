#coding=UTF_8

from math import sqrt, floor
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
        print "ne"
        return False
    d = 1 - int(include_zero)
    while d < base:
        # check if digit d appears once in n
        appeared_once = False
        for n_d in n_digits:
            if n_d == d:
                if appeared_once:
                    print "o"
                    # d appeares twice in n
                    return False
                appeared_once = True
        if not appeared_once:
            # d does not appear in n
            print "t"
            return False
        d += 1
    return True

## returns wheather the natural number in i a palindrome (in given base)
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
        if number % i == 0:
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

#########################
#-# COMPUTING METHODS #-#
#########################

################
#-- for math --#
################

def faculty(number):
    i = 1
    for j in range(number):
        i *= j+1
    return i

def binomial_coefficient(n,k):
	if n >= k:
		return faculty(n) / (faculty(k)*faculty(n-k))

########################
#-- for translations --#
########################

def worth_of_string(str):
    worth = 0

    for c in str:
        if c == 'A' or c == 'a':
            worth += 1
        if c == 'B' or c == 'b':
            worth += 2
        if c == 'C' or c == 'c':
            worth += 3
        if c == 'D' or c == 'd':
            worth += 4
        if c == 'E' or c == 'e':
            worth += 5
        if c == 'F' or c == 'f':
            worth += 6
        if c == 'G' or c == 'g':
            worth += 7
        if c == 'H' or c == 'h':
            worth += 8
        if c == 'I' or c == 'i':
            worth += 9
        if c == 'J' or c == 'j':
            worth += 10
        if c == 'K' or c == 'k':
            worth += 11
        if c == 'L' or c == 'l':
            worth += 12
        if c == 'M' or c == 'm':
            worth += 13
        if c == 'N' or c == 'n':
            worth += 14
        if c == 'O' or c == 'o':
            worth += 15
        if c == 'P' or c == 'p':
            worth += 16
        if c == 'Q' or c == 'q':
            worth += 17
        if c == 'R' or c == 'r':
            worth += 18
        if c == 'S' or c == 's':
            worth += 19
        if c == 'T' or c == 't':
            worth += 20
        if c == 'U' or c == 'u':
            worth += 21
        if c == 'V' or c == 'v':
            worth += 22
        if c == 'W' or c == 'w':
            worth += 23
        if c == 'X' or c == 'x':
            worth += 24
        if c == 'Y' or c == 'y':
            worth += 25
        if c == 'Z' or c == 'z':
            worth += 26

    return worth

def character_for_int(number):
    if number > 26:
        return ""

    if number == 1:
        return "A"
    if number == 2:
        return "B"
    if number == 3:
        return "C"
    if number == 4:
        return "D"
    if number == 5:
        return "E"
    if number == 6:
        return "F"
    if number == 7:
        return "G"
    if number == 8:
        return "H"
    if number == 9:
        return "I"
    if number == 10:
        return "J"
    if number == 11:
        return "K"
    if number == 12:
        return "L"
    if number == 13:
        return "M"
    if number == 14:
        return "N"
    if number == 15:
        return "O"
    if number == 16:
        return "P"
    if number == 17:
        return "Q"
    if number == 18:
        return "R"
    if number == 19:
        return "S"
    if number == 20:
        return "T"
    if number == 21:
        return "U"
    if number == 22:
        return "V"
    if number == 23:
        return "W"
    if number == 24:
        return "X"
    if number == 25:
        return "Y"
    if number == 26:
        return "Z"



########################
#-- for permutations --#
########################

#------------------------------#
# complex & calculating method #
#------------------------------#

class Permutation():

    def all_permutations_from_list(E):
        list = []
        for i in range(faculty(len(E))):
            list.append(Permutation.permutation_from_list(i, E))
        return list


    def permutation_from_list(n, e):

        DigitNumber = int((n % faculty(len(e)))/faculty(len(e)-1))

        D = e[DigitNumber]

        if len(e) > 1:
            e2 = copy.copy(e)
            del(e2[DigitNumber])
            D += Permutation.permutation_from_list(n, e2)

        return D

#-----------------------#
# easy & stupid methods #
#-----------------------#

def abc_grid_for(N=3):

    paths = []
    all = ""

    for c in range(1, N+1):
        all += character_for_int(c)

    def ABCGrid(n, path=""):
        if n == 0:
            paths.append(path)

        for i in range(1, N+1):
            if not character_for_int(i) in path:
                ABCGrid(n-1, path + character_for_int(i))


    ABCGrid(N)
    return paths

def number_grid_for(N=3):

    paths = []
    all = ""

    for c in range(0, N):
        all += str(c)

    def number_grid(n, path=""):
        if n == 0:
            paths.append(path)

        for i in range(0, N):
            if not str(i) in path:
                number_grid(n-1, path + str(i))


    number_grid(N)
    return paths
