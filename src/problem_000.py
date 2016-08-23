#   coding=UTF_8
#
#   problem_000.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from sys import stdout
from time import time
from input_format import *
from util import list_to_fancy_str


##############
#BasicProblem#
##############

## root class for all problems
class Problem:

    # overwrite:
    problem_nr = 0 # must be overwritten
    # optional overwrite:
    description_str = None
    input_format = None # e.g. (InputType.NUMBER_INT, 0, 1) see input_format.py
    default_input = None
    supports_details = False

    # internal:
    last_input = None # is set automatically
    last_result = None # is set manually in calculateProblemWith / automatically printed
    last_result_details = None # is set manually in calculateProblemWith / manually printed with text

    ## sets the attributes including problem_nr, decriptionStr, input_format etc.
    def __init__(self):
        self.problem_nr = None

    ## returns true if problem supports userdefined input
    def supports_input(self):
        return self.input_format != None

    # should return true if any allowed input results in execution longer than 1 minute
    def should_warn_long_execution_time(self):
        return False

    def pre_calculate(self, last_input):
        self.last_result = None
        self.last_result_details = None
        self.last_input = last_input

    ## contains the solving algorithm for the problem (muste be overwritten)
    def calculate(self, input):
        pass

    def post_calculate(self):
        stdout.write("%s\n" % dye_result_var(self.last_result))

    ## calles the solving algorithm for this problem (use this method for external handling)
    def execute(self, input=None):
        self.pre_calculate(input)
        self.calculate(input)
        self.post_calculate()

    ## returns either a description or a 'not available' message
    def description(self):
        if self.description_str != None:
            return self.description_str
        else:
            return " - no description available - "

    ## returns the answer as dyed string
    def answer(self):
        return dye_result_var(self.last_result)

    ## returns either some details to the solution or a 'not available' message
    def details(self):
        return " - no details available - "

    ## returns the corresponding url on ProjectEuler.net
    def url(self):
        return "http://projecteuler.net/problem=" + str(self.problem_nr)

    ## returns a small description of the input format
    def usage(self):
        if self.supports_input():
            return usage_text_for_input_format(self.input_format)
        else:
            return "only input is allowed"


#######################
# Map of All Problems #
#######################

## global list of all registered problems
glob_problems = {}

## call once per problem to register it
def register_problem(p):
    glob_problems.update({p.problem_nr:p})
