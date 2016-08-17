#coding=UTF_8

from math import sqrt, floor
import copy
from prime import is_prime, next_prime


#############
#-- BASIC --#
#############

class Fraction():

    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    # comperision related methods

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return self.numerator != other.numerator or self.denominator != other.denominator

    def __lt__(self, other):
        return self.evaluate() < other.evaluate()

    def __le__(self, other):
        return self.evaluate() <= other.evaluate()

    def __gt__(self, other):
        return self.evaluate() > other.evaluate()

    def __ge__(self, other):
        return self.evaluate() >= other.evaluate()

    # string related methods

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        return str(self)

    def evaluate(self):
        return float(self.numerator) / float(self.denominator)


def number_from_list(L):
    n = 0
    for d in L:
        n *= 10
        n += int(d)
    return n

def list_from_number(N):
    if N == 0:
        return [0]

    l = []

    if N < 0:
        N = -N
        l[0:0] = ['-']

    while N != 0:
        l[0:0] = [N % 10]
        N /= 10

    return l

##################
#-# PROPERTIES #-#
##################

def is_even(number):
    return number % 2 == 0

def is_abundant(number):
    return sum_of_all_proper_divisors_of(number) - number > number

def is_deficient(number):
    return sum_of_all_proper_divisors_of(number) - number < number

# n must be an positive integer
def get_digits_as_list(N):

    if type(N) != int or N < 0:
        return None

    if N == 0:
        return [0]

    Ds = []
    while N != 0:
        Ds[0:0] = [N % 10]
        N /= 10

    return Ds

# converts a list of positive integers to a number
def number_from_digit_list(Ds):

    if type(Ds) != list:
        return None

    n = 0
    for d in Ds:
        if type(d) != int or d < 0:
            n = None
            break
        else:
            n *= 10
            n += d

    return n

# n must be an positive integer
def is_pandigital(n, include_zero = False):

    if type(n) != int or n < 0:
        return None

    # checks if each digit from 1 (or 0) is used exactly once
    #     0      1      2      3      4      5      6      7      8      9
    Ds = [False, False, False, False, False, False, False, False, False, False]
    ds = 0

    while n != 0:

        # get next digit
        d = n % 10

        # zero allowed?
        if d == 0 and (not include_zero):
            return False

        # digit already used?
        if (Ds[d]):
            # digit occurs twice
            return False
        else:
            # register digit
            Ds[d] = True
            ds += 1

        n /= 10

    if include_zero:
        return ds == 10
    else:
        return ds == 9

# n must be an integer
# a list is returned from witch the original value can be recreated by multiplying a variable initially set to 1 by each element of the list
# otherwise 1 is skipped as factor
def lazy_factorise(n):
        if n == 1:
            return []
        else:
            i = 2
            while i < n + 1:
                # n can be divided by i
                if is_prime(i) and n % i == 0:
                    return [i] + lazy_factorise(n / i)
                i += 1

# n must be an integer
# a list is returned from witch the original value can be recreated by multiplying a variable initially set to 1 by each element of the list
# a list containing a zero represents 0
# -1 is returned as leading factor, if n was negative
# otherwise 1 is skipped as factor
def factorise(n):
    if type(n) != int:
        return None

    if n == 0:
        return [0]

    negative = n < 0

    if negative:
        return [-1] + lazy_factorise(-n)
    else:
        return lazy_factorise(n)

## returns the totient for the natural number n ≥ 1
# this function implements: φ(n) = n * product[p is a prime factor of n]{1 - 1/p}
def totient(n):
    dpfsn = set(lazy_factorise(n)) # distinct prime factors

    mult = 1
    div = 1
    for p in dpfsn:
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

################
#-- Fractions --#
################

# a must be an integer other than 0
# b must be an integer other than 0
# a pair is returned representing the simplified fraction
def simplify_fraction_dec(n, d):
    if type(n) != int or type(d) != int or d == 0:
        return None

    if n == 1 or d == 1: # for performance only
        return (n, d)

    # get prime factors
    pfsn = factorise(n)
    pfsd = factorise(d)

    # cancel prime factors (new prime factors)
    npfsa = copy.copy(pfsn)
    npfsb = copy.copy(pfsd)

    for x in pfsd:
        try:
            npfsa.remove(x)
        except:
            pass

    for x in pfsn:
        try:
            npfsb.remove(x)
        except:
            pass

    # create simplified fraction
    n = 1
    d = 1
    for x in npfsa:
        n *= x
    for x in npfsb:
        d *= x

    return (n, d)


################
#-- Dividors --#
################

def number_of_divisors(number):
    divs = 0
    i = 1
    while i <= sqrt(number):
        if number % i == 0:
            divs += 1
        i += 1

    divs *= 2

    return divs

def list_of_divisors(number):
    divs = []
    i = 1
    while i <= sqrt(number):
        if number % i == 0:
            divs.append(i)
            divs.append(number / i)
        i += 1

    divs.sort()

    return divs

def set_of_proper_divisors(number):
    divs = set()
    i = 2
    s = sqrt(number)
    while i < s:
        if number % i == 0:
            divs.add(i)
            divs.add(number / i)
        i += 1

    if number % s == 0:
        divs.add(int(s))

    return divs

def all_proper_divisors_of(number):
    divsA = []
    divsB = []
    i = 1
    while i <= sqrt(number):
        if number % i == 0:
            divsA.append(i)
        i += 1

    for k in range(len(divsA), 0, -1):
        if divsA[k-1] < sqrt(number):
            divsB.append(int(number/divsA[k-1]))

    return divsA + divsB #sorted array


def sum_of_all_proper_divisors_of(number):
    sumOfDivs = 1

    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            sumOfDivs += i
            if i < sqrt(number):
                sumOfDivs += int(number/i)
        i += 1

    return sumOfDivs

#################
#-#   BASE    #-#
#################

_digits_for_base_ = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_digit_as_char(d):

    if type(d) != int or d < 0 or d > 35:
        return None

    return _digits_for_base_[d]

# get positive integer N in Base b as a string
def inBase(N, b):

    if type(N) != int or type(b) != int or N < 0 or b < 0:
        return None

    if N == 0:
        return '0'

    n = ''
    while N != 0:
        n = get_digit_as_char(N % b) + n
        N /= b
    return n

#################
#-#  SPECIAL  #-#
#################

def is_palindrome(E):

    if type(E) != list and type(E) != str:
        return None

    for i in range(0, len(E) / 2):
        if E[i] != E[-(i+1)]:
            return False
    return True

#################
#-# SEQUENCES #-#
#################

def collatz_depth(N):
            counter = 1

            if N == 1:
                return counter
            else:
                if N % 2 == 0:
                    counter += collatz_depth(int(N / 2))
                    return counter
                else:
                    counter += collatz_depth(N*3 + 1)
                    return counter

def collatz_chain(N):

    if N == 1:
        return [N]
    else:
        if N % 2 == 0:
            return [N] + collatz_chain(N / 2)
        else:
            return [N] + collatz_chain(N*3 + 1)


#-- Fibonacci --#

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#-- Triangle Numbers --#

def triangle_number(n):
    return n * (n + 1) / 2

# lazy implementation (only for t > 0)
def is_triangle_number(t):
    return (- 0.5 + sqrt(0.25 + 2 * t)) % 1.0 == 0.0

# check is_triangle_number first
def triangle_number_inverse(t):
    return - 0.5 + sqrt(0.25 + 2 * t)

#-- Square Numbers --#

def square_number(n):
    return n ** 2

# lazy implementation (only for t > 0)
def is_square_number(s):
    return sqrt(s) % 1.0 == 0.0

# check is_triangle_number first
def square_number_inverse(s):
    return sqrt(s)

#-- Pentagonal Numbers --#

def pentagonal_number(n):
    return n * (3 * n - 1) / 2

# lazy implementation (only for p > 0)
def is_pentagonal_number(p):
    return ((1 + sqrt(1.0 + 24 * p)) / 6.0) % 1.0 == 0.0

def pentagonal_number_inverse(p):
    return (1 + sqrt(1.0 + 24 * p)) / 6.0

#-- Hexagonal Numbers --#

def hexagonal_number(n):
    return n * (2 * n - 1)

# lazy implementation (only for p > 0)
def is_hexagonal_number(h):
    return ((1 + sqrt(1.0 + 8 * h)) / 4.0) % 1.0 == 0.0

def hexagonal_number_inverse(h):
    return (1 + sqrt(1.0 + 8 * h)) / 4.0

#-- Heptagonal Numbers --#

def heptagonal_number(n):
    return n * (5 * n - 3) / 2

# lazy implementation (only for p > 0)
def is_heptagonal_number(h):
    return ((1.5 + sqrt(2.25 + 10 * h)) / 5.0) % 1.0 == 0.0

def heptagonal_number_inverse(h):
    return (1.5 + sqrt(2.25 + 10 * h)) / 5.0

#-- Octagonal Numbers --#

def octagonal_number(n):
    return n * (3 * n - 2)

# lazy implementation (only for p > 0)
def is_octagonal_number(o):
    return ((2.0 + sqrt(4.0 + 12 * o)) / 6.0) % 1.0 == 0.0

def octagonal_number_inverse(o):
    return (2.0 + sqrt(4.0 + 12 * o)) / 6.0



###########################
#-- continued fractions --#
###########################

# takes only a positive integer s (All other parameters are used by the recursive algorithm!)
# returns list of integer value pairs representing the continues fraction
# format (an, (nsn, dn)) where nsn is the nth numerator summand and dn is the nth denominator as part of the intermediate fraction
# first pair represents digit before point
def get_continued_fraction_for_sqrt_of(s, ns = 0.0, d = 1.0, cfivps = None, cf = None): # s := square, ns := numerator summand, d := denominator, cfivps := continued fraction integer values pairs (needed for paeriod detection), cf := continued fraction

    if cfivps == None: # is first iteration
        cfivps = []

        ipi = floor(sqrt(s)) # integer part
        nsi = -ipi
        di = 1.0

    else:
        nsi = - ns
        di =  (s - (ns ** 2)) / d

        ipi = floor((sqrt(s) + nsi) / di)

        nsi -= ipi * di

    cfivpi = (ipi, (nsi, di))

    if not cfivpi in cfivps:
        cfivps.append(cfivpi)

        if cf == None:
            cf = Continued_Fraction(int(ipi), [])
        else:
            cf.appendToPeriod(int(ipi))

        return get_continued_fraction_for_sqrt_of(s, nsi, di, cfivps, cf)
    else:
        return cf

def get_acf_index(a, k):
    if a == 0:
        return 0
    else:
        return ((a-1) % k) + 1
'''
# RECUSIVE VERSION / VERY!!! SLOW!!!
# n := current depth (decreasing) , N := approximation limit, ks := list of all fraction parameters (first digit and period)
def _approximate_continued_fraction_from_list(n, N, ks):

    if n == -1:
        return 1

    if n == 0:
        return ks[get_acf_index(N, len(ks) - 1)]

    return ks[get_acf_index(N - n, len(ks) - 1)] * _approximate_continued_fraction_from_list(n - 1, N, ks) + _approximate_continued_fraction_from_list(n - 2, N, ks)
'''

# LOOP VERSION / VERY FAST!
def _approximate_continued_fraction_from_list(n, ks):
    N = 1
    D = 0

    i = n
    while i >= 0:
        d = ks[get_acf_index(i, len(ks) - 1)]

        Ni = D + d * N
        Di = N

        N = Ni
        D = Di

        i -= 1

    return Fraction(N, D)

# TODO: ADD FUNCTION BASED SUPPORT!
class Continued_Fraction():

    # takes an integer an a list of integers
    def __init__(self, firstDigit = 0, period = [], periodIsList = True):
        self.firstDigit = firstDigit
        self.period = period
        self.periodIsList = periodIsList

    def __str__(self):
        s = '[' + str(self.firstDigit) + ';('

        if self.periodIsList:
            i = 0
            while i < len(self.period):
                s += str(self.period[i])
                if i + 1 < len(self.period):
                    s += ','
                i += 1

        s += ')]'
        return s

    def __repr__(self):
        return str(self)

    def getPeriodLength(self):
        if self.periodIsList:
            return len(self.period)
        return None

    def appendToPeriod(self, p):
        self.period.append(p)

    def getApproximation(self, i):
        if i < 0:
            return None
        if self.periodIsList:
            ks = [self.firstDigit] + self.period
            #return Fraction(_approximate_continued_fraction_from_list(i, i, ks), _approximate_continued_fraction_from_list(i - 1, i, ks))
            return _approximate_continued_fraction_from_list(i, ks)




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
