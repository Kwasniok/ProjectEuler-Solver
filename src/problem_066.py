#   coding=UTF_8
#
#   problem_066.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import sqrt
from ppe_math import get_continued_fraction_for_sqrt_of

class Problem_066(Problem):

    def __init__(self):
        self.problem_nr = 66
        self.input_format = (InputType.NUMBER_INT, 2, 10000)
        self.default_input = 1000
        self.description_str = '''Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
''' + dye_highlight(9) + '''^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ ''' + dye_input_var(1000) + ''' in minimal solutions of x for which the largest value of x is obtained.
'''

    def calculate(self, N):

        D_min_max = None
        F_min_max = None
        D = N
        while D > 1:

            if sqrt(D) % 1.0 != 0.0: # is not a square

                cf = get_continued_fraction_for_sqrt_of(D)
                #print(cf)

                k = -1
                while True:
                    k += 1
                    #print(k)

                    F = cf.getApproximation(k)
                    x = F.numerator
                    y = F.denominator
                    #print(F)

                    if x**2 - D*y**2 == 1:
                        #print(str(int(D)) + ";" + str(x))
                        if D_min_max == None or x > F_min_max.numerator:
                            D_min_max = D
                            F_min_max = F
                        break

            D -= 1
            
        self.last_result = D_min_max
        self.last_result_details = F_min_max

    def details(self):
        D = self.last_result
        x = self.last_result_details.numerator
        y = self.last_result_details.denominator
        return "D = " + dye_result_var(D) + ", x = " + dye_highlight(x) + ", y = " + str(y)

register_problem(Problem_066())
