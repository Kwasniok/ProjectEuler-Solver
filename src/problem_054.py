#   coding=UTF_8
#
#   problem_054.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_054_all_games import all_games
from cards import poker_card_hand_stack_from_string, comparePokerCardHands

class Problem_054(Problem):
    
    def __init__(self):
        self.problem_nr = 54
        self.description_str = '''In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand         Player 1         Player 2         Winner
1         5H 5C 6S 7S KD    2C 3S 8S 8D TD    Player 2
          Pair of Fives     Pair of Eights
     
2         5D 8C 9S JS AC    2C 5C 7D 8S QH    Player 1
        Highest card Ace  Highest card Queen
         
3         2D 9C AS AH AC    3D 6D 7D TD QD    Player 2
            Three Aces   Flush with Diamonds
     
4         4D 6S 9H QH QC    3D 6D 7H QD QS    Player 1
          Pair of Queens    Pair of Queens
        Highest card Nine Highest card Seven

5         2H 2D 4C 4D 4S    3C 3D 3S 9S 9D    Player 1
            Full House         Full House
        With Three Fours  With Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
    
    def calculate(self, X):
        
        sum = 0
        sum_Details = []
        
        games = poker_card_hand_stack_from_string(all_games)
        g = 1 # for break points only
        for game in games:
            winner = comparePokerCardHands(game)
            if len(winner) == 1 and winner[0].hand == game[0]:
                sum += 1
                sum_Details.append(0)
            if len(winner) == 1 and winner[0].hand == game[1]:
                sum_Details.append(1)
            g += 1
                
        
        self.last_result = sum
        self.last_result_details = sum_Details
        
    def details(self):
        desc_str = "game nr.   Player 1      vs.        Player 2\n"
        games = poker_card_hand_stack_from_string(all_games)
        winner_is = self.last_result_details
        g = 1
        for game in games:
            desc_str += str(g) + " : " + list_to_fancy_str(game, " vs. ", highlightColour = Colours.HIGHLIGHT, startHighlight = winner_is[g - 1], endHighlight = winner_is[g - 1]) + "\n"
            g += 1
        return desc_str
    
register_problem(Problem_054())
