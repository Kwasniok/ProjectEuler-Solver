#   coding=UTF_8
#
#   problem_029.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#


from problem_000 import *

class Problem_029(Problem):
    
    def __init__(self):
        self.problem_nr = 29
        self.input_format = (InputType.LIST_OF, (InputType.NUMBER_INT, 2, 200), 1, 2)
        self.default_input = [100, 100]
        self.description_str = '''Consider all integer combinations of ab for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4,  2^3=8,   2^4=16,  2^5=32
3^2=9,  3^3=27,  3^4=81,  3^5=243
4^2=16, 4^3=64,  4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 <= a <= ''' + dye_input_var(100) + " and 2 <= b <= " + dye_input_var(100) + "?\n"

    def calculate(self, Ns):
        
        Na = Ns[0]
        if len(Ns) == 1:
            Nb = Na
        else:
            Nb = Ns[1]
        
        numbers = []
        a = 2
        while a <= Na:
            b = 2
            while b <= Nb:
                n = a**b
                if not n in numbers:
                    numbers.append(n)
                b += 1
            a += 1
            
        self.last_result = len(numbers)
        
register_problem(Problem_029())
        