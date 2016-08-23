#   coding=UTF_8
#
#   problem_040.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_040(Problem):

    def __init__(self):
        self.problem_nr = 40
        self.input_format = (InputType.NUMBER_INT, 1, 9)
        self.default_input = 6
        self.description_str = '''An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910''' + dye_highlight(1) + '''112131415161718192021...

It can be seen that the ''' + dye_highlight(12) + '''th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d10^0 × d10^1 × d10^2 × ... × d10^''' + dye_input_var(6) + '''
[notation was changed but is equivalent to original]
'''

    def calculate(self, N):

        res = 1

        ds = ""
        i = 1
        max = 10**N
        while len(ds) < max:

            ds += str(i)
            i += 1

        for i in range(0, N):
			#print(int(ds[10**i - 1]))
            res *= int(ds[10**i - 1])

        self.last_result = res

register_problem(Problem_040())
