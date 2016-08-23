#   coding=UTF_8
#
#   problem_025.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_025(Problem):

    def __init__(self):
        self.problem_nr = 25
        self.input_format = (InputType.NUMBER_INT, 2, 10000)
        self.default_input = 1000
        self.description_str = '''The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain ''' + dye_input_var(1000) + " digits?\n"


    def calculate(self, N):

        res = 0
        i = 1
        j = 1
        count = 2

        while True:
            f = i + j
            j = i
            i = f
            count += 1

            if len(str(i)) >= N:
                res = count
                break

        self.last_result = res

register_problem(Problem_025())
