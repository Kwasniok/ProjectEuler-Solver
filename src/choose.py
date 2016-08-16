#   coding=UTF_8
#
#   choose.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#


from ppe_math import binomial_coefficient as nCr

# M := number of choose elements
# E := list
def num_of_choose_variations(M, E):
    
    if type(M) != int or type(E) != list:
        return None
    
    N = len(E)
    
    if M > N:
        return None
    
    return nCr(N, M)

# choose ith variation of M elements out of list E
def choose(i, M, E):
    
    # assertions #1
    if type(i) != int or type(M) != int or (type(E) != list and type(E) != str):
        return None
    
    N = len(E)
    
    # assertions #2
    if i < 1 or M < 1 or M > N:
        return None
    
    i -= 1
    i = i % nCr(N, M)
    i += 1
    
    # list of chosen elements
    e = []
    
    # internal version for recursion
    def _choose(i, M, E, N, e):
        
        if M == 0:
            return
        
        # find index for first element to choose
        k = N
        for n in range(N, M - 1, -1):
            
            l = nCr(n, M)
            if i <= l:
                k = n
            else:
                break
        
        # append new chosen element as head
        e[0:0] = [E[k - 1]]
        
        # recalculate values for remaining elements to choose
        if k > M:
            i -= nCr(k - 1, M)
        M -= 1
        N = k - 1
        
        # recursive recall for remaining elements to be chosen
        _choose(i, M, E, N, e)
        return
            
    _choose(i, M, E, N, e)
    
    return e

# choose ith variation of M elements out of list of length N
def choose_indexes_only(i, M, N):
    
    # assertions #1
    if type(i) != int or type(M) != int or type(N) != int:
        return None
    
    # assertions #2
    if i < 1 or M < 1 or M > N:
        return None
    
    i -= 1
    i = i % nCr(N, M)
    i += 1
    
    # list of chosen indexes
    e = []
    
    # internal version for recursion
    def _choose_indexes_only(i, M, N, e):
        
        if M == 0:
            return
        
        # find index for first element to choose
        k = N
        for n in range(N, M - 1, -1):
            
            l = nCr(n, M)
            if i <= l:
                k = n
            else:
                break
        
        # append new chosen element as head
        e[0:0] = [k - 1]
        
        # recalculate values for remaining elements to choose
        if k > M:
            i -= nCr(k - 1, M)
        M -= 1
        N = k - 1
        
        # recursive recall for remaining elements to be chosen
        _choose_indexes_only(i, M, N, e)
        return
            
    _choose_indexes_only(i, M, N, e)
    
    return e

# choose ith variation of M elements out of list of length N in reversed order
def choose_reverse_indexes_only(i, M, N):
    
    # assertions #1
    if type(i) != int or type(M) != int or type(N) != int:
        return None
    
    # assertions #2
    if i < 1 or M < 1 or M > N:
        return None
    
    i -= 1
    i = i % nCr(N, M)
    i += 1
    
    # list of chosen indexes
    e = []
    
    # internal version for recursion
    def _choose_reverse_indexes_only(i, m, n, N, e):
        
        if m == 0:
            return
        
        # find index for first element to choose
        k = n
        for n in range(n, m - 1, -1):
            
            l = nCr(n, m)
            if i <= l:
                k = n
            else:
                break
        
        # append new chosen element as head
        e.append(N - k)
        
        # recalculate values for remaining elements to choose
        if k > m:
            i -= nCr(k - 1, m)
        m -= 1
        n = k - 1
        
        # recursive recall for remaining elements to be chosen
        _choose_reverse_indexes_only(i, m, n, N, e)
        return
            
    _choose_reverse_indexes_only(i, M, N, N, e)
    
    return e

'''
E = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for l in range(1, len(E) + 1):
    for i in range(1, num_of_choose_variations(l, E) + 1):
        #print("%d : %d" % (l, i))
        print(choose(i, l, E))
'''

'''
N = 3
M = 2
for i in range (0, nCr(N, M)):
    print (choose_reverse_indexes_only(i + 1, M, N))
'''
