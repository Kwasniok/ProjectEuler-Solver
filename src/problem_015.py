#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import faculty

class Problem_015(Problem):

    def __init__(self):
        self.problem_nr = 15
        self.input_format = (InputType.LIST_OF, (InputType.NUMBER_INT, 1, 10000), 2, 2)
        self.default_input = [20, 20]
        self.description_str = '''Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

                             X -->
            start(0,0) > x   x   x

                      Y  x   x   x
                      :
                      V  x   x   x < end(2,2)


start > x---x---x        x---x   x        x---x   x
                |            |                |
        x   x   x        x   x---x        x   x   x
                |                |            |
        x   x   x < end  x   x   x        x   x---x


        x   x   x        x   x   x        x   x   x
        |                |                |
        x---x---x        x---x   x        x   x   x
                |            |            |
        x   x   x        x   x---x        x---x---x

How many routes are there through a ''' + dye_input_var(20) + "x" + dye_input_var(20) + " grid?"

    def calculate(self, Ns):

        X = Ns[0]
        Y = Ns[1]
        '''
         (X+Y)!
        --------
        X! * Y!
        '''
        try:
            self.last_result = faculty(X + Y) / (faculty(X) * faculty(Y))
        except OverflowError:
            self.last_result = dye_warning("Error: Stack overflow")


register_problem(Problem_015())
