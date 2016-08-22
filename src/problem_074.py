#   coding=UTF_8
#
#   problem_074.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 19.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import faculty
from util import list_to_fancy_str

class Problem_074(Problem):

    def __init__(self):
        self.problem_nr = 74
        self.input_format = (InputType.TUPLE_HETEROGENE, 2, (InputType.NUMBER_INT, 1, 1000000), (InputType.NUMBER_INT, 1, 60))
        self.default_input = (1000000, 60)
        self.description_str = '''The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below ''' + dye_input_var("one million") + ''', contain exactly ''' + dye_input_var("sixty") + ''' non-repeating terms?'''

    def calculate(self, vs):

        res = 0
        res_details = []

        # Since each permutation of a number has the same chain length the algorithm could be much faster by making
        # use of this fact. (Must exclude leading zeros and duplicate digits!, 0! = 1!) Nevertheless it's fast enough.
        n_max = vs[0]
        lim = vs[1]
        n = 0
        while n < n_max:
            ns = [n]
            m = n
            while True:
                s = 0
                while m != 0:
                    s += faculty(m % 10)
                    m /= 10
                if s in ns:
                    if len(ns) == lim:
                        res += 1
                        res_details.append(n)
                    break
                if len(ns) == lim:
                    break
                ns.append(s)
                m = s

            n += 1

        self.last_result = res
        self.last_result_details = res_details

    def details(self):
        return "list of all starting numbers:\n" + list_to_fancy_str(self.last_result_details, separator=',')

register_problem(Problem_074())
