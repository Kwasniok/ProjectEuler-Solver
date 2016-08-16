#   coding=UTF_8
#
#   problem_017.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_017(Problem):

    def __init__(self):
        self.problem_nr = 17
        self.input_format = (InputType.NUMBER_INT, 1, 9999)
        self.default_input = 1000
        self.description_str = '''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to ''' + dye_input_var(1000) + ''' (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''

    def calculate(self, N):

        def get_len_single(number):
            #sum 36
            if number == 0:
                return 0
            if number == 1 or number == 2 or number == 6:
                return 3
            if number == 4 or number == 5 or number == 9:
                return 4
            if number == 3 or number == 7 or number == 8:
                return 5

        def get_len_ten_plus(number):
            #sum 72
            if number == 10:
                return 3
            if number == 11 or number == 12:
                return 6
            if number == 15 or number == 16:
                return 7
            if number == 13 or number == 14 or number == 18 or number == 19:
                return 8
            if number == 17:
                return 9

        def get_len_double(number):
            if number < 10:
                return get_len_single(number)
            if 9 < number < 20:
                return get_len_ten_plus(number)
            if 19 < number and number < 40 or 79 < number and number < 100:
                return 6 + get_len_single(int(str(number)[-1]))
            if 39 < number and number < 70:
                return 5 + get_len_single(int(str(number)[-1]))
            if 69 < number and number < 80:
                return 7 + get_len_single(int(str(number)[-1]))

        def get_len_houndred(number):
            if number < 100:
                return get_len_double(number)
            if int(str(number)[1])*10 + int(str(number)[2]) == 0:
                return get_len_single(int(str(number)[0])) + 7
            if 99 < number:
                return get_len_single(int(str(number)[0])) + 10 + get_len_double(int(str(number)[1])*10 + int(str(number)[2]))

        def get_len_thousand(number):
            if number < 1000:
                return get_len_houndred(number)
            if int(str(number)[1])*100 + int(str(number)[2])*10 + int(str(number)[3]) == 0:
                return get_len_single(int(str(number)[0])) + 8
            if 999 < number:
                return get_len_single(int(str(number)[0])) + 11 + get_len_houndred(int(str(number)[1])*100 + int(str(number)[2])*10 + int(str(number)[3]))

        res = 0
        i = 1
        while i < N + 1 :
            string = str(i)
            res +=  get_len_thousand(i)
            i += 1

        self.last_result = res

register_problem(Problem_017())
