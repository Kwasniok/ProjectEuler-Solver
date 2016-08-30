#   coding=UTF_8
#
#   problem_079.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on XX.XX.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_079_attempts import attempts

class Problem_079(Problem):

    def __init__(self):
        self.problem_nr = 79
        self.description_str = '''A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.'''

    def calculate(self, unused):

        # easy to solve even on paper without any algorithm!

        res = ""

        ## simple graph class
        class Graph():
            def __init__(self):
                self.nodes = []
                self.edges = set()
                return None
            ## returns all indices of nodes wich have no predecessor as list
            def get_head_node_indices(self):
                ret = []
                for i in range(len(self.nodes)):
                    is_head_node = True
                    for edge in self.edges:
                        if edge[1] == i:
                            is_head_node = False
                            break
                    if is_head_node:
                        ret.append(i)
                return ret
            ## removes a node from graph.
            # @note This method might alter the indices of the nodes.
            def remove_node(self, node_index):
                edges = set()
                for edge in self.edges:
                    if edge[0] != node_index and edge[1] != node_index:
                        i = edge[0]
                        j = edge[1]
                        if i > node_index:
                            i -= 1
                        if j > node_index:
                            j -= 1
                        edges.add((i,j))
                nodes = self.nodes[0:node_index] + self.nodes[node_index+1:len(self.nodes)]
                self.nodes = nodes
                self.edges = edges


        g = Graph()

        # store all information from attempts in directed graph
        # where each digits node points to the successors one
        # e.g. attempts ABC, DBE become:
        #          E
        #          ↑
        #      A → B → C
        #          ↑
        #          D
        for attempt in attempts:

            for d in attempt:
                if not d in g.nodes:
                    g.nodes.append(d)

            i = g.get_node_index(attempt[0])
            j = g.get_node_index(attempt[1])
            k = g.get_node_index(attempt[2])

            g.edges.add((i,j))
            g.edges.add((j,k))

        # The first (resp. next) digit is the one without any edge pointing to it.
        # If there is not exactly one node with this property the solution in ambiguous or there is none.
        while g.nodes != []:
            hns = g.get_head_node_indices()
            if len(hns) != 1:
                res = "data is ambiguous"
                break
            res += g.nodes[hns[0]]
            g.remove_node(hns[0])

        self.last_result = res

    def details(self):
        return "The attempts were:\n" + list_to_fancy_str(attempts, separator=",")

register_problem(Problem_079())
