#   coding=UTF_8
#
#   problem_009.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from math import sqrt
from problem_000 import *

class Problem_009(Problem):

    def __init__(self):
        self.problem_nr = 9
        self.input_format = (InputType.NUMBER_INT, 1, 7500)
        self.default_input = 1000
        self.description_str = '''A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = ''' + dye_input_var(1000) + '''.
Find the product abc.
'''

    def calculate(self, N):

        number = N

        finished = False

        for i in range(1, number):

            if finished == True:
                break

            for j in range(1, number):
                if i + j + sqrt(i*i + j*j) == number:
                    self.last_result = i * j * int(sqrt(i*i + j*j))
                    self.last_result_details = [i, j]
                    finished = True
                    break

            if i == number -1:
                pass
                self.last_result = -1


    def details(self):

        if self.last_result == -1:
            return("There is no pythagorean triplet for: " + str(self.last_input))
        else:

            desc_str = ""
            a = self.last_result_details[0]
            b = self.last_result_details[1]
            c = int(sqrt(a*a + b*b))

            res_add = a + b + c
            res_mult = a * b * c
            desc_str += (
                     str(a) + "   + " + str(b) + "   + " + str(c) + "   = " + dye_input_var(str(res_add)) + "\n" +
                     str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2 = " + str(c**2) + "\n" +
                     "\n" +
                     str(a) + " * " + str(b) + " * " + str(c) + " = " + dye_result_var(str(res_mult))
                    )

            return desc_str

register_problem(Problem_009())
