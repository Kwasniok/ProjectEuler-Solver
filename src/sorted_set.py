#   coding=UTF_8
#
#   sorted_set.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

## set which is in sorted order
# use &, |, /, ^ as set operators
class Sorted_Set():

    elements = []

    def __init__(self, elements):
        self.elements = sorted(set(elements))

    # list related methods

    def __len__(self):
        return len(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def __getitem__(self, index):
        return self.elements[index]

    def __iter__(self):
        return iter(self.elements)

    def __reversed__(self):
        return reversed(self.elements)

    ## value of maxium
    def min(self):
        return self.elements[0]

    ## value of minimum
    def max(self):
        return self.elements[len(self.elements)-1]

    ## returns the index of the given element or None if it's not in the set
    def index_of(self, element):
        i = 0
        while i < len(self.elements):
            if element == self.elements[i]:
                return i
            i += 1
        return None

    # set related methods

    ## returns the overlap of two sets
    def __and__(self, other):
        elements = sorted([element for element in self.elements if element in other.elements])
        return self.__class__(elements)

    ## return the union of two sets
    def __or__(self, other):
        elements = sorted(set(self.elements + other.elements))
        return self.__class__(elements)

    ## returns all elements which are in only one of the two sets
    def __xor__(self, other):
        return (self | other) / (self & other)

    ## returns all elements in the left set except those in the right set
    def __div__(self, other):
        elements = sorted([element for element in self.elements if element not in other.elements])
        return self.__class__(elements)

    # string related methods

    def __repr__(self):
        return str(self.elements)

    def __str__(self):
        return repr(self)

    def __unicode__(self):
        return unicode(self.elements)
