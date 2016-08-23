#   coding=UTF_8
#
#   problem_052.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from number import get_digit_list

class Problem_052(Problem):

    def __init__(self):
        self.problem_nr = 52
        self.input_format = (InputType.NUMBER_INT, 1, 6)
        self.default_input = 6
        self.description_str = '''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
	def should_warn_long_execution_time(self):
		return True

    def calculate(self, N):

        res = 0

        n = 1
        cont = True
        while cont:

            #print(n)

            nList = get_digit_list(n)

            i = 2
            while i <= N:

                niList = get_digit_list(n * i)

                l = 0
                while l < 10:
                    if nList.count(l) != niList.count(l):
                        i = N + 1
                        break
                    l += 1

                i += 1

            if i == N + 1:
                res = n
                cont = False

            n += 1

        self.last_result = res

    def details(self):
        desc_str = ""
        n = self.last_result
        N = self.last_input
        for i in range(1, N + 1):
            desc_str += str(n) + " * " + str(i) + " = " + str(n * i)
            if i < N:
                desc_str += '\n'
        return desc_str

register_problem(Problem_052())
