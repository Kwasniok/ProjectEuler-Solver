#   coding=UTF_8
#
#   problem_003.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_003(Problem):

    def __init__(self):
        self.problem_nr = 3
        self.input_format = (InputType.NUMBER_INT, 0, 1000000000000000)
        self.default_input = 600851475143
        self.description_str = '''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number ''' + dye_input_var(600851475143) + "?."

    def fac_of_number(self, number):
        dividors = []

        i = 2
        while i < number:
            if number % i == 0:
                k = self.fac_of_number(i)
                for l in k:
                    dividors.append(l)
                m = self.fac_of_number(int(number / i))
                for n in m:
                    dividors.append(n)
                return dividors

            i += 1

        dividors.append(number)
        return dividors

    def calculate(self, N):

        self.last_result_details = self.fac_of_number(N)
        self.last_result = int(self.last_result_details[len(self.last_result_details) - 1])

    def details(self):
        res_str = ("The prime factors of " + dye_input_var(self.last_input) + " are:\n" + dye_input_var(self.last_input) + " = ")
        for i in range(0, len(self.last_result_details) - 1):
            res_str += str(self.last_result_details[i])
            res_str += " * "
        res_str += dye_result_var(self.last_result)
        return res_str

register_problem(Problem_003())
