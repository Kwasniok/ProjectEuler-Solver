#   coding=UTF_8
#
#   ppe_permutation.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 18.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from ppe_math import faculty
from number import get_digit_list

## abstract class for permutation types
# note: see static method get for the i-th permutation of a seqence (list or string)
# note: apply permutations to a seqence via function call (e.g. permutated_seq = perm(seq))
class Abstract_Permutation():

    ## @param n must be a natural number where n ≥ 1
    def __init__(self, n, i=0):
        self.indices = range(1, n + 1)
        self.nr = 0
        if i != 0:
            self.set_nr(i)

    # list related methods

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, index):
        return self.indices[index]

    ## returns the sequence (list or string) with permutation applied
    # note: 1 in permutation correspnds to first element in seq
    # @param: perm a permutation of same size like seq, perm must start with 0
    # @param: seq a sequence (list or string) of same size like perm
    def __call__(self, seq):
        assert len(self) == len(seq), "missmatch in length when applying permutation to sequence"
        # note: decrease index by to to get index for lists
        # 1 corresponds to first element in list
        if type(seq) == list:
            return map(lambda i : seq[i-1], self.indices)
        if type(seq) == str:
            s = ""
            for i in self.indices:
                s += seq[i-1]
            return s
        assert False, "unsupported type when applying permutation to sequence"

    # string related methods

    def __str__(self):
        return str(self.get())

    def __unicode__(self):
        return str(self)

    def __repr__(self):
        return "nr=" + str(self.get_nr()) + ",sgn=" + str(self.signum()) + ":" + str(self.get())

    ## returns the i-th permutation of the sequence (list or string)
    # note: depends on permutation type and must be overwritten
    @staticmethod
    def get(i, seq):
        raise NotImplementedError

    ## returns the nr of the current permutation
    # 0 means initial permutation is in initial state
    def get_nr(self):
        return self.nr

    ## sets permutation to the i-th permutation in order of permutation type (must be overwriten)
    # @param nr must be an integer in range 0 ≤ nr < possiblilites()
    def set_nr(self, i=0):
        self.indices = self.__class__.get(i, range(1, len(self.indices) + 1))
        self.nr = i

    ## returns True if permutation is in initial state
    def is_initial(self):
        return self.get_nr() == 0

    ## returns True if permutation is in last possible state (according to this order)
    def is_last(self):
        return self.get_nr() == self.possibilities() - 1

    ## returns the amount of different possibilities of this permutation
    def possibilities(self):
        raise NotImplementedError

    ## returns True if permutation is not last possible state (according to this order)
    def has_next(self):
        return self.get_nr() < self.possibilities() - 1

    ## returns next abstract permutation
    # note: this method depends on the permutation type and must be overwritten
    def next(self):
        raise NotImplementedError

    ## returns signum of this abstract permutation
    # note: this method depends on the permutation type and must be overwritten
    def signum(self):
        raise NotImplementedError

## returns the sequence (list or string) with permutation applied
# @param: perm a permutation of same size like list, perm must start with 0
# @param: seq a sequence of same size like perm
def apply_permutation_to_list(perm, seq):
    return perm(seq)

# abstract class representing a permutation group of magnitude n
class Abstract_Permutation_Group():

    ## reference to class of permutation type which must inherit from Abstract_Permutation
    # must be overwritten
    attached_permutation_class = None

    ## @param n must be a natural number where n ≥ 1
    def __init__(self, n):
        self.n = n

    # string related methods

    ## returns the basic information about this permutation group
    # must be overwritten
    # format: L(n) where L ist the abbr. of the permutation group and n the magnitude
    def __str__(self):
        raise NotImplementedError

    ## returns the basic information about this permutation group
    # (allows unicode characters like mathematical symbols)
    # must be overwritten
    # format: L(n) where L ist the abbr. of the permutation group and n the magnitude
    def __unicode__(self):
        raise NotImplementedError

    # list related methods

    ## retuns magnitude
    def __len__(self, i):
        return self.n

    ## (efficient) implementation of iteration through complete permutation group
    # note: esp. usefull when calculating a permutation is cheaper when knowing the previous one
    # in permutation order (compared to calculating the permutation from scratch)
    # can be overwritten (if calculating costs are the opposite)
    def __iter__(self):

        ## handles the iteration through this symmetrical group
        class Abstract_Permutation_Group_Iter():

            def __init__(self, n, attached_permutation_class):
                self.n = n
                self.last = None
                self.attached_permutation_class = attached_permutation_class

            def next(self):
                # return Permutaion for n in initial state as first element
                if self.last == None:
                    # prevent from iterating over empty sets
                    if self.n == 0:
                        raise StopIteration
                    if self.attached_permutation_class == None:
                        raise NotImplementedError
                    self.last = self.attached_permutation_class(self.n)
                    return self.last
                # if there is a next permutation return it
                if self.last.has_next():
                    self.last.next()
                    return self.last
                # there is no ermutation left -> stop iteration
                raise StopIteration

        return Abstract_Permutation_Group_Iter(self.n, self.__class__.attached_permutation_class)

    def __getitem__(self, i):
        return self.attached_permutation_class(self.n, i)

    ## returns the amount of different possibilities of this permutation type
    def possibilities(self):
        raise NotImplementedError

    ## returns all permutations in this permutation group
    # note: if n is large this might take too much rescources (ckeck possiblilites first!)
    # prefer iteration through permutations over listing all permutations!
    def get_all(self):
        ret = []
        for p in self:
            ret.append(p)
        return ret

    ## returns all permutations of permutation group of sequence (list or string)
    # must be overwritten
    # note: Copy code in comment and replace CLASS_NAME with class name.
    #       Since this method is static there is no way to automise this.
    #       (Static methods have no refernce to invoking class.)
    # note: if n is large this might take too much rescources (ckeck possiblilites first!)
    # prefer iteration through permutations over listing all permutations!
    @staticmethod
    def get_all_of_seq(seq):
        raise NotImplementedError
        '''
        ret = []
        for p in CLASS_NAME(len(seq)):
            ret.append(p(seq))
        return ret
        '''

## returns weather the integer i is a permutation of the integer j
def is_permutation_of_number(i, j):
    return is_permutation_of(get_digit_list(i), get_digit_list(j))

## returns True if list seq1 is permutation of list seq2 (both lists or strings)
def is_permutation_of(seq1, seq2):
    # compare length first
    if len(seq1) != len(seq2):
        return False
    # check equality
    if seq1 == seq2:
        return True
    # check if first element in seq1 is in seq2
    if seq1[0] in seq2:
        # remove first element of seq1 from both sequences and continue recursively
        if type(seq1) == list:
            seq1_remaining = list(seq1)
            seq2_remaining = list(seq2)
            seq1_remaining.remove(seq1[0])
            seq2_remaining.remove(seq1[0])
        elif type(seq1) == str:
            i = 0
            while True:
                if seq2[i] == seq1[0]:
                    break
                i += 1
            seq1_remaining = seq1[1:len(seq1)]
            seq2_remaining = seq2[0:i]
            seq2_remaining += seq2[i+1:len(seq2)]
        return is_permutation_of(seq1_remaining, seq2_remaining)
    else:
        # seq1 has an element which is not in seq2
        return False

## class representing permutations in lexicografical order
class Permutation(Abstract_Permutation):

    ## returns the i-th lexicografical permutation of the list
    @staticmethod
    def get(i, list):
        # current leading elements index in ns
        l = int((i % faculty(len(list))) / faculty(len(list)-1))
        # store it as list
        ret = [list[l]]
        # next elements
        if len(list) > 1:
            list_remaining = []
            # copy all elements without the current leading element
            k = 0
            while k < len(list):
                if k != l:
                    list_remaining.append(list[k])
                k += 1
            # append next elements
            ret += Permutation.get(i, list_remaining)
        return ret

    ## returns the amount of different lexicografical permutation for magnitude n
    def possibilities(self):
        return faculty(len(self.indices))

    ## returns next lexicografical permutation
    def next(self):
        # taken from https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
        # Find the largest x such that P[x]<P[x+1].
        # (If there is no such x, P is the last permutation.)
        # Find the largest y such that P[x]<P[y].
        # Swap P[x] and P[y].
        # Reverse P[x+1 .. n].

        # for n ≤ 1 there are no differing permutations
        if len(self.indices) < 2:
            return

        # find lagest x where indices[x] < indices[x+1]
        x = len(self.indices) - 2
        while self.indices[x] > self.indices[x+1]:
            x -= 1
            if x == -1:
                # was last permutation
                return
        # find largest y where indices[x] < indices[y]
        y = len(self.indices) - 1
        while self.indices[x] > self.indices[y]:
            y -= 1
        # swap indices[x] and indices[y]
        tmp = self.indices[x]
        self.indices[x] = self.indices[y]
        self.indices[y] = tmp
        # revert inidces[x+1] to indices[last_index]
        x += 1
        y = len(self.indices) - 1
        while x < y:
            tmp = self.indices[x]
            self.indices[x] = self.indices[y]
            self.indices[y] = tmp
            x += 1
            y -= 1
        # update permutation nr.
        self.nr += 1

    ## returns signum of this permutation
    def signum(self):
        if self.nr % 2 == 0:
            return +1
        else:
            return -1

## class representing a symmetrical group of magnitude n
class Symmetric_Group(Abstract_Permutation_Group):

    ## reference to class of permutation type
    attached_permutation_class = Permutation

    # string related methods

    ## returns the basic information about this permutation group
    # format: L(n) where L ist the abbr. of the permutation group and n the magnitude
    def __str__(self):
        return "S(" + str(self.n) + ")"

    ## returns the basic information about this permutation group
    # (allows unicode characters like mathematical symbols)
    # format: L(n) where L ist the abbr. of the permutation group and n the magnitude
    def __unicode__(self):
        return u"𝔖(" + str(self.n) + ")"

    ## returns the amount of different possibilities of this permutation
    def possibilities(self):
        return len(self)

    ## returns all (lecicographic) permutations of list
    # note: if n is large this might take too much rescources (ckeck possiblilites first!)
    # prefer iteration through permutations over listing all permutations!
    @staticmethod
    def get_all_of_list(list):
        ret = []
        for p in Symmetric_Group(len(list)):
            ret.append(p(list))
        return ret

## class representing permutations in rotational order
class Cyclic_Rotation(Abstract_Permutation):

    ## returns the i-th permutation of the list
    # @param i (default rotation direction is to the left,
    #           negative values result in rotaion to the right)
    @staticmethod
    def get(i, list):
        ret = []
        j = 0
        while j < len(list):
            ret.append(list[(j + i) % len(list)])
            j += 1
        return ret

    ## returns the amount of different possibilities of rotations of magnitude n
    def possibilities(self):
        return len(self.indices)

    ## rotates the set one step to the left
    def next(self):
        # for n < 2 there are no differing permutations
        if len(self.indices) < 2:
            return
        next_indices = []
        i = 0
        while i < len(self.indices):
            next_indices.append(self.indices[(i + 1) % len(self.indices)])
            i += 1
        self.indices = next_indices
        self.nr += 1

    ## returns signum of this permutation
    def signum(self):
        if self.n % 2 == 0:
            # n is even and signum is alternating
            if self.nr % 2 == 0:
                return +1
            else:
                return -1
        else:
            # n is odd and signum is allways +1
            return +1

## class representing a cyclic rotation group of magnitude n
class Cyclic_Rotation_Group(Abstract_Permutation_Group):

    ## reference to class of permutation type
    attached_permutation_class = Cyclic_Rotation

    # string related methods

    ## returns the basic information about this permutation group
    # format: L(n) where L ist the abbr. of the permutation group and n the magnitude
    def __str__(self):
        return "R(" + str(self.n) + ")"

    ## returns the basic information about this permutation group
    # (allows unicode characters like mathematical symbols)
    # format: L(n) where L ist the abbr. of the permutation group and n the magnitude
    def __unicode__(self):
        return u"ℜ(" + str(self.n) + ")"

    ## returns the amount of different possibilities of rotations of magnitude n
    def possibilities(self):
        return len(self)

    ## returns all (lecicographic) permutations of list
    # note: if n is large this might take too much rescources (ckeck possiblilites first!)
    # prefer iteration through permutations over listing all permutations!
    @staticmethod
    def get_all_of_list(list):
        ret = []
        for p in Symmetric_Group(len(list)):
            ret.append(p(list))
        return ret
