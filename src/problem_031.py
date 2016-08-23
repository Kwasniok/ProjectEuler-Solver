#   coding=UTF_8
#
#   problem_031.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_031(Problem):

    def __init__(self):
        self.problem_nr = 31
        self.input_format = (InputType.NUMBER_INT, 1, 1000 )
        self.default_input = 200
        self.description_str = '''In England the currency is made up of pound, British pund, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 British pound (100p) and 2 British puonds (200p).
It is possible to make 2 British pounds in the following way:

1×1 British pound + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can 2 British pounds [''' + dye_input_var(200) + " in pence] be made using any number of coins?/n"

    def calculate(self, N):

        Q = [1, 2, 5, 10, 20, 50, 100, 200] # quantites available (ordered from lowest to highest, lowest must be one)

        qs = [] # quantities representing N

        def get_num_of_reps(N, Q, hqi):
            #print(">>>> N:%d hq:%d" % (N, Q[hqi]))

            # for every quantity q in Q:
            reps = 0
            for qi in range(1, hqi +1):
                q = Q[qi]
                #print(">> N:%d q:%d" % (N, q))
                i = 1
                while q * i <= N:
                    #print("N:%d q: %d i: %d" % (N, q, i))
                    reps += 1 # i times q and rest are 1s
                    nN = N - i*q # new N (rest)
                    nhqi = qi -1 # new highes quantity index (smaller highest quantity for rest)
                    if N > 1 and nhqi > 0: # avoid unneccessary/unintended calls
                        reps += get_num_of_reps(nN, Q, nhqi) # add amount of represenations for rest
                    i += 1

            return reps

        #print(">>>>>> N:%d" % N)
        self.last_result = 1 + get_num_of_reps(N, Q, len(Q)-1) # +1 for all 1

register_problem(Problem_031())
