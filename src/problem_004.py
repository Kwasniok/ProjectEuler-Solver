#   coding=UTF_8
#
#   problem_000.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_004(Problem):

    def __init__(self):
        self.problem_nr = 4
        self.input_format = (InputType.NUMBER_INT, 0, 7)
        self.default_input = 3
        self.description_str = '''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two ''' + dye_input_var(3) + "-digit numbers."

    def is_palindrome(self, number):
        number_str = str(number)
        mirrored_number_str = ""
        for c in range(len(number_str) -1 , -1, -1):
            mirrored_number_str += number_str[c]
        return mirrored_number_str == number_str

    def calculate(self, N):

        largest_number = int('9'*N)

        checked_area_i = 0
        finished = False
        fac = int('1'+'0'*(N-1))

        for i in range(largest_number - checked_area_i, largest_number - checked_area_i - fac, -1):
            if finished == True:
                break

            checked_area_j = 0

            for j in range(largest_number - checked_area_j, largest_number - checked_area_j - fac, -1):

                k = i * j

                if self.is_palindrome(k):
                    self.last_result = k
                    self.last_result_details = [i, j]
                    finished = True
                    break

                checked_area_j += fac

            checked_area_i += fac

    def details(self):
        return ("Largest palindrome made from the product of two " + dye_input_var(self.last_input) + "-digit numbers is:\n" + dye_result_var(self.last_result) + " = " + str(self.last_result_details[0]) + " * " + str(self.last_result_details[1]))

register_problem(Problem_004())
