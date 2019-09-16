#   coding=UTF_8
#
#   problem_084.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.09.19.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
import random
from util import list_to_fancy_str

class Problem_084(Problem):

    def __init__(self):
        self.problem_nr = 84
        self.input_format = (InputType.NUMBER_INT, 2, 6)
        self.default_input = 4
        self.description_str = '''In the game, Monopoly, the standard board is set up in the following way:

    GO  A1  CC1  A2  T1  R1  B1  CH1  B2  B3  JAIL
    H2                                        C1
    T2                                        U1
    H1                                        C2
    CH3                                       C3
    R4                                        R2
    G3                                        D1
    CC3                                       CC2
    G2                                        D2
    G1                                        D3
    G2J  F3  U2  F2  F1  R3  E3  E2  CH2  E1  FP

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.'''

    def calculate(self, dice_size):

        res = ''

        def diff(a, b):
            return sum([abs(i - j) for i,j in zip(a,b)])
        def props(freqs, its):
            return [float(f)/float(its) for f in freqs]
        def roll(dice_size):
            return random.randrange(dice_size) + 1

        field_tags = [
                'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
                'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
                'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
                'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
            ]
        board_size = len(field_tags)
        field_ids = dict(zip(field_tags, range(board_size)))
        max_sample_size = 10000000
        field_frquencies = [0] * board_size
        heuristic_field_props = [-1] * board_size
        heuristic_field_props_old = [-2] * board_size
        current_field_nr = 0
        doubles_counter = 0
        iterations = 0
        epsilon = 0.000001 * board_size
        while True:
            iterations += 1
            # check convergence
            if iterations % 100000 == 0:
                heuristic_field_props = props(field_frquencies, iterations)
                delta = diff(heuristic_field_props, heuristic_field_props_old)
                print(list_to_fancy_str(['%.2f' % (prop * 100) for prop in heuristic_field_props],
                      separator = ' '))
                print('delta = ' + str(delta))
                if delta < epsilon:
                   break
                heuristic_field_props_old = heuristic_field_props[:] # copy
            # roll dices
            d1 = roll(dice_size)
            d2 = roll(dice_size)
            d = d1 + d2
            # count doubles
            if d1 == d2:
                doubles_counter += 1
            else:
                doubles_counter = 0
            # to jail because of doubles
            if doubles_counter == 3:
                doubles_counter = 0
                current_field_nr = field_ids['JAIL']
            else:
                # advance by rolled value
                current_field_nr = (current_field_nr + d) % board_size
                # effects of special fields
                field_tag = field_tags[current_field_nr]
                # go to jail
                if field_tag == 'G2J':
                    current_field_nr = field_ids['JAIL']
                # community chest: go to field
                if field_tag.startswith('CC'):
                    d16 = roll(16)
                    if d16 == 1:
                        current_field_nr = field_ids['GO']
                    if d16 == 2:
                        current_field_nr = field_ids['JAIL']
                # chance: go to field, next railway/utility company or back
                if field_tag.startswith('CH'):
                    d16 = roll(16)
                    if d16 == 1:
                        current_field_nr = field_ids['GO']
                    if d16 == 2:
                        current_field_nr = field_ids['JAIL']
                    if d16 == 3:
                        current_field_nr = field_ids['C1']
                    if d16 == 4:
                        current_field_nr = field_ids['E3']
                    if d16 == 5:
                        current_field_nr = field_ids['H2']
                    if d16 == 6:
                        current_field_nr = field_ids['R1']
                    if d16 == 7 or d16 == 8: # to next railway
                        while not field_tag.startswith('R'):
                            current_field_nr = (current_field_nr + 1) % board_size
                            field_tag = field_tags[current_field_nr]
                    if d16 == 9: # to next utility
                        while not field_tag.startswith('U'):
                            current_field_nr = (current_field_nr + 1) % board_size
                            field_tag = field_tags[current_field_nr]
                    if d16 == 10:
                        current_field_nr = (current_field_nr - 3 + board_size) % board_size
            # update heuristic
            field_frquencies[current_field_nr] += 1
        # convert heuritstic
        heuristic_field_props = props(field_frquencies, iterations)
        field_ids = ['%02d' % id for id in range(board_size)]
        ranking = sorted(list(zip(heuristic_field_props,
                                  field_tags,
                                  field_ids
                                  )
                             )
                        )
        ranking.reverse()
        res = ''.join([str(e[2]) for e in ranking[0:3]])

        self.last_result = res
        self.last_result_details = [ranking, iterations, epsilon, dice_size]

    def details(self):
        ranking = self.last_result_details[0]
        iterations = self.last_result_details[1]
        epsilon = self.last_result_details[2]
        dice_size = self.last_result_details[3]
        ranking = [str(e[1]) + ' (' + str(e[2]) + ('-%.2f' % (e[0]*100)) + '%)' for e in ranking]
        ret = 'dice_size: ' + str(dice_size) + '\n'
        ret += 'epsilon: ' + str(epsilon) + '\n'
        ret += 'iterations: ' + str(iterations) + '\n'
        ret += 'ranking:\n'
        ret += list_to_fancy_str(ranking, separator = '  ')
        return ret

register_problem(Problem_084())
