#   coding=UTF_8
#
#   problem_085.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 17.09.19.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import sqrt

class Problem_085(Problem):

    def __init__(self):
        self.problem_nr = 85
        self.input_format = (InputType.NUMBER_INT, 1, 100000000)
        self.default_input = 2000000
        # ┏━┓ ┃ ━┗━┛ ┣ ┫ ┳ ┻ ╋
        # ┌─┐ │ ─└─┘ ├ ┤ ┬ ┴ ┼
        self.description_str = '''By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
    ┏┓   ┏┳┓  ┏┳┳┓
    ┗┛   ┗┻┛  ┗┻┻┛
      6    4    2
    ┏┓   ┏┳┓  ┏┳┳┓
    ┣┫   ┣╋┫  ┣╋╋┫
    ┗┛   ┗┻┛  ┗┻┻┛
      3    2    1

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.'''

    def calculate(self, target):

        res = 0
        self.last_result_details = ''

        # m = 3
        # n = 2
        # for k in range(1, m+1):
        #     for l in range(1, n+1):
        #         res += (m+1-k)*(n+1-l)
        def g(n):
            # s = 0
            # for l in range(1, n+1):
            #     s += n+1-l
            # return s
            return int(n*(n+1)/2)
        # def f(m,n):
        #     if m == 1 and n == 1:
        #         return 1
        #     if m > 1:
        #         return f(m-1, n) + m*g(n)
        #     else:
        #         return f(n-1, m) + n*g(m)
        #
        # res = f(m,n)

        # calculate v(m) = (f(m,1), ..., f(m,m)) iteratively
        v = [1]
        best_diff = target
        best = (1,1,1)
        # lower bound: f(m,n) >= f(m,1) = m*(m+1)/2
        m_max = int(-0.5+sqrt(0.25+2*target) +1) # +1 to be safe
        for m in range(1,m_max):
            if (m+1) % 1000 == 0: print(m+1)
            for n in range(m):
                # calculate f(m+1,n) = f(m,n) + (m+1)*g(n)
                x = v[n] + (m+1)*g(n+1)
                v[n] = x
                diff = abs(x-target)
                if diff < best_diff:
                    best = (m+1,n+1,x)
                    best_diff = diff

            # calculate f(m+1,m+1) = f(m+1, m) + (m+1)*g(m+1)
            x = v[m-1] + (m+1)*g(m+1)
            v.append(x)
            diff = abs(x-target)
            if diff < best_diff:
                best = (m+1,m+1,x)
                best_diff = diff

        res = best[0] * best[1]

        self.last_result = res
        self.last_result_details = best

    def details(self):
        m = self.last_result_details[0]
        n = self.last_result_details[1]
        x = self.last_result_details[2]
        return 'm = ' + str(m) + ', n = ' + str(n) + ', combinations = ' + str(x)

register_problem(Problem_085())
