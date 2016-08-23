#   coding=UTF_8
#
#   problem_068.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_permutation import Symmetric_Group
from math import log10

class Problem_068(Problem):

    def __init__(self):
        self.problem_nr = 68
        self.input_format = (InputType.CHOOSE_FROM_LIST, [3, 5, 7, 9])
        self.default_input = 5
        self.description_str = '''Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

         4
          .
           3
          .  .
         1 .  2 . 6
        .
       5

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total  Solution Set
9      4,2,3; 5,3,1; 6,1,2
9      4,3,2; 6,2,1; 5,1,3
10     2,3,5; 4,5,1; 6,1,3
10     2,5,3; 6,3,1; 4,1,5
11     1,4,6; 3,6,2; 5,2,4
11     1,6,4; 5,4,2; 3,2,6
12     1,5,6; 2,6,4; 3,4,5
12     1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" ''' + dye_input_var(5) + '''-gon ring?
'''

    def calculate(self, G):

        # This problem was a first hit problem!
        # ~25 lines of code and two perfect solutions for G=3, 5 without ANY bug or error! :D

        def findGon(G):

            Ns = range(2 * G, 0, -1) # G inner numbers + G outer numbers; high to low

            stop = False
            for fon in range(G + 1, 0, -1): # first outer number (lowest outer number); high to low

                # remaining numbers (outer & inner)
                Nsoi = list(Ns)
                Nsoi.remove(fon)

                for i in range(G + 1):
                    oons = [] # other outer numbers

                    # other outer numbers; ordered high to low
                    while i < G - 1:
                        oons.append(Nsoi[i])
                        i += 1

                    # remaining inner numbers
                    ins = list(Nsoi)
                    for oon in oons:
                        ins.remove(oon)

                    # for each combination of outer numbers; high to low
                    for perm in Symmetric_Group(len(oons)):
                        poons = perm(oons)

                        # outer numbers
                        # O[n] := n-th outer number; clockwise
                        O = []
                        O.append(fon)
                        O += poons

                        # inner numbers
                        # I[n] := n-th inner number; clockwise
                        #for I in all_permutations(ins):
                        for p in Symmetric_Group(len(ins)):
                            I = p (ins)

                            # (O[n], I[n], I[(n+1) mod G]) is the n-th chain

                            m = None # magic number
                            n = 0
                            while n < G:
                                cv = O[n] + I[n] + I[(n+1) % G] # chain value

                                if m == None:
                                    m = cv
                                elif cv != m:
                                    break

                                n += 1

                            # are all chains of same value?
                            if n == G:
                                return (O, I)

        gon = findGon(G)

        O = gon[0]
        I = gon[1]
        res_str = ""
        for n in range(G):
            res_str += str(O[n])
            res_str += str(I[n])
            res_str += str(I[(n+1) % G])


        self.last_result = int(res_str)
        self.last_result_details = gon

    def details(self):
        desc_str = "Total  Solution Set\n"
        G = self.last_input
        O = self.last_result_details[0]
        I = self.last_result_details[1]

        cv = O[0] + I[0] + I[1]
        desc_str += str(cv) + " " * (7 - int(log10(cv) + 1))

        for n in range(G):
            desc_str += str(O[n]) + ","
            desc_str += str(I[n]) + ","
            desc_str += str(I[(n+1) % G])
            if n < G - 1:
                desc_str += "; "

        return desc_str

register_problem(Problem_068())
