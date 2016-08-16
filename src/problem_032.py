#   coding=UTF_8
#
#   problem_032.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_permutation import *

class Problem_032(Problem):
    
    def __init__(self):
        self.problem_nr = 32
        self.input_format = (InputType.NUMBER_INT, 1, 9) # see problem_00.py for other formats
        self.default_input = 9
        self.description_str = '''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through ''' + dye_input_var(9) + ''' pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
    
    def calculate(self, N):
        
        # list of all distinct pandigital products
        pdps = []
        # sum of all distinct products
        res = 0
        
        # total number of digits
        #Ds = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Ds = []
        for i in range(1, N + 1):
            Ds.append(i)
        ds = len(Ds)
        
                
        # for every permutation
        i = -1
        nop = num_of_permutations(Ds)
        while i < nop:
            i += 1
            
            pDs = get_permutation(i, Ds)
                        
            # digits for multiplicand
            for dm1 in range(1, ds - 1): # -2 for min. digits for multiplier and product; +1 for upper range bound
                # digits for multiplier
                for dm2 in range(1, ds - dm1): # -1 for min. digits for product; +1 for upper range bound
                    # digits for product
                    dp = ds - dm1 - dm2
                    
                    # digit counter
                    c = 0
                    # multiplicand, multiplier, product
                    m1 = 0
                    m2 = 0
                    p = 0
                    # create numbers from digits
                    for di in range(c, c + dm1):
                        m1 *= 10
                        m1 += pDs[c]
                        c += 1
                        
                    for di in range(c, c + dm2):
                        m2 *= 10
                        m2 += pDs[c]
                        c += 1
                        
                    for di in range(c, c + dp):
                        p *= 10
                        p += pDs[c]
                        c += 1
                    
                    if m1 * m2 == p: # It's a hit!
                        #print("%d * %d = %d" % (m1, m2, p))
                        
                        # check if product is already listed
                        add = True
                        for op in pdps:
                            # if product is already listed its multiplicand and multiplier are swapped
                            if op == p:
                                add = False
                                break
                        if add:
                           # print("*NEW*")
                            pdps.append(p)
                            res += p
                
        
        self.last_result = res
        
register_problem(Problem_032())
        