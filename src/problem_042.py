#   coding=UTF_8
#
#   problem_042.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_042_words import words
from ppe_math import worth_of_string
from math import sqrt

class Problem_042(Problem):
    
    def __init__(self):
        self.problem_nr = 42
        self.description_str = '''The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
    
    def calculate(self, unused):
        
        sum = 0
        
        # from t_n = 1/2 * n * (n + 1) follows 0 = n^2 + n - 2*t_n
        # so t_n is a triangle number if n = -1/2 + √(1/4 + 2*t_n) is an integer
        for w in words:
            v = worth_of_string(w)
            n = -0.5 + sqrt(0.25 + 2*v)
            if n % 1 == 0.0:
                sum += 1
        
        self.last_result = sum
        
    def details(self):
        desc_str = "content of words.txt:\n"
        
        i = 0
        while i < len(words):
            desc_str += words[i]
            if i < len(words) - 1:
                desc_str += ", "
            i += 1
        
        return desc_str
        
register_problem(Problem_042())
