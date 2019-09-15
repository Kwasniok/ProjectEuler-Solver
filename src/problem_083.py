#   coding=UTF_8
#
#   problem_083.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 28.06.17.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

import sys
from problem_000 import *
from problem_083_matrix import matrix
from matrix import *
from math import inf as infinity, isnan

sys.setrecursionlimit(100000)

class Problem_083(Problem):

    test_matrix = Matrix([[131, 673, 234, 103,  18],
           [201,  96, 342, 965, 150],
           [360, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]])

    def __init__(self):
        self.problem_nr = 83
        self.input_format = (InputType.CHOOSE_FROM_LIST, ['small', 'large'])
        self.default_input = 'large'
        self.description_str = 'In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down [...] is equal to 2297.\n'''
        self.description_str += "\n     " + self.test_matrix.fancy_ustr() + "\n"*self.test_matrix.dim()[0]
        self.description_str += '''\nFind the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.'''

    def calculate(self, mode):

        res = 0

        # chosse matrix
        if mode == 'small':
            A = self.test_matrix
        if mode == 'large':
            A = Matrix(matrix)
        # dimensions of matrix in down and rigth direction
        m = A.dim()[0]
        n = A.dim()[1]
        
        mp = Matrix(m, n, default_value=infinity)
        mp[0,0] = A[0,0]
        
        mp_swap = Matrix(m, n, default_value=None)
        
        for x in range(m*n): # max iteration number
            
            #print(mp.fancy_ustr())
            
            for i in range(m):
                for j in range(n):
                    vs = []
                    if i > 0: vs.append(mp[i-1,j] + A[i,j])
                    if j > 0: vs.append(mp[i,j-1] + A[i,j])
                    if i < m-1: vs.append(mp[i+1,j] + A[i,j])
                    if j < n-1: vs.append(mp[i,j+1] + A[i,j])
                    vs.append(mp[i,j])
                    mp_swap[i,j] = min(vs)
        
            if mp == mp_swap: # stable?
                break
            
            mp, mp_swap = mp_swap, mp

        self.last_result = mp[n-1,m-1]

register_problem(Problem_083())
