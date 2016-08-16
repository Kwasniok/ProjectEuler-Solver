#   coding=UTF_8
#
#   problem_018.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import log10
 
class Problem_018(Problem):
    
    def __init__(self):
        self.problem_nr = 18
        self.demo_triangle = [[3],
                             [7, 4],
                             [2, 4, 6],
                             [8, 5, 9, 3]]
        self.demo_highlight = [(0,0), (1, 0), (2, 1), (3, 2)]
        self.triangle = [[75],
                         [95, 64],
                         [17, 47, 82],
                         [18, 35, 87, 10],
                         [20, 04, 82, 47, 65],
                         [19, 01, 23, 75, 03, 34],
                         [88, 02, 77, 73, 07, 63, 67],
                         [99, 65, 04, 28, 06, 16, 70, 92],
                         [41, 41, 26, 56, 83, 40, 80, 70, 33],
                         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                         [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                         [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                         [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                         [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]
        self.description_str = "By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.\n\n" + self.trinagle_to_str(self.demo_triangle, 1, self.demo_highlight) + '''

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below: \n\n''' + self.trinagle_to_str(self.triangle, 2) + "\n"
    
    def calculate(self, unused):
        
        def find_path(r, c):
            sum = self.triangle[r][c]
            best_path = [(r, c)]
            
            # has next row
            if r+1 < len(self.triangle):
                
                l = find_path(r+1, c)
                r = find_path(r+1, c+1)
                if l >= r:
                    sum += l[0]
                    best_path += l[1]
                else:
                    sum += r[0]
                    best_path += r[1]
                    
            return [sum, best_path]
        
        path = find_path(0, 0)
        
        self.last_result = path[0]
        self.last_result_details = path[1]
        
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
   
register_problem(Problem_018())
