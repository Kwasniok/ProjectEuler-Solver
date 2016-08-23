#   coding=UTF_8
#
#   problem_026.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_026(Problem):

    def __init__(self):
        self.problem_nr = 26
        self.input_format = (InputType.NUMBER_INT, 4, 4000)
        self.default_input = 1000
        self.description_str = '''A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10   =     0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  ''' + dye_input_var(1000) + " for which 1/d contains the longest recurring cycle in its decimal fraction part.\n"


    def calculate(self, N):

        res = 0
        res_details = []
        longest_reurring_cycle = -1

        i = 2
        while i < N:

            number_part = 10
            remainders = []
            r_cycle_not_found = True

            while r_cycle_not_found:

                number_part = number_part % i

                if number_part == 0:
                    break

                for j in range(len(remainders)):

                    if number_part == remainders[j]:

                        if len(remainders) > longest_reurring_cycle:
                            longest_reurring_cycle = len(remainders)
                            res = i
                            res_details = [len(remainders), j]

                        r_cycle_not_found = False
                        break

                remainders.append(number_part)

                number_part *= 10

            i += 1


        self.last_result = res
        self.last_result_details = res_details

    def details(self):
        f_str = "0."
        n  = self.last_result # number
        rs = self.last_result_details[0] # amount of remainders
        cs = self.last_result_details[1] # cycle starting position
        np = 10 # number part
        i = 0
        while i < rs:
            if i == cs:
                f_str += "("
            f_str += str(np / n)
            np = np % n
            np *= 10
            i += 1
        f_str += ")"

        return "1/" + dye_result_var(self.last_result) + " = " + dye_highlight(f_str)

register_problem(Problem_026())
