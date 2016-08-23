#   coding=UTF_8
#
#   problem_022.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_string import worth_of_string
import problem_022_names

class Problem_022(Problem):

    def __init__(self):
        self.problem_nr = 22
        self.description_str = '''Using names.txt [see more], a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x  53 = 49714.

What is the total of all the name scores in the file?
'''

    def calculate(self, unused):

        sum = 0

        all_names = sorted(problem_022_names.all_names())

        for i in range(0, len(all_names)):
            sum += (i+1) * worth_of_string(all_names[i])

        self.last_result = sum


    def details(self):
        desc_str = ""
        for n in problem_022_names.all_names():
            desc_str += n  + " "
        return desc_str + "\npew ...\n"

register_problem(Problem_022())
