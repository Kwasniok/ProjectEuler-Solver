#   coding=UTF_8
#
#   continued_fraction.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from fraction import Fraction
from math import sqrt

## a class representing periodic regular continued fractions
# note: the a periodic regular continued fraction is defined as:
#       a_0 + (1 / a_1 + (1 / a_2 + ...))
#       where a_1, a_2, ..., a_p repeats periodically (p is the length of the period)
class Periodic_Regular_Continued_Fraction():

    ## initialises the periodic regular continued fraction
    def __init__(self, a_0 = 0, period = []):
        # stores the continued fraction [a_0; a_1, a_2, ..., a_p] as list [a_0, a_1, a_2, ..., a_p]
        # where a_1, ..., a_p ist the period
        self.a_s = [a_0]
        self.a_s += period

    ## returns either a_0 as string if there is no fraction
    # or [a_0;(a_1, a_2, ... , a_p)] as string where a_1, ..., a_p is the period
    def __str__(self):
        # check if continued fraction has period
        if self.length_of_period() == 0:
            return str(self.a_s[0])
        # construct string wich includes the period
        s = '[' + str(self.a_s[0]) + ';('
        i = 1
        while i < len(self.a_s):
            s += str(self.a_s[i])
            if i + 1 < len(self.a_s):
                s += ','
            i += 1
        s += ')]'
        return s

    def __repr__(self):
        return str(self)

    ## returns a_n (the n-th parameter)
    # note: This method takes care of the period.
    def __getitem__(self, n):
        index = 0
        if n != 0:
            index = ((n-1) % self.length_of_period()) + 1
        return self.a_s[index]

    ## returns the length of the period
    def length_of_period(self):
        return len(self.a_s) - 1

    ## append number to continued fraction's period
    def append_to_period(self, a):
        self.a_s.append(a)

    ## returns the d-th approximation of this periodic regular continued fraction as Fraction
    # note: d = 0 returns a_0
    #       d = 1 returns a_0 + 1 / a_1
    #       d = 2 returns a_0 + 1 / (a_1 + 1 / a_2)
    #       etc.
    def approximate(self, d):
        # if there is no period return just a_0 as Fraction
        if self.length_of_period() == 0:
            return Fraction(self.a_s[0])
        # stores the final fraction
        appr = Fraction(1, 0) ## will be inverted
        # approximation: resolve the approximated fraction by calculating from deepest nested fraction to top level
        i = d
        while i >= 0:
            # calculate index of current parameter a_d (either in period or 0 for top level)
            a_i = self[i]
            # calculate the i-th numerator and denominator
            appr.invert()
            appr += Fraction(a_i)
            # go to previuos level
            i -= 1
        # return result as fraction
        return appr

## returns a Periodic_Regular_Continued_Fraction representing the square root of the natural number n
def get_continued_fraction_for_sqrt_of(n):
    # The target is to write √n like: √n = a_0 + (1 / (a_1 + (1 / (a_2 + ...))))
    # Where a_0, a_1, ... are the floored values of thier corresponding level e.g.
    # a_0 = floor(√n)
    # a_1 = floor(1 / (√n - a_0)
    # a_2 = floor(1 / (1 / (√n - a_0) - a_1))
    # ...
    # All continued fraction for square roots of natural numbers are regular and periodic.
    # Their period always starts with a_1.

    # calculate sqrt(n) once to save time
    s = sqrt(n)
    # calculate a_0
    a_0 = int(s)
    ret = Periodic_Regular_Continued_Fraction(a_0)
    # if n is square there is no period to calculate
    if n == a_0 ** 2:
        return ret
    # - calculate and append next fraction parameter a_i until it repeats -
    # The parameters a_1, a_2, ... a_p (where p is the length of the period)
    # are calculated in ascending order of the index.
    # Each step takes the fraction f = (√n - sub)/num and calculates the current level's parameter a_current
    # and the fraction g of the next level.
    # The first f is calculated by expanding √n to the frist level:
    # √n = a_0 + √n - a_0 = a_0 + 1 / (1 / (√n - a_0)) = a_0 + f
    # Where f is:
    # f = 1 / (1 / (√n - a_0))
    #
    # step 1 (implicit): invert fraction
    #     f' := f^-1 = num / (√n - sub)
    #     f' can be transformed:
    #     f' = num (√n + sub) / (n - sub^2)
    # step 2: calculate denominator of this representation of f'
    #     den = (n - sub^2) / num
    #     f' can now be written like:
    #     f' = (√n + sub) / den
    # step 3: calculate continued fraction parameter of this level
    #     a_current = floor(f') = floor((√n + sub) / den)
    #     f' can now be written as:
    #     f' = a_current + f' - a_current = a_current + (√n + sub - a_current * den) / den
    # step 4: calculate num and sub for next level
    #     Since the next level's fraction is:
    #     g = f' - a_current = (√n + sub - a_current * den) / den
    #     Which is inverted:
    #     g' := g^-1 = den / (√n + (sub - a_current * den))
    #     Now g' should be written like f' in the beginning since it becomes the f' of the next cycle:
    #     g' = num' / (√n - sub')
    #     It can be drived that the values for num and sub become:
    #     num' = den
    #     sub' = - (sub - a_current * den)
    # step 5: append a_current to the continued fraction
    # step 6: break condition (found end of period)
    #     The sequence of the continued fraction's parameters are periodic when g is equals to some f of previous levels
    #     because the algorithm reaches the exact same state as before.
    num = 1
    sub = a_0
    while True:
        den = (n - sub**2) / num
        a_current = int((s + sub) / den)
        sub = -(sub - a_current * den)
        num = den
        ret.append_to_period(a_current)
        if num == 1 and sub == a_0:
            break
    return ret
