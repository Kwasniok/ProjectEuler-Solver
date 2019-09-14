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

        if len(self.elements) == 0:
            return None

        # binary search

        l = 0
        r = len(self.elements) - 1
        m = None

        while True:
            # check if search was unsuccessful
            if l > r:
                return False
            # set middle index
            m = int((l + r) / 2)
            # compare value with middle element (and move bounderies if necessary)
            if self.elements[m] < element:
                l = m + 1
            elif self.elements[m] > element:
                r = m - 1
            else: # found element in sorted set
                return True

    def __getitem__(self, index):
        return self.elements[index]

    def __iter__(self):
        return iter(self.elements)

    def __reversed__(self):
        return reversed(self.elements)

    ## value of maxium
    def min(self):
        if len(self.elements) == 0:
            return None
        else:
            return self.elements[0]

    ## value of minimum
    def max(self):
        if len(self.elements) == 0:
            return None
        else:
            return self.elements[len(self.elements)-1]

    ## returns the index of the given element or None if it's not in the set
    def index_of(self, element):
        i = 0
        while i < len(self.elements):
            if element == self.elements[i]:
                return i
            i += 1
        return None

    ## returns smallest elements in sorted set which is greater than value or None if there is none
    def next(self, value):

        if len(self.elements) == 0:
            return None

        # binary search

        l = 0
        r = len(self.elements) - 1
        m = None

        while True:
            # check if direct search was unsuccessful
            if l > r:
                break
            # set middle index
            m = int((l + r) / 2)
            # compare value with middle element (and move bounderies if necessary)
            if self.elements[m] < value:
                l = m + 1
            elif self.elements[m] > value:
                r = m - 1
            else: # found element in sorted set
                # if there is a next element in set return it or return None otherwise
                if m + 1 < len(self.elements):
                    return self.elements[m + 1]
                else:
                    return None

        # value not found in sorted set find next element based on last middle position
        # note: m stops close to where value would be in this sorted set
        #       hence the next value is either at m or m + 1 (or not in this set)
        if self.elements[m] > value:
            return self.elements[m]
        else:
            if m + 1 < len(self.elements):
                return self.elements[m + 1]
            else:
                return None

    ## returns largest elements in sorted set which is less than value or None if there is none
    def previous(self, value):

        if len(self.elements) == 0:
            return None

        # binary search

        l = 0
        r = len(self.elements) - 1
        m = None

        while True:
            # check if direct search was unsuccessful
            if l > r:
                break
            # set middle index
            m = int((l + r) / 2)
            # compare value with middle element (and move bounderies if necessary)
            if self.elements[m] < value:
                l = m + 1
            elif self.elements[m] > value:
                r = m - 1
            else: # found element in sorted set
                # if there is a previous element in set return it or return None otherwise
                if m > 0:
                    return self.elements[m - 1]
                else:
                    return None

        # value not found in sorted set find next element based on last middle position
        # note: m stops close to where value would be in this sorted set
        #       hence the next value is either at m or m - 1 (or not in this set)
        if self.elements[m] < value:
            return self.elements[m]
        else:
            if m > 0:
                return self.elements[m - 1]
            else:
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
        return str(self.elements)
