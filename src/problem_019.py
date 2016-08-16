#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from date import is_leap_year, Date

class Problem_019(Problem):
    
    def __init__(self):
        self.problem_nr = 19
        self.input_format = (InputType.LIST_OF, (InputType.DATE, Date(1582, 10, 15), None), 2, 2)
        self.default_input = [Date(1901, 1, 1), Date(2000, 12, 31)]
        self.description_str = '''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (''' + dye_input_var(self.default_input[0].get_date_as_string()) + " to " + dye_input_var(self.default_input[1].get_date_as_string()) + "?\n"
    
    def calculate(self, Ds):
        
        start_date = Ds[0]
        end_date = Ds[1]
        self.last_result_details = [start_date.get_date_as_string(), end_date.get_date_as_string()]
        
        res = 0
        
        while start_date.get_weekday() != "Sunday":
            start_date.add_days()
        self.last_result_details.append(start_date.get_date_as_string())
        
        while start_date.get_date() <= end_date.get_date():
            if start_date.get_date()[2] == 1:
                res += 1
            start_date.add_days(7)
            
        self.last_result = res
        self.last_result_details.append(start_date.get_date_as_string())
        
    
    def details(self):
        return "Between " + dye_input_var(self.last_result_details[0]) + " and " + dye_input_var(self.last_result_details[1]) + " are " + dye_result_var(self.last_result) + " Sundays falling on the first day of a month\nfirst Sunday in this period:" + self.last_result_details[2] + " last:" + self.last_result_details[3]
        
register_problem(Problem_019())

