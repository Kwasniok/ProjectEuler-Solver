#   coding=UTF_8
#
#   problem_081.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.09.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_081_matrix import matrix
from matrix import *

class Problem_081(Problem):

    test_matrix = Matrix([[131, 673, 234, 103,  18],
           [201,  96, 342, 965, 150],
           [360, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]])

    def __init__(self):
        self.problem_nr = 81
        self.input_format = (InputType.CHOOSE_FROM_LIST, ['minimal', 'maximal'])
        self.default_input = 'minimal'
        self.description_str = 'In the 5 by 5 matrix below, the ' + dye_input_var('minimal') + ''' path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.\n'''
        self.description_str += "\n     " + self.test_matrix.fancy_ustr() + "\n"*self.test_matrix.dim()[0]
        self.description_str += '''\nFind the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.'''
        self.more_show_matrix = False

    def calculate(self, mode):

        res = 0

        # convert list to matrix
        A = Matrix(matrix)
        # dimensions of matrix in down and rigth direction
        n = A.dim()[0]
        m = A.dim()[1]
        # matrix storing the minimal path value for a path starting at this point
        V = Matrix(n, m)
        # optional flow chart
        F = Matrix(n, m)
        RIGHT = '>'
        DOWN  = 'v'
        STOP  = 'x'

        # all values are derived from a reversed path starting in the right bottom corner

        # initialze with trivial path
        V[n-1,m-1] = A[n-1,m-1]
        F[n-1,m-1] = STOP

        # fill in paths on the right and bottom (which have no branching)
        i = n - 2
        while i >= 0:
            V[i,m-1] = A[i,m-1] + V[i+1,m-1]
            F[i,m-1] = DOWN
            i -= 1
        j = m - 2
        while j >= 0:
            V[n-1,j] = A[n-1,j] + V[n-1,j+1]
            F[n-1,j] = RIGHT
            j -= 1

        # fill in remaing path values in the same manner
        i = n - 2
        while i >= 0:
            j = m - 2
            while j >= 0:
                r = V[i, j + 1]
                d = V[i + 1, j]
                if (mode == 'minimal' and r <= d) or (mode =='maximal' and r >= d):
                    V[i,j] = A[i,j] + r
                    F[i,j] = RIGHT
                else:
                    V[i,j] = A[i,j] + d
                    F[i,j] = DOWN
                j -= 1
            i -= 1

        # get optimal path value
        res = V[0,0]

        # extract optimal path indices
        i = 0
        j = 0
        H = []
        while True:
            nxt = F[i,j]
            H.append((i,j))
            if nxt == DOWN:
                i += 1
            elif nxt == RIGHT:
                j += 1
            else:
                break

        self.last_result_details = [A, F, H]
        self.last_result = res

    def details(self):
        self.more_show_matrix = not self.more_show_matrix
        A = self.last_result_details[0]
        F = self.last_result_details[1]
        H = self.last_result_details[2]
        if self.more_show_matrix:
            return "Type in " + dye_input_var("more") + " to get flow chart.\nmatrix:\n    " + A.fancy_ustr(highlight=H)
        else:
            return "Type in " + dye_input_var("more") + " to get matrix.\nflow chart:\n    " + F.fancy_ustr(highlight=H)

register_problem(Problem_081())
