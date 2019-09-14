#   coding=UTF_8
#
#   problem_021.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 22.06.17.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_082_matrix import matrix
from matrix import *

class Problem_082(Problem):

    test_matrix = Matrix([[131, 673, 234, 103,  18],
           [201,  96, 342, 965, 150],
           [360, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]])

    def __init__(self):
        self.problem_nr = 82
        self.input_format = (InputType.CHOOSE_FROM_LIST, ['small', 'large'])
        self.default_input = 'large'
        self.description_str = 'The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right [...] the sum is equal to 994..\n'''
        self.description_str += "\n     " + self.test_matrix.fancy_ustr() + "\n"*self.test_matrix.dim()[0]
        self.description_str += '''\nFind the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, from the left column to the right column.'''
        self.more_state = 0

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
        # matrix storing the minimal path value for a path starting at this point
        V = Matrix(n, m)
        # optional flow chart
        F = Matrix(n, m)
        RIGHT = u'▶'
        UP    = u'▲'
        DOWN  = u'▼'
        STOP  = u'⊠'

        # all values are derived from a reversed path starting at the right

        # initialze with trivial paths
        i = n - 1
        while i >= 0:
            V[i,m-1] = A[i,m-1]
            F[i,m-1] = STOP
            i -= 1

        # fill in remaing path values
        # scan all columns from right to left
        # all cells one column to the right contain the values for an optimal path starting at that cell
        j = m - 2
        while j >= 0:
            i = n - 1
            while i >= 0:

                # branch right
                r = V[i, j + 1]

                # branch up (compare all possible paths)
                u = None
                u_path = 0 # value of path just going up
                k = i - 1
                while k >= 0:
                    # update value of extended path
                    u_path += A[k, j]
                    # compare this path branching to the right to current optimal path
                    if u == None:
                        u = u_path + V[k, j + 1]
                    elif u_path + V[k, j + 1] <= u:
                        u = u_path + V[k, j + 1]
                    # extend path one step upwards
                    k -= 1

                # branch down (compare all possible paths)
                d = None
                d_path = 0 # value of path just going down
                k = i + 1
                while k <= n-1:
                    # update value of extended path
                    d_path += A[k, j]
                    # compare this path branching to the right to current optimal path
                    if d == None:
                        d = d_path + V[k, j + 1]
                    elif d_path + V[k, j + 1] <= d:
                        d = d_path + V[k, j + 1]
                    # extend path one step downwards
                    k += 1

                # find optimal path within the possible branching options

                # all branching directions possible
                if u != None and d != None:
                    if r <= u and r <= d:
                        V[i,j] = A[i,j] + r
                        F[i,j] = RIGHT
                    if u <= r and u <= d:
                        V[i,j] = A[i,j] + u
                        F[i,j] = UP
                    if d <= r and d <= u:
                        V[i,j] = A[i,j] + d
                        F[i,j] = DOWN

                # branching up and right only
                if u == None and d != None:
                    if r <= d:
                        V[i,j] = A[i,j] + r
                        F[i,j] = RIGHT
                    if d <= r:
                        V[i,j] = A[i,j] + d
                        F[i,j] = DOWN

                # branching down and right only
                if u != None and d == None:
                    if r <= u:
                        V[i,j] = A[i,j] + r
                        F[i,j] = RIGHT
                    if u <= r:
                        V[i,j] = A[i,j] + u
                        F[i,j] = UP

                # branching right only
                if u == None and d == None:
                    V[i,j] = A[i,j] + r
                    F[i,j] = RIGHT

                i -= 1
            j -= 1

        # get optimal path value
        res = V[0,0]
        start = 0
        i = 1
        while i <= n-1:
            if V[i,0] <= res:
                res = V[i,0]
                start = i
            i += 1

        # extract optimal path indices
        i = start
        j = 0
        H = []
        while True:
            nxt = F[i,j]
            H.append((i,j))
            if nxt == DOWN:
                i += 1
            elif nxt == UP:
                i -= 1
            elif nxt == RIGHT:
                j += 1
            else:
                break

        self.last_result = res
        self.last_result_details = [A, F, V, H]
        self.more_state = 0

    def details(self):
        A = self.last_result_details[0]
        F = self.last_result_details[1]
        V = self.last_result_details[2]
        H = self.last_result_details[3]
        if self.more_state == 0:
            ret = "Type in " + dye_input_var("more") + " to get flow chart.\nmatrix:\n    " + A.fancy_ustr(highlight=H)
        elif self.more_state == 1:
            ret =  "Type in " + dye_input_var("more") + " to get flow chart.\nmatrix:\n    " + V.fancy_ustr(highlight=H)
        else:
            ret = "Type in " + dye_input_var("more") + " to get matrix.\nflow chart:\n    " + F.fancy_ustr(highlight=H)
        self.more_state = (self.more_state + 1) % 3
        return ret

register_problem(Problem_082())
