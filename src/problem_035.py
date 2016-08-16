#   coding=UTF_8
#
#   problem_035.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#


from problem_000 import *
from math import log10
from ppe_math import get_digits_as_list, number_from_digit_list, is_prime
from sys import maxint
from ppe_permutation import all_rotations


class Problem_035(Problem):
    
    def __init__(self):
        self.problem_nr = 35
        self.input_format = (InputType.NUMBER_INT, 1, 100000000)
        self.default_input = 1000000
        self.description_str = '''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below ''' + dye_input_var("one million") + "?\n"
    
    def calculate(self, N):
        
        # number of digits
        DS = int(log10(N)) + 1
        rot_primes = []
        
        # special code for primes in range(2, 10)
        M = 10
        if N < 10:
            M = N
        
        for n in range (2, M):
            if is_prime(n):
                #print(n)
                rot_primes.append(n)
        
        # special code for primes in range (10, infinity)
        # all other digits can be left out
        # if any circular variation ends with 0, 2, 4, 5, 6 or 8 it can not be a circular prime number
        B4Ds = [1, 3, 7, 9]
        for ds in range (2, DS + 1):
            
            # numbers are mapped as numbers to base 3 to B4Ds:
            # number of variations
            vs = 4 ** ds
            # for each variation:
            # variation mapping indexes
            vis = []
            for i in range(0, vs):
                # conversion to 'base 4'
                vis = []
                cur = i
                while len(vis) != ds: # leading zeros are intended
                    vis[0:0] = [cur % 4]
                    cur /= 4
            
                # mapping to 'base 10'
                n = 0
                for d in vis:
                    n *= 10
                    n += B4Ds[d]
                #print(n)
                
                if n >= N:
                    break
                       
                Ds = get_digits_as_list(n)
                add = True
                for r in all_rotations(Ds):
                    # current rotation
                    rn = number_from_digit_list(r)
                    
                    # save time by looking-up known circular primes
                    for rp in rot_primes:
                        if rn == rp:
                            break
                        
                    # if one permutation is not a prime
                    if not is_prime(rn):
                        add = False
                        break
                
                if add:
                    #print(n)
                    rot_primes.append(n)
            
        
        self.last_result = len(rot_primes)
        self.last_result_details = rot_primes
        
        
        
    def details(self):
        desc_str = "All rotational primes below " + dye_input_var(self.last_input) + ":\n"
        
        i = 0
        while i < len(self.last_result_details):
            desc_str += str(self.last_result_details[i])
            if i < len(self.last_result_details) - 1:
                desc_str += ", "
            i += 1
        
        return desc_str
    
register_problem(Problem_035())
