#   coding=UTF_8
#
#   problem_048.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *


class Problem_048(Problem):
    
    def __init__(self):
        self.problem_nr = 48
        self.input_format = (InputType.NUMBER_INT, 1, 10000)
        self.default_input = 1000
        self.description_str = '''The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + ''' + dye_input_var(1000) + "^1000.\n"

    def calculate(self, N):
        
        sum = 0
        i = 1
        while i < N + 1:
            sum += i ** i
            i += 1
        
        res = ""
        ds = 10
        sum_str = str(sum)
        if len(sum_str) < ds:
            ds = len(sum_str)
        for i in range(0, ds):
            res += sum_str[len(sum_str) - ds + i]
        
        
        self.last_result = res
        self.last_result_details = (sum, ds)
        
    def details(self):
        
        sum = self.last_result_details[0]
        ds = self.last_result_details[1]
        
        sum_str = str(sum)
        
        return list_to_fancy_str(sum_str, highlightColour = Colours.RESULTVAR,
                              startHighlight = len(sum_str) - ds, endHighlight = len(sum_str))
        
register_problem(Problem_048())
