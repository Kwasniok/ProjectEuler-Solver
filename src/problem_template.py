#   coding=UTF_8
#
#   problem_QQQ.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on XX.XX.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_QQQ(Problem):

    def __init__(self):
        self.problem_nr = QQQ
        self.input_format = (InputType.NUMBER_INT, XX, XX)
        self.default_input = XX
        self.description_str = XX

    def calculate(self, XX):

        res = 0

        self.last_result = res

register_problem(Problem_QQQ())
