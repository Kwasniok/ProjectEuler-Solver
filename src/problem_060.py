#   coding=UTF_8
#
#   problem_060.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from choose import choose
from ppe_math import is_prime, next_prime, binomial_coefficient as nCr
from math import log10

class Problem_060(Problem):
    
    def __init__(self):
        self.problem_nr = 60
        self.input_format = (InputType.NUMBER_INT, 2, 5)
        self.default_input = 5
        self.description_str = '''The numbers 3, 7, 109, and 673, are quite remarkable. By taking any two numbers and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four numbers, 792, represents the lowest sum for a set of four numbers with this property.

Find the lowest sum for a set of five numbers for which any two numbers concatenate to produce another prime.
'''
	
	def should_warn_long_execution_time(self):
		return True

    def calculate(self, N):
        
        resS = None
        
        # a and b must be integers
        def concats_to_prime(a, b):
            return is_prime(a * 10 ** int(log10(b) + 1) + b)
        
        def set_sum(S):
            sum = 0
            for e in S:
                sum += e
            return sum
        
        def comp_sets_by_sum(s1, s2):
            return set_sum(s1) - set_sum(s2)
        
        
        Ss = []
        p = 2
        cont = True
        while cont:
            
            p = next_prime(p)
            
            #print(p)
            
            new_sets = [[p]]
            for s in Ss:
                
                append = True
                for e in s:
                    
                    if not concats_to_prime(p, e) or not concats_to_prime(e, p):
                        append = False
                        break
                    
                if append:
                    extended_set = list(s)
                    extended_set.append(p)
                    
                    if len(extended_set) == N:
                        resS = extended_set
                        cont = False
                        break
                    
                    new_sets.append(extended_set)
            
            for s in new_sets:
                Ss.append(s)
                #if len(s) == 4:
                #    print(s)
            
            # sort all sets by sum in ascendent order
            Ss = sorted(Ss, cmp = comp_sets_by_sum) # TODO: use 'key = ConverterClassHere(comp_sets_by_sum)' for v. 3.X code
           
        self.last_result = set_sum(resS)
        self.last_result_details = resS
        
        ''' unused
        class Set():
            
            def __init__(self, set):
                
                if type(set) == list:
                    self.numbers = set
                    self.sum = 0
                    for p in self.numbers:
                        self.sum += p
                
                elif isinstance(set, Set):
                    self.numbers = list(set.numbers)
                    self.sum = set.sum
                    
            
            def add(self, n):
                self.numbers.append(n)
                self.sum += n
                
            def __len__(self):
                return len(self.numbers)
                
            def __eq__(self, other):
                self.sum == other.sum  
                
            def __ne__(self, other):
                self.sum != other.sum
                
            def __lt__(self, other):
                self.sum < other.sum
                
            def __gh__(self, other):
                self.sum > other.sum
                
            def __le__(self, other):
                self.sum <= other.sum
                
            def __ge__(self, other):
                self.sum >= other.sum
            
            def __str__(self):
                return str(self.numbers)
            
            def __repr__(self):
                return str(self.numbers)
        '''

        ''' 2nd attempt
        S = [3, 7] # lowest set for N = 2
        p = 7 # last prime used
        while len(S) < N:
            
            p = next_prime(p)
            
            print(p)
            
            cont = False
            for s in S:
                if not concats_to_prime(p, s) or not concats_to_prime(s, p):
                    cont = True
                    break
            if cont:
                continue
            
            S.append(p)
            print("HIT")
         
           
        self.last_result = set_sum(S)
        self.last_result_details = S
        '''
            
        
        ''' VERY SLOW METHOD!
        # S must contain distinct positive numbers
        def testSet(S):
            
            for e1 in S:
                
                for e2 in S:
                    
                    if e1 == e2:
                        continue
                    
                    if not concats_to_prime(e1, e2):
                        return False
                    
            return True
            
        
        # create first N numbers
        S = [2]
        while len(S) != N:
            S.append(next_prime(S[len(S) - 1]))
            
        
        i = 1
        curr_max_c_ops = nCr(len(S), N) # number of current max choose options
        lowestSetSum = None
        lowestSet = None
        while True:
            
            # list of numbers needs extension?
            if i == curr_max_c_ops + 1:
                
                # found set in last partition of numbers?
                if lowestSet != None:
                    break
                    
                S.append(next_prime(S[len(S) - 1]))
                curr_max_c_ops = nCr(len(S), N) 
                
            S = choose(i, N, S) # i-th iteration of N elements out of S
            
            ssum = set_sum(S)
            if testSet(S) and (lowestSet == None or ssum < lowestSetSum):
                print("HIT")
                lowestSetSum = ssum
                lowestSet = S
            
            print(str(i) + " : " + str(S) + " --> " + str(testSet(S)))
            
            
            i += 1
        
        self.last_result = lowestSet
        '''
        
    def details(self):
        return list_to_fancy_str(self.last_result_details, ", ")
        
register_problem(Problem_060())
