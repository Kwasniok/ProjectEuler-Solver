
## INFO: THIS CODE MIGHT CONTAIN SOME BUGGS!

## important functions: poker_card_hand_stack_from_string, comparePokerCardHands

class Poker_Card:

    LOWER_THAN_ALL = -1

    ACE_BOTTOM = 1
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9
    TEN   = 10
    JACK  = 11
    QUEEN = 12
    KING  = 13
    ACE   = 14

    HEARTS   = 1
    DIAMONDS = 2 # or TAILS
    CLOVERS  = 3 # or CLUBS
    SPADES   = 4 # or PIKES

    def __init__(self, s, n = None):

        if n != None:
            self.number = n
            self.suit = s
            return

        self.number = None
        self.suit = None

        if not len(s) == 2:
            return

        if s[0] == '2':
            self.number = Poker_Card.TWO
        elif s[0] == '3':
            self.number = Poker_Card.THREE
        elif s[0] == '4':
            self.number = Poker_Card.FOUR
        elif s[0] == '5':
            self.number = Poker_Card.FIVE
        elif s[0] == '6':
            self.number = Poker_Card.SIX
        elif s[0] == '7':
            self.number = Poker_Card.SEVEN
        elif s[0] == '8':
            self.number = Poker_Card.EIGHT
        elif s[0] == '9':
            self.number = Poker_Card.NINE
        elif s[0] == 'T' or s[0] == 'X':
            self.number = Poker_Card.TEN
        elif s[0] == 'J':
            self.number = Poker_Card.JACK
        elif s[0] == 'Q':
            self.number = Poker_Card.QUEEN
        elif s[0] == 'K':
            self.number = Poker_Card.KING
        elif s[0] == 'A' or s[0] == '1':
            self.number = Poker_Card.ACE

        if s[1] == 'H':
            self.suit = Poker_Card.HEARTS
        elif s[1] == 'D' or s[1] == 'T':
            self.suit = Poker_Card.DIAMONDS
        elif s[1] == 'C':
            self.suit = Poker_Card.CLOVERS
        elif s[1] == 'S' or s[1] == 'P':
            self.suit = Poker_Card.SPADES

    def __str__(self):
        s = ""

        if self.number == Poker_Card.TWO:
            s += '2'
        elif self.number == Poker_Card.THREE:
            s += '3'
        elif self.number == Poker_Card.FOUR:
            s += '4'
        elif self.number == Poker_Card.FIVE:
            s += '5'
        elif self.number == Poker_Card.SIX:
            s += '6'
        elif self.number == Poker_Card.SEVEN:
            s += '7'
        elif self.number == Poker_Card.EIGHT:
            s += '8'
        elif self.number == Poker_Card.NINE:
            s += '9'
        elif self.number == Poker_Card.TEN:
            s += 'T'
        elif self.number == Poker_Card.JACK:
            s += 'J'
        elif self.number == Poker_Card.QUEEN:
            s += 'Q'
        elif self.number == Poker_Card.KING:
            s += 'K'
        elif self.number == Poker_Card.ACE or self.number == Poker_Card.ACE_BOTTOM:
            s += 'A'
        else:
            s += "."

        if self.suit == Poker_Card.HEARTS:
            s += 'H'
        elif self.suit == Poker_Card.DIAMONDS:
            s += 'D'
        elif self.suit == Poker_Card.CLOVERS:
            s += 'C'
        elif self.suit == Poker_Card.SPADES:
            s += 'S'
        else:
            s += '.'

        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.number, self.suit) == (other.number, other.suit)

    def __ne__(self, other):
        return (self.number, self.suit) != (other.number, other.suit)

    # for sort orders
    def __lt__(self, other):
        return (self.number, self.suit) < (other.number, other.suit)

    def __gt__(self, other):
        return (self.number, self.suit) > (other.number, other.suit)

    def __le__(self, other):
        return (self.number, self.suit) <= (other.number, other.suit)

    def __ge__(self, other):
        return (self.number, self.suit) >= (other.number, other.suit)


def all_poker_card_numbers():
    return range(Poker_Card.TWO, Poker_Card.ACE + 1)

def all_poker_card_suits():
    return range(Poker_Card.HEARTS, Poker_Card.SPADES + 1)

def all_poker_cards():
    cards = []
    for s in all_poker_card_suits():
        for n in all_poker_card_numbers():
           cards.append(Poker_Card(s, n))
    return cards

class Poker_Card_Analysed_Hand():

    def __init__(self, hand):
        self.hand = hand

        self.hand.sort()

        self.supplement = list(self.hand)

        # pair & triple
        self.pair_numbers = []
        self.triple_number = None
        self.four_number = None

        for n in all_poker_card_numbers():
            count = 0
            for c in self.hand:
                if c.number == n:
                    count += 1
            if count == 2:
                self.pair_numbers.append(n)
            elif count == 3:
                self.triple_number = n
            elif count == 4:
                self.four_number = n

            if count > 1:
                i = 0
                while i < len(self.supplement):
                    if self.supplement[i].number == n:
                        self.supplement.remove(self.supplement[i])
                    else:
                        i += 1

        # straight
        self.is_straight = False


        if self.hand[4].number == Poker_Card.ACE and self.hand[3].number == Poker_Card.FIVE:
            # ace is used at bottom
            self.hand[4].number = Poker_Card.ACE_BOTTOM
            self.hand.sort()

        number = self.hand[4].number - 1

        i = 3
        while i > -1:
            n = self.hand[i].number
            if  self.hand[3].number == Poker_Card.FIVE and n == Poker_Card.ACE: # if ace can be used at bottom
                n = Poker_Card.ACE_BOTTOM
            if n != number:
                break
            number -= 1
            i -= 1

        if i == -1:
            self.is_straight = True
        elif self.hand[0].number == Poker_Card.ACE_BOTTOM:
            # ace is not used at bottom
            self.hand[0].number == Poker_Card.ACE
            self.hand.sort()

        # flush
        self.is_flush = False

        number = self.hand[4].number
        suit = self.hand[4].suit

        i = 3
        while i > -1:
            if self.hand[i].suit != suit:
                break
            i -= 1

        if i == -1:
            self.is_flush = True
            if not is_full_house(self) and not is_four_of_a_kind(self): # reset supplement if flush tops
                self.supplement = self.hand

    def __str__(self):
        return str(self.hand) + " --> {pairs<" + str(self.pair_numbers) + ">, triple<" + str(self.triple_number) + ">, four<" + str(self.four_number) + ">, is_straight<" + str(self.is_straight) + ">, is_flush<" + str(self.is_flush) + ">}"

    def __repr__(self):
        return str(self)


# all ranks
def is_royal_flush(ah):
    return is_straight_flush(ah) and ah.hand[4].number == Poker_Card.ACE

def is_straight_flush(ah):
    return is_flush(ah) and is_straight(ah)

def is_four_of_a_kind(ah):
    return ah.four_number != None

def is_full_house(ah):
    return len(ah.pair_numbers) == 1 and ah.triple_number != None

def is_flush(ah):
    return ah.is_flush

def is_straight(ah):
    return ah.is_straight

def is_three_of_a_kind(ah):
    return ah.triple_number != None and len(ah.pair_numbers) != 1

def is_two_pairs(ah):
    return len(ah.pair_numbers) == 2

def is_one_pair(ah):
    return len(ah.pair_numbers) == 1 and ah.triple_number == None


#### winning functions ####
# takes a list with at least one analysed hand of required type
# returns (all) winning hand(s)

# auxiliary
def wins_tie(ahs): # analysed hands

    i = 1
    while i < 6 and len(ahs) > 1:

        max = Poker_Card.LOWER_THAN_ALL
        ties = None

        for ah in ahs:

            if len(ah.supplement) < i: # supplement is not long enough
                continue

            ir = len(ah.supplement) - i
            if ah.supplement[ir].number > max:
                max = ah.hand[ir].number
                ties = []
                ties.append(ah)
            elif ah.supplement[ir].number == max:
                ties.append(ah)

        if len(ties) == 1:
            return ties

        ahs = ties

        i += 1

    return ahs

def wins_triple(aths):

    max = Poker_Card.LOWER_THAN_ALL
    ties = None

    for ah in aths:

        if ah.triple_number > max:
            max = ah.triple_number
            ties = []
            ties.append(ah)
        elif ah.triple_number == max:
            ties.append(ah)

    return ties


def wins_pair_at_index(aphs, pair_index):

    max = Poker_Card.LOWER_THAN_ALL
    ties = None

    for ah in aphs:

        if ah.pair_numbers[pair_index] > max:
            max = ah.pair_numbers[pair_index]
            ties = []
            ties.append(ah)
        elif ah.pair_numbers[pair_index] == max:
            ties.append(ah)

    return ties


# winning functions
def wins_royal_flush(arfhs): # analysed royal flush hands
    return arfhs

def wins_straight_flush(asfhs):
    return wins_tie(asfhs)

def wins_four_of_a_kind(afhs):

    max = Poker_Card.LOWER_THAN_ALL
    ties = None

    for ah in afhs:

        if ah.four_number > max:
            max = ah.four_number
            ties = []
            ties.append(ah)
        elif ah.four_number == max:
            ties.append(ah)

    if len(ties) == 1:
        return ties

    return wins_tie(ties)

def wins_full_house(afhhs):

    ties = wins_triple(afhhs)

    if len(ties) == 1:
        return ties

    return wins_pair_at_index(ties, 0)

def wins_flush(afhs):
    return wins_tie(afhs)

def wins_straight(ashs):
    return wins_tie(ashs)

def wins_three_of_a_kind(aths):

    ties = wins_triple(aths)

    if len(ties) == 1:
        return ties

    return wins_tie(ties)


def wins_two_pairs(atphs):
    ties = wins_pair_at_index(atphs, 1)

    if len(ties) == 1:
        return ties

    ties = wins_pair_at_index(ties, 0)

    if len(ties) == 1:
        return ties

    return wins_tie(ties)

def wins_one_pair(aphs):
    ties = wins_pair_at_index(aphs, 0)

    if len(ties) == 1:
        return ties

    return wins_tie(ties)

def wins_high_card(ahchs):
    return wins_tie(ahchs)

def filter_for_prop(ahs, is_func):
    _ahs = list(ahs)
    for ah in ahs:
        if not is_func(ah):
            _ahs.remove(ah)
    return _ahs

# takes a list of poker card hands (a list of five cards each)
# returns the the winning hand(s) as list
# Every card must occur at most one time per comparison.
# Otherwise the result might be unsuitable.
def comparePokerCardHands(hands):

    ahs = []
    for hand in hands:
        ahs.append(Poker_Card_Analysed_Hand(hand))

    rfahs = filter_for_prop(ahs, is_royal_flush)
    if len(rfahs) > 0:
        return wins_royal_flush(rfahs)

    sfahs = filter_for_prop(ahs, is_straight_flush)
    if len(sfahs) > 0:
        return wins_straight_flush(sfahs)

    fahs = filter_for_prop(ahs, is_four_of_a_kind)
    if len(fahs) > 0:
        return wins_four_of_a_kind(fahs)

    fhahs = filter_for_prop(ahs, is_full_house)
    if len(fhahs) > 0:
        return wins_full_house(fhahs)

    fahs = filter_for_prop(ahs, is_flush)
    if len(fahs) > 0:
        return wins_flush(fahs)

    sahs = filter_for_prop(ahs, is_straight)
    if len(sahs) > 0:
        return wins_straight(sahs)

    tahs = filter_for_prop(ahs, is_three_of_a_kind)
    if len(tahs) > 0:
        return wins_three_of_a_kind(tahs)

    tpahs = filter_for_prop(ahs, is_two_pairs)
    if len(tpahs) > 0:
        return wins_two_pairs(tpahs)

    opahs = filter_for_prop(ahs, is_one_pair)
    if len(opahs) > 0:
        return wins_one_pair(opahs)

    return wins_high_card(ahs)


def poker_card_stacks_from_string(s, card_seperator = ' ', stack_seperator = '\n'):
    sstacks = s.split(stack_seperator)

    stacks = []
    for sstack in sstacks:
        if sstack == '':
            continue
        stack = []
        scards = sstack.split(card_seperator)
        for scard in scards:
            card = Poker_Card(scard)
            stack.append(card)
        stacks.append(stack)

    return stacks


# creates a stack of poker games from a string
# After every fifth card a new hand is interpreted.
# The number of cards per game thus must be a multiple of five.
# Otherwise the code will willfully crash (by a division by zero).
def poker_card_hand_stack_from_string(s, card_seperator = ' ', stack_seperator = '\n'):
    sstacks = s.split(stack_seperator)

    handsStack = []
    for sstack in sstacks:

        if sstack == '':
            continue

        scards = sstack.split(card_seperator)
        hands = []
        hand = []
        for scard in scards:

            card = Poker_Card(scard)
            hand.append(card)

            if len(hand) == 5:
                hands.append(hand)
                hand = []

        if len(hand) != 0:
             1 / 0
        handsStack.append(hands)

    return handsStack
