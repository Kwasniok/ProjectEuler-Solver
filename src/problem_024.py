#   coding=UTF_8
#
#   problem_024.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from number import number_from_digit_list
from ppe_permutation import Symmetric_Group

class Problem_024(Problem):

    def __init__(self):
        self.problem_nr = 24
        self.input_format = (InputType.NUMBER_INT, None, None)
        self.default_input = 1000000
        self.description_str = '''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the ''' + dye_input_var("million-th") + " lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and " + dye_input_var(9) + "?\n"


    def calculate(self, i):

        s = Symmetric_Group(10)
        p = s[i -1]

        self.last_result = number_from_digit_list(p(range(10)))
        self.last_result_details = p

    def details(self):
        return "There are " + dye_highlight(self.last_result_details.possibilities()) + " possible distinct (lexicographic) permutations."

register_problem(Problem_024())
