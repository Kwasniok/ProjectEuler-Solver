#   coding=UTF_8
#
#   problem_006.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_006(Problem):

    def __init__(self):
        self.problem_nr = 6
        self.input_format = (InputType.NUMBER_INT, 0, 1000000000)
        self.default_input = 100
        self.description_str = '''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first ''' + dye_input_var("one hundred") +  " natural numbers and the square of the sum."


    def calculate(self, N):

        number = N

        sum_of_sqrts = 0
        sqrt_of_sum = 0

        for i in range(1, number + 1):
            sum_of_sqrts += i * i
        sqrt_of_sum = (int(number / 2 ) * (number +1))
        sqrt_of_sum *= sqrt_of_sum

        self.last_result = sqrt_of_sum - sum_of_sqrts

register_problem(Problem_006())
