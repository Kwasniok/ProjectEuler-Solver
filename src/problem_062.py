#   coding=UTF_8
#
#   problem_062.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_permutation import is_permutation_of
from util import stringToCharList, charListToString

class Problem_062(Problem):

    def __init__(self):
        self.problem_nr = 62
        self.input_format = (InputType.NUMBER_INT, 1, 5)
        self.default_input = 5
        self.description_str = '''The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly ''' + dye_input_var("five") + ''' permutations of its digits are cube.
'''

	def should_warn_long_execution_time(self):
		return True

    def calculate(self, N):

        PS = None
        cs = [] # cubes as character lists
        n = 1
        cont = True
        while cont:
            ci = n ** 3
            #print(ci)

            ciList = stringToCharList(str(ci))

            ps = 1
            for c in cs:
                if is_permutation_of(ciList, c):
                    ps += 1

            cs.append(ciList)

            if ps == N:
                PS = []
                for c in cs:
                    if is_permutation_of(ciList, c):
                        ci = int(charListToString(c))
                        PS.append(ci)
                cont = False

            n += 1


        self.last_result = PS[0]
        self.last_result_details = PS

    def details(self):
        return list_to_fancy_str(self.last_result_details, ", ", Colours.HIGHLIGHT)

register_problem(Problem_062())
