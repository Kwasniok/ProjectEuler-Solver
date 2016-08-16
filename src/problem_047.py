#   coding=UTF_8
#
#   problem_047.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import next_prime
from ppe_math import factorise
from util import list_to_fancy_str
from choose import num_of_choose_variations, choose

class Problem_047(Problem):
    
    def __init__(self):
        self.problem_nr = 47
        self.input_format = (InputType.LIST_OF, (InputType.NUMBER_INT, 1, 4), 1, 2)
        self.default_input = [4, 4]
        self.description_str = '''The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first ''' + dye_input_var("four") + " consecutive integers to have " + dye_input_var("four") + " distinct prime factors. What is the first of these numbers?\n"
    
    def calculate(self, Ns):
        
        Nci = Ns[0] # number of consecutive integers
        if len(Ns) == 1:
            Npf = Nci # number of distinct prime factors
        else:
            Npf = Ns[1]
            
        res = None
        
        # (tests all numbers) --> n > 50000
        
        '''
        # I.a
        # checks all numbers (once)
        n = 2
        while True:
            if n % 1000 == 0:
                print(n)
            i = 0
            while i < Nci:
                ni = n + i
                pfs = set(factorise(ni)) # prime factor set
                if len(pfs) != Npf:
                    break
                i += 1
                
            if i == Nci:
                break
            
            n += i + 1
            
        res = n
        '''
            
        '''
        # I.b
        # checks all numbers (once)
        ps = [2] # primes
        n = 2
        while True:
            #if n % 1000 == 0:
            #    print(n)
            i = 0
            while i < Nci:
                ni = n + i
                
                while ni > ps[len(ps) - 1]:
                    ps.append(next_prime(ps[len(ps) - 1]))
                    
                ndpf = 0
                for p in ps:
                    if ni % p == 0:
                        ndpf += 1
                    if ndpf > Npf:
                        break
                
                if ndpf != Npf:
                    break
                
                i += 1
                
            if i == Nci:
                break
            
            n += i + 1
        res = n
        '''
        
        ps = [2] # primes (for optimization only)
        def hnodpfs(n, Npf): # has number of distinct prime factors
            
            while n > ps[len(ps) - 1]:
                ps.append(next_prime(ps[len(ps) - 1]))
               
            ndpf = 0
            for p in ps:
                if n % p == 0:
                    ndpf += 1
                if ndpf > Npf:
                    return False
            
            if ndpf == Npf:
                return True
            else:
                return False
            
        
        # II.b
        # checks each Nci-th number
        # and surrounding numbers if match occurred
        n = 2
        cont = True
        while cont:
            
            # check each Nci-th number
            # if matched
            if hnodpfs(n, Npf):
                # check surrounding numbers
                ni = n - Nci + 1
                # set bounds for surrounding check
                if ni < 2:
                    ni = 2
                ss = None # sequence start
                while ni < n + Nci:
                    if hnodpfs(ni, Npf):
                        if ss == None:
                            # found first number of possible sequence
                            ss = ni
                        if ni - ss + 1 == Nci:
                            # found full sequence
                            res = ss
                            cont = False
                            break
                    else:
                        # sequence disrupted
                        ss = None
                    
                    ni += 1
            
            n += Nci
        
        ''' 
        # III.
        # -/- (unfinished)
        ### TODO: REPLACE FACTROISE WITH METHOD OF I.b!!!
        res = None
        
        ps = [2] # list of prime numbers
        # fill list with first Npf prime numbers
        while len(ps) < Npf:
            ps.append(next_prime(ps[len(ps) - 1]))
            
        # calculate lowest number with Npf distinct prime factors
        #lowest = 1
        #for p in ps:
        #    lowest *= p
        
        ### TODO: HAS TO CHECK OTHER EXPONENTS THAN 1!
        pfes = [] # list of exponents for chosen distinct prime factors
        # fill pfes with Npf 1s
        while len(pfes) < Npf:
            pfes.append(1)
                    
        cont = True
        while cont:
        
            # choose Npf distinct prime factors out of ps
            l = 0
            ncv = num_of_choose_variations(Npf, ps)
            while l != ncv:
                
                pfs = choose(l + 1, Npf, ps)  # list of chosen distinct prime factors
                    
                # construct number from pfs and pfes
                n = 1
                k = 0
                while k < Npf:
                    n *= pfs[k] ** pfes[k]
                    k += 1
                
                # check following sequence
                j = 1
                hit = True
                while j < Nci:
                    nj = n + j
                    if len(set(factorise(nj))) != Npf:
                        hit = False
                        break
                    j += 1
                
                if hit:
                    res = n
                    cont = False
                    break
                
                # next
                l += 1
                
            # extend ps
            ps.append(next_prime(ps[len(ps) - 1]))
        '''
        
        
        self.last_result = res
        
    def details(self):
        n = self.last_result
        
        Nci = self.last_input[0]
        if len(self.last_input) == 1:
            Npf = Nci
        else:
            Npf = self.last_input[1]
        
        desc_str = ""
        i = 0
        while i < Nci:
            if i == 0:
                desc_str += dye_result_var(n)
            else:
                desc_str += str(n)
            pfs = factorise(n)
            desc_str += " = " + list_to_fancy_str(pfs, " x ")
            if i + 1 != Nci:
                desc_str += '\n'
            n += 1
            i += 1
            
        return desc_str
        
register_problem(Problem_047())
