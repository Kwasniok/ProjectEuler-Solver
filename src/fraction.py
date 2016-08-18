#   coding=UTF_8
#
#   fraction.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from math import sqrt
from prime import next_prime

## class representing a fraction
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

    def simplify(self):
        p = 2
        lim = min(self.numerator, self.denominator)
        while p <= lim:
            while self.numerator % p == 0 and self.denominator % p == 0:
                self.numerator /= p
                self.denominator /= p
            p = next_prime(p)
