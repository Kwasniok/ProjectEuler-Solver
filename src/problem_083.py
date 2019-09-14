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
        n = A.dim()[0]
        m = A.dim()[1]
        
        Problem_083.current_best = None

        def get_best_path(i=0, j=0, _p=[], _pv=0):
            
            pv = _pv + A[i,j]
            p = list(_p)
            p.append((i,j))
            
            if i == n - 1 and j == m - 1:
                if Problem_083.current_best is None or pv < Problem_083.current_best:
                    Problem_083.current_best = pv
                    print(pv)
                    print(A.fancy_ustr(highlight=p))
                return [p, pv]
        
            if (not (Problem_083.current_best is None)) and pv > Problem_083.current_best:
                return [None, None]



            branches = []

            go_up = True
            go_down = True
            go_left = True
            go_right = True

            # respect bounderies
            if i == 0:
                go_up = False
            if i == n - 1:
                go_down = False
            if j == 0:
                go_left = False
            if j == n - 1:
                go_right = False

            # avoid second visit of tile
            if (i-1,j) in p:
                go_up = False
            if (i+1,j) in p:
                go_down = False
            if (i,j-1) in p:
                go_left = False
            if (i,j+1) in p:
                go_right = False

            # avoid neighbouring previous visited tiles
            if (i-1,j-1) in p or (i-1,j+1) in p or (i-2,j) in p:
                go_up = False
            if (i+1,j-1) in p or (i+1,j+1) in p or (i+2,j) in p:
                down_up = False
            if (i-1,j-1) in p or (i+1,j-1) in p or (i,j-2) in p:
                left_up = False
            if (i-1,j+1) in p or (i+1,j+1) in p or (i,j+2) in p:
                right_up = False

            # iterate on remaining possible branching paths
            if go_right:
                branches.append(get_best_path(i, j+1, p, pv))
            if go_down:
                branches.append(get_best_path(i+1, j, p, pv))
            if go_up:
                branches.append(get_best_path(i-1, j, p, pv))
            if go_left:
                branches.append(get_best_path(i, j-1, p, pv))

            best_branch = None
            best_branch_value = None
            for pair in branches:
                branch = pair[0]
                branch_value = pair[1]

                if branch == None:
                    continue

                if best_branch == None:
                    best_branch = branch
                    best_branch_value = branch_value
                else:
                    if branch_value < best_branch_value:
                        best_branch = branch
                        best_branch_value = branch_value

            if best_branch == None:
                return [None, None]

            return [best_branch, best_branch_value]

        best_path_pair = get_best_path()

        # get optimal path value
        res = best_path_pair[1]
        # extract optimal path indices
        H = best_path_pair[0]

        self.last_result = res
        self.last_result_details = [A, H]
    def details(self):
        A = self.last_result_details[0]
        H = self.last_result_details[1]
        ret = "path: " + str(H)
        ret += "\n    " + A.fancy_ustr(highlight=H)
        return ret

register_problem(Problem_083())
