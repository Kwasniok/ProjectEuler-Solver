#   coding=UTF_8
#
#   problem_027.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_prime, next_prime

class Problem_027(Problem):
    
    def __init__(self):
        self.problem_nr = 27
        self.input_format = (InputType.LIST_OF, (InputType.NUMBER_INT, 0, 5000), 1, 2)
        self.default_input = [1000, 1000]
        self.description_str = '''Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < ''' + dye_input_var(1000) + ''' and |b| < ''' + dye_input_var(1000) + '''

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.'''

    
    def calculate(self, Ns):
        
        res = 0
        res_details = [0, 0, 0] # a, b, max n
        
        Na = Ns[0]
        if len(Ns) == 1:
            Nb = Na
        else:
            Nb = Ns[1]
        
        amount_of_primes = 0
        b = 2
        while b < Nb:
            
            for a in range(-Na + 1, Na):
                
                n = -1
                unfinished_plus = True
                unfinished_minus = True
                while unfinished_plus or unfinished_minus:
                    #print("b: " + str(b) + " |a: " + str(a) + " |n: " + str(n) + " >> " + str(n*n + a*n + b) + "|" + str(is_prime(n*n + a*n + b)))
                    if unfinished_plus:
                        if not is_prime(n*n + a*n + b):
                            unfinished_plus = False
                            if n > amount_of_primes:
                                amount_of_primes = n
                                res = a * b
                                res_details = [a,b,n]
                    
                    if unfinished_minus:
                        if not is_prime(n*n + a*n - b):
                            unfinished_minus = False
                            if n > amount_of_primes:
                                amount_of_primes = n
                                rest = a * -b
                                res_details = [a,-b,n]
                    
                    n += 1
                    
            
            b = next_prime(b)
            
        self.last_result = res
        self.last_result_details = res_details
            
    def details(self):
        a = self.last_result_details[0]
        b = self.last_result_details[1]
        N = self.last_result_details[2]
        desc_str = "a = " + dye_highlight(a) + ", b = " + dye_highlight(b) + '\n'
        desc_str += "p(n) = n^2 + an + b\n\n"
        
        n = 0
        while n < N + 1:
            desc_str += "p(" + str(n)  + ") = " + str(n**2 + a*n + b) + '\n'
            n += 1
        
        return desc_str
            
register_problem(Problem_027())
