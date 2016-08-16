#   coding=UTF_8
#
#   problem_067.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_067_triangle import triangle
from math import log10

class Problem_067(Problem):
    
    def __init__(self):
        self.problem_nr = 67
        self.demo_triangle = [[3],
                             [7, 4],
                             [2, 4, 6],
                             [8, 5, 9, 3]]
        self.demo_highlight = [(0,0), (1, 0), (2, 1), (3, 2)]
        self.triangle = triangle
        self.description_str = "By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.\n\n" + self.trinagle_to_str(self.demo_triangle, 1, self.demo_highlight) + '''

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
        '''
    
    def calculate(self, N):
        
        # create empty copy of triangle
        dataTriangle = []
        for r in self.triangle:
            R = []
            for c in r:
                R.append(None)
            dataTriangle.append(R)
        
        # copy last row
        c = 0
        lr = len(self.triangle) - 1 # last row
        while c < len(self.triangle[lr]):
            dataTriangle[lr][c] = self.triangle[lr][c]
            c += 1
            
        # fill rows from bottom to top by adding the current value to the best sub path value
        r = lr - 1
        while r > -1:
            c = 0
            while c < len(self.triangle[r]):
                if dataTriangle[r + 1][c] > dataTriangle[r + 1][c + 1]:
                    sum = self.triangle[r][c] + dataTriangle[r + 1][c]
                else:
                    sum = self.triangle[r][c] + dataTriangle[r + 1][c + 1]
                dataTriangle[r][c] = sum
                c += 1
            r -= 1
        
        #print(self.trinagle_to_str(dataTriangle, len(str(dataTriangle[0][0]))))
        
        # calculate path (for details only)
        r = 0
        c = 0
        path = [(0,0)]
        while r <= lr - 1:
            if dataTriangle[r + 1][c] > dataTriangle[r + 1][c + 1]:
                path.append((r + 1, c))
            else:
                path.append((r + 1, c + 1))
                c += 1
            r += 1
            
        self.last_result = dataTriangle[0][0]
        self.last_result_details = path
        
    def trinagle_to_str(self, triangle, space_width, highlight = []):
        desc_str = ""
        
        r = 0
        while r < len(triangle):
            desc_str += " " * space_width * (len(triangle) -1 - r)
            
            c = 0
            while c < len(triangle[r]):
                n = triangle[r][c]
                # alignment
                nStr = '0' * (space_width - int(log10(n) + 1.0)) + str(n)
                # add number
                if (r, c) in highlight:
                    desc_str += dye_highlight(nStr)
                else:
                    desc_str += nStr
                desc_str += " " * space_width
                
                c += 1
                
            desc_str += '\n'
            r += 1
            
        return desc_str
    
    def details(self):
        return self.trinagle_to_str(self.triangle, 2, self.last_result_details)
        
register_problem(Problem_067())

'''  attempt #2
def findSubPath(n, av, r, c, path, sum):
            sum += self.triangle[r][c]
            path += [(r, c)]
            
            if len(path) % n == 0:
                if (float(sum) / float(len(path))) < av:
                    return [-1, None]
                else:
                    return [sum, path]
                #print(path)
            
            
            # has next row
            if r+1 < len(self.triangle):
                
                retL = findSubPath(n, av, r+1, c, list(path), sum)
                retR = findSubPath(n, av, r+1, c+1, list(path), sum)
                if retL[0] > retR[0]:
                    return retL
                else:
                    return retR
            else:
                return [sum, path]
            
        def getAv(n, R, C):
            sum = 0.0
            count = 0.0
            r = 0
            while r < n and R + r < len(self.triangle) - 1:
                c = 0
                while c <= r:
                    sum += self.triangle[R + r][C + c]
                    count += 1
                    c += 1
                r += 1
            return sum / count
        
        def find_path(n):
            path = [(0, 0)]
            sum = self.triangle[0][0]
            r = 0
            c = 0
            while r + 1 < len(self.triangle) - 1:
                
                subPathL = [-1, None]
                subPathR = [-1, None]
                av = getAv(n, r, c)
                while subPathL[0] == -1 and subPathR[0] == -1:
                    subPathL = findSubPath(n, av, r + 1, c, [], 0)
                    subPathR = findSubPath(n, av, r + 1, c + 1, [], 0)
                    av -= 1.0
                
                if subPathL[0] > subPathR[0]:
                    sum += subPathL[0]
                    path += subPathL[1]
                else:
                    sum += subPathR[0]
                    path += subPathR[1]
                
                r = path[len(path) - 1][0] # last row
                c = path[len(path) - 1][1] # last column
                
            return [sum, path]
        
        path = find_path(N)
        
        self.last_result = path[0]
        self.last_result_details = path[1]
'''

''' attempt #1
# get average
        sum = 0
        count = 0
        for r in self.triangle:
            for c in r:
                sum += c
                count += 1
                
        av = float(sum) / float(count)
        global pc
        pc = 0
        
        def find_path(r = 0, c = 0, path = [], sum = 0):
            sum += self.triangle[r][c]
            path += [(r, c)]
            
            if len(path) % N == 0:
                if (float(sum) / float(len(path))) < av:
                    return [-1, None]
                #print(path)
            
            
            # has next row
            if r+1 < len(self.triangle):
                
                # can branch right
                if c+1 < len(self.triangle[r+1]):
                    retL = find_path(r+1, c, list(path), sum)
                    retR = find_path(r+1, c+1, list(path), sum)
                    if retL[0] > retR[0]:
                        return retL
                    else:
                        return retR
                else:
                    return find_path(r+1, c, list(path), sum)
            else:
                global pc
                pc += 1
                return [sum, path]
        
        path = find_path()
        print(str(pc) + " => " + str(float(pc) / float(2**(len(triangle) - 1))))
        
        self.last_result = path[0]
        self.last_result_details = path[1]
'''
