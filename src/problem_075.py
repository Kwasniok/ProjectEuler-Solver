#   coding=UTF_8
#
#   problem_075.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 20.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from matrix import Matrix, Vector

class Problem_075(Problem):

    def __init__(self):
        self.problem_nr = 75
        self.input_format = (InputType.NUMBER_INT, 12, 2000000)
        self.default_input = 1500000
        self.description_str = '''It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

        12 cm: (3,4,5)
        24 cm: (6,8,10)
        30 cm: (5,12,13)
        36 cm: (9,12,15)
        40 cm: (8,15,17)
        48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ ''' + dye_input_var("1,500,000") + ''' can exactly one integer sided right angle triangle be formed?'''

    def calculate(self, l_max):

        res = 0

        # The following algoritm bases on http://mathworld.wolfram.com/PythagoreanTriple.html

        # first pythagorean triple
        triple_first = Vector([3, 4, 5])
        # list of frequency of length
        l_frequency = dict({12 : 1})

        # matrices to create 3 new primitive distinct (and non-repeating) pythagorean triples from primitive triple
        matries = [Matrix([[1, 2, 2], [2, 1, 2], [2, 2, 3]])]
        matrices += [Matrix([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])]
        matrices += [Matrix([[1, 2, 2], [-2, -1, -2], [2, 2, 3]])]

        # generates multiples of given primitive tiple and new primitive triples
        # and checks their length to update frequency
        def next_triples(triple):
            # get length of current primitive triple
            l_triple = sum(triple)
            # check multiples of this triple
            i = 2
            while l_triple * i <= l_max:
                l_ = l_triple * i
                if l_ in l_frequency:
                    l_frequency[l_] += 1
                else:
                    l_frequency[l_] = 1
                i += 1
            # generate new primitive triples and check them as well
            for m in matries:
                triple_new = triple * m
                l = sum(triple_new)
                if l <= l_max:
                    if l in l_frequency:
                        l_frequency[l] += 1
                    else:
                        l_frequency[l] = 1

                    next_triples(triple_new)

        next_triples(triple_first)

        for l in l_frequency.items():
            if l[1] == 1:
                res += 1

        self.last_result = res

register_problem(Problem_075())
