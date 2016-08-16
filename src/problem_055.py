#   coding=UTF_8
#
#   problem_055.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_palindrome

class Problem_055(Problem):

    def __init__(self):
        self.problem_nr = 55
        self.input_format = (InputType.NUMBER_INT, 1, 10000)
        self.default_input = 10000
        self.description_str = '''If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ''' + dye_input_var("ten-thousand") + '''?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
'''

    def calculate(self, N):

        sum = 0
        sum_Details = []

        def nextLychrelIteration(n):
            nStr_r = str(n)[::-1]
            return int(n + int(nStr_r))

        n = 1
        while n < N:

            isLychrel = True
            i = 0
            ni = n
            while isLychrel and i < 50:

                ni = nextLychrelIteration(ni)

                if is_palindrome(str(ni)):
                    isLychrel = False

                i += 1

            if isLychrel:
                sum += 1
                sum_Details.append(n)

            n += 1

        self.last_result = sum
        self.last_result_details = sum_Details

    def details(self):
        return "All Lychrel numbers below " + dye_input_var(self.last_input) + " are:\n" + list_to_fancy_str(self.last_result_details, ", ")

register_problem(Problem_055())
