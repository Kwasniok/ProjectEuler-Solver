
#-- my_permutation.py --#

from ppe_math import faculty
from number import get_digit_list
import copy

'''
def nextDigit(i,E):
    print(i / faculty(len(E) - i))
    return int((i / faculty(len(E) - i))) % faculty(len(E)-1)
'''


def num_of_permutations(E):
    return faculty(len(E))

# returns the ith permutation of the list E
'''
def get_permutation(i, E):

    DigitNumber = int((i % faculty(len(E)))/faculty(len(E)-1))

    D = [E[DigitNumber]]

    if len(E) > 1:
        E2 = copy.copy(E)
        del(E2[DigitNumber])
        D += get_permutation(i, E2)

    return D
'''
def get_permutation(i, E):

    l = int((i % faculty(len(E))) / faculty(len(E)-1))

    # leading element
    if type(E) == list:
        Eout = [E[l]]
    elif type(E) == str:
        Eout = E[l]

    # next elements
    if len(E) > 1:

        if type(E) == list:
            E2 = []
        elif type(E) == str:
            E2 = ""

        # copy all elements without the leading element
        k = 0
        while k < len(E):
            if k != l:

                if type(E) == list:
                    E2 += [E[k]]
                elif type(E) == str:
                    E2 += E[k]

            k += 1

        # append next elements
        Eout += get_permutation(i, E2)

    return Eout

# returns a list of all permutations for a list E
def all_permutations(E):
    ps = []
    i = 0
    nops = num_of_permutations(E)
    while i < nops:
        ps.append(get_permutation(i, E))
        i += 1
    return ps

def all_rotations(E):
    rs = []
    cur = copy.copy(E)
    for i in range(0, len(E)):
        rs.append(copy.copy(cur))
        tmp = cur.pop()
        cur[0:0] = [tmp]
    return rs

''' VERY SLOW METHOD
def is_permutation_of(p, E):
    i = 0
    ps = num_of_permutations(E)
    while i < ps:
        if p == get_permutation(i, E):
            return True
        i += 1
    return False
'''

def list_from_number(N):
    if N == 0:
        return [0]

    l = []
    if N < 0:
        N = -N
        l[0:0] = ['-']

    while N != 0:
        l[0:0] = [N % 10]
        N /= 10

    return l

# p and E must be integers
def is_permutation_of_number(p, N):
    return is_permutation_of(get_digit_list(p), get_digit_list(N))


# p and E must be lists
def is_permutation_of(p, E):
    if len(p) != len(E):
        return False
    if p == E:
        return True
    if p[0] in E:
        pi = list(p)
        Ei = list(E)
        pi.remove(p[0])
        Ei.remove(p[0])
        return is_permutation_of(pi, Ei)
    else:
        return False
