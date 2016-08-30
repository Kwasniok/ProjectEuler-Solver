#   coding=UTF_8
#
#   problem_078.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 30.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from partition import partition_P

class Problem_078(Problem):

    def __init__(self):
        self.problem_nr = 78
        self.input_format = (InputType.NUMBER_INT, 1, None)
        self.default_input = 1000000
        self.description_str = '''Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

         OOOOO
        OOOO  O
        OOO  OO
       OOO  O  O
       OO  OO  O
      OO  O  O  O
     O  O  O  O  O

Find the least value of n for which p(n) is divisible by ''' + dye_input_var("one million") + '''.'''

    def should_warn_long_execution_time(self):
        return True

    def calculate(self, N):

        n = 0
        while partition_P(n) % N != 0:
            n += 1
            if n % 1000 == 0:
                Footer.set_text_left(str(n) + ":" + str(partition_P(n)))
                Footer.draw()

        self.last_result = n

register_problem(Problem_078())
