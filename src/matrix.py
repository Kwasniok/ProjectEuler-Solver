#   coding=UTF_8
#
#   matrix.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 22.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from type_number import is_number

## @brief A class representing a Vector of dimension $n$.
# `vec` $ \\equiv
# \\begin{bmatrix}
# a_{1} \\\\
# a_{2} \\\\
#   ⋮   \\\\
# a_{n}
# \\end{bmatrix}
# $
# where $a_{i}$ can be accessed by `vec[i]` $(i = 1, 2, …, n)$.
class Vector():

    ## @brief initializes a Vector of dimension $n$
    # @code
    # >>> #initialze a 1-vector equivalent to 0
    # >>> vec = Vector()
    # >>> print vec
    # [0]
    # >>> #initialze a 2-vector equivalent to 0
    # >>> vec = Vector(2)
    # >>> print vec
    # [0, 0]
    # >>> #initialze a 2-vector with values
    # >>> vec = Vector([1, 2])
    # >>> print vec
    # [1, 2]
    # @endcode
    # @param first when integer n is set to first otherwise first is interpreted as list of elements.
    def __init__(self, first=1):
        if type(first) == int:
            ## stores the values of the Vector
            self.vs = []
            for i in range(first):
                self.vs.append(0)
        elif type(first) == list:
            # set elements
            self.vs = first
        else:
            assert False, "Vector needs either integer or list to be initialized"

    ## @brief returns the dimension of the Vector
    # @code
    # >>> vec = Vector([1, 2, 3])
    # >>> print vec.dim()
    # 3
    # @endcode
    def dim(self):
        return len(self.vs)

    # string related methods

    ## @brief returns values of Vector as string similar to list of elements
    # @code
    # >>> vec = Vector([1, 2, 3])
    # >>> print str(vec)
    # [1, 2, 3]
    # @endcode
    def __str__(self):
        return str(self.vs)

    ## @brief returns values of Vector as string similar of list of elements with extra hint for dimension
    # @code
    # >>> vec = Vector([1, 2, 3])
    # >>> print repr(vec)
    # Vec(3):[1, 2, 3]
    # @endcode
    def __repr__(self):
        return "Vec(" + str(self.dim()) + "):" + str(self.vs)

    ## @brief returns Vector as aligned grid surrounded by brackets using unicode characters and multiple lines (via vertical tabs)
    # @code
    # >>> vec = Vector([123, 12, 1]])
    # >>> print "-some space-" + unicode(vec)
    # -some space-⎡123⎤
    #             ⎢ 12⎥
    #             ⎣  1⎦
    # @endcode
    # @note Prefer this method over str() when printing to console since the output is much more readable.
    def fancy_ustr(self):
        ret = ""
        # convert all elements to unicode strings
        vs_ustr = map(lambda elem: unicode(elem), self.vs)
        # calculate indentation
        elem_space = 0
        for i in range(self.dim()):
            if len(vs_ustr[i]) > elem_space:
                elem_space = len(vs_ustr[i])
        # store numbers of characters used in row (brackets, elements, padding & seperating spaces)
        b = 2 + elem_space
        # addpend matrix as string
        for i in range(self.dim()):
            # append leftpart of left square bracket
            if i == 0:
                if self.dim() == 1:
                    ret += u"["
                else:
                    ret += u"⎡"
            elif i == self.dim() - 1:
                if self.dim() != 1:
                    ret += u"⎣"
            else:
                ret += u"⎢"
            # append (row) element
            # calculate padding
            padding = (elem_space - len(vs_ustr[i]))
            ret += u" " * padding + vs_ustr[i]
            # append leftpart of right square bracket
            if i == 0:
                if self.dim() == 1:
                    ret += u"]"
                else:
                    ret += u"⎤"
            elif i == self.dim() - 1:
                if self.dim() != 1:
                    ret += u"⎦"
            else:
                ret += u"⎥"
            # go back to one character before first character in line and append vertical tab
            if i < self.dim() - 1:
                ret += u"\b" * b + u"\v"
        # move cursor back up
        ret += "\033[" + str(self.dim() - 1) + "A"
        return ret

    # list related methods

    ## returns the i-th element of the vector
    def __getitem__(self, i):
        return self.vs[i]

    ## sets the i-th element of the vector to val
    def __setitem__(self, i, val):
        self.vs[i] = val

    # operators

    ## returns the sum of this an another Vector
    def __add__(self, other):
        assert self.dim() == other.dim(), "missmatch in vector length when adding"
        return Vector(map(lambda i: self[i] + other[i], range(self.dim())))

    ## returns the difference of this an another Vector
    def __sub__(self, other):
        assert self.dim() == other.dim(), "missmatch in vector length when subtracting"
        return Vector(map(lambda i: self[i] - other[i], range(self.dim())))

    def __mul__(self, other):
        if is_number(other):
            return Vector(map(lambda x: x * other, self.vs))
        if other.__class__ == Matrix :
            assert self.dim() == other.n, "missmatch in Vector size when multiplicating with Matrix"
            prod = Vector(other.m)
            for j in range(other.m):
                for k in range(other.n):
                    prod[j] += self[k] * other[(k,j)]
            return prod
        if other.__class__ == Vector:
            assert self.dim() == other.dim(), "missmatch in Vector size when multiplicating with Vector"
            return Vector(sum(map(lambda i: self[i] * other[i], range(self.dim()))))
        assert False, "cannot multiplicate Vector with instance of type " + str(other.__class__.__name__)

    ## adds another Vector to this Vector
    def __iadd__(self, other):
        self = self + other

    ## subtracts another Vector from this Vector
    def __isub__(self, other):
        self = self - other

    def __imul__(self, other):
        self = self * other

## returns the dot product of two Vectors
# @note: Both vectors must have the same length.
def dot(self, other):
    assert self.dim() == other.dim(), "missmatch in vector length when scalar multiplicating"
    ret = 0
    for i in range(self.dim()):
        ret += self[i] * other[i]
    return ret

## returns the cross product of two Vectors
# @note: Both vectors must have length of 3.
def cross(self, other):
    assert self.dim() == 3, "missmatch in vector length when cross multiplicating"
    assert other.dim() == 3, "missmatch in vector length when cross multiplicating"
    return Vector([self[1]*other[2] - self[2]*other[1], self[2]*other[0] - self[0]*other[2], self[0]*other[1] - self[1]*other[0]])


## @brief A class representing a $m \\times n$ Matrix.
# `mat` $ \\equiv
# \\begin{bmatrix}
# a_{11} & a_{12} & ⋯ & a_{1m} \\\\
# a_{21} & a_{22} & ⋯ & a_{2m} \\\\
# ⋮    & ⋮    & ⋱ & ⋮ \\\\
# a_{n1} & a_{n2} & ⋯ & a_{nm}
# \\end{bmatrix}
# $
# where $a_{ij}$ can be accessed by `mat[i][j]` $(i = 1, 2, …, n; j = 1 ,2, …, m)$.
class Matrix():

    ## @brief initializes a $m \\times n$ Matrix
    # @code
    # >>> #initialze a 1x1-matrix equivalent to 0
    # >>> m = Matrix()
    # >>> print m
    # [[0]]]]
    # >>> #initialze a 2x2-matrix equivalent to 0
    # >>> m = Matrix(2)
    # >>> print m
    # [[0, 0], [0, 0]]
    # >>> #initialze a 2x3-matrix equivalent to 0
    # >>> m = Matrix(2, 3)
    # >>> print m
    # [[0, 0, 0], [0, 0, 0]]
    # >>> #initialze a 3x2-matrix with values
    # >>> m = Matrix([[1, 2], [3, 4], [5, 6]])
    # >>> print m
    # [[1, 2], [3, 4], [5, 6]]
    # @endcode
    # @param first when integer m is set to first otherwise first is interpreted as list of list of elements.
    # @param second used when first is an integer and interpreted as n.
    #               (When unset n is set to m and the Matrix becomes square.)
    def __init__(self, first=1, second=None):
        # shortcut for square matrices
        if type(first) == int and second == None:
            second = first
        if type(first) == int and type(second) == int:
            # create null matrix with m x n dimensions
            ## @brief number of columns
            self.m = first
            ## @brief number of rows
            self.n = second
            ## @brief values
            self.vs = []
            i = 0
            while i < self.m:
                self.vs.append([])
                j = 0
                while j < self.n:
                    self.vs[i].append(0)
                    j += 1
                i += 1
        elif type(first) == list:
            # create metrix from list
            assert type(first[0]) == list , "Matrix needs list of lists to be initialized"
            self.vs = first
            self.m = len(self.vs)
            self.n = len(self.vs[0])
            i = 1
            while i < len(self.vs):
                assert type(self.vs[i]) == list, "Matrix needs list of lists to be initialized"
                assert len(self.vs[i]) == self.n, "Matrix needs each row to have the same length"
                i += 1
        else:
            assert False, "atrix needs either two integers or a list to be initialized"

    def dim(self):
        return (self.m, self.n)

    # string related methods

    ## @brief returns values of Matrix as string similar to list of list of elements
    # @code
    # >>> m = Matrix([[123, 456, 789],[12, 34, 56],[1, 2, 3]])
    # >>> print str(m)
    # [[123, 456, 789], [12, 34, 56], [1, 2, 3]]
    # @endcode
    def __str__(self):
        return str(self.vs)

    ## @brief returns values of Matrix as string similar to list of list of elements with extra hint for dimensions
    # @code
    # >>> m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # >>> print repr(m)
    # Mat(3,3):[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # @endcode
    def __repr__(self):
        return "Mat(" + str(self.m) + "," + str(self.n) + "):" + str(self.vs)

    ## @brief returns Matrix as aligned grid surrounded by brackets using unicode characters and multiple lines (via vertical tabs)
    # @code
    # >>> m = Matrix([[123, 456, 789],[12, 34, 56],[1, 2, 3]])
    # >>> print "-some space_" + unicode(m)
    # -some space_⎡123 456 789⎤
    #             ⎢ 12  34  56⎥
    #             ⎣  1   2   3⎦
    # @endcode
    # @note Prefer this method over str() when printing to console since the output is much more readable.
    def fancy_ustr(self):
        ret = u""
        # convert all elements to unicode strings
        vs_ustr = []
        for row in self.vs:
            vs_ustr.append(map(lambda elem: unicode(elem), row))
        # calculate indentation
        elem_space_per_col = []
        b = 2 + self.n -1 # stores numbers of characters used in row (brackets, elements, padding & seperating spaces)
        for j in range(self.n):
            max_len = 0
            for i in range(self.m):
                if len(vs_ustr[i][j]) > max_len:
                    max_len = len(vs_ustr[i][j])
            elem_space_per_col.append(max_len)
            b += max_len
        # addpend matrix as string
        i = 0
        while i < self.m:
            # append leftpart of left square bracket
            if i == 0:
                if self.m == 1:
                    ret += u"["
                else:
                    ret += u"⎡"
            elif i == self.m - 1:
                if self.m != 1:
                    ret += u"⎣"
            else:
                ret += u"⎢"
            # append row
            j = 0
            while j < self.n:
                # calculate padding
                padding = (elem_space_per_col[j] - len(vs_ustr[i][j]))
                ret += u" " * padding + vs_ustr[i][j]
                if j < self.n - 1:
                    ret += u" "
                j += 1
            # append leftpart of right square bracket
            if i == 0:
                if len(self.vs) == 1:
                    ret += u"]"
                else:
                    ret += u"⎤"
            elif i == len(self.vs) - 1:
                if len(self.vs) != 1:
                    ret += u"⎦"
            else:
                ret += u"⎥"
            # go back to one character before first character in line and append vertical tab
            if i < self.m - 1:
                ret += u"\b" * b + u"\v"
            i += 1
        if self.m - 1 > 0:
            ret += "\033[" + str(self.m - 1) + "A"
        return ret

    ## list related methods

    def __getitem__(self, (i,j)):
        return self.vs[i][j]

    def __setitem__(self, (i,j), val):
        self.vs[i][j] = val

    # operators

    def __add__(self, other):
        assert self.dim() == other.dim(), "missmatch in Matrix size when adding"
        sum = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                sum[(i,j)] = self[(i,j)] + other[(i,j)]
        return sum

    def __sub__(self, other):
        assert self.dim() == other.dim(), "missmatch in Matrix size when adding"
        diff = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                diff[(i,j)] = self[(i,j)] - other[(i,j)]
        return diff

    ## @brief multiplies two matrices.
    # If `mat1` $ \\equiv
    # \\begin{bmatrix}
    # a_{11} & a_{12} & ⋯ & a_{1p} \\\\
    # a_{21} & a_{22} & ⋯ & a_{2p} \\\\
    # ⋮    & ⋮    & ⋱ & ⋮ \\\\
    # a_{n1} & a_{n2} & ⋯ & a_{np}
    # \\end{bmatrix}
    # $ and `mat2` $ \\equiv
    # \\begin{bmatrix}
    # b_{11} & b_{12} & ⋯ & b_{1m} \\\\
    # b_{21} & b_{22} & ⋯ & b_{2m} \\\\
    # ⋮    & ⋮    & ⋱ & ⋮ \\\\
    # b_{p1} & b_{p2} & ⋯ & b_{pm}
    # \\end{bmatrix}
    # $ then `prod = mat1 * mat2` $ \\equiv
    # \\begin{bmatrix}
    # c_{11} & c_{12} & ⋯ & c_{1m} \\\\
    # c_{21} & c_{22} & ⋯ & c_{2m} \\\\
    # ⋮    & ⋮    & ⋱ & ⋮ \\\\
    # c_{n1} & c_{n2} & ⋯ & c_{nm}
    # \\end{bmatrix}
    # $ such that $c_{ij} = \\sum_{k=1}^{k=p}a_{ik}b_{kj}$.
    # <p>
    # Where $a_{ij}$ can be accessed by `mat1[i][j]` $(i = 1, 2, …, n; j = 1 ,2, …, p)$,
    # $b_{ij}$ can be accessed by `mat2[i][j]` $(i = 1, 2, …, p; j = 1 ,2, …, m)$ and
    # $c_{ij}$ can be accessed by `prod[i][j]` $(i = 1, 2, …, n; j = 1 ,2, …, m)$.
    def __mul__(self, other):
        if is_number(other):
            prod = Matrix(self.m, self.n)
            for i in range(prod.m):
                for j in range(prod.n):
                    prod[(i,j)] = self[(i,j)] * other
            return prod
        if other.__class__ == Matrix :
            assert self.m == other.n, "missmatch in Matrix size when multiplicating with Matrix"
            prod = Matrix(self.n, other.m)
            for i in range(prod.m):
                for j in range(prod.n):
                    for k in range(self.m):
                        prod[(i,j)] += self[(i,k)] * other[(k,j)]
            return prod
        if other.__class__ == Vector:
            assert self.m == other.dim(), "missmatch in Matrix size when multiplicating with Vector"
            prod = Vector(self.n)
            for i in range(prod.dim()):
                for k in range(self.m):
                    prod[i] += self[(i,k)] * other[k]
            return prod
        assert False, "cannot multiplicate Matrix with instance of type " + str(other.__class__.__name__)

    def __iadd__(self, other):
        assert self.dim() == other.dim(), "missmatch in Matrix size when adding"
        for i in range(self.m):
            for j in range(self.n):
                self[(i,j)] += other[(i,j)]

    def __isub__(self, other):
        assert self.dim() == other.dim(), "missmatch in Matrix size when adding"
        for i in range(self.m):
            for j in range(self.n):
                self[(i,j)] -= other[(i,j)]

    def __imul__(self, other):
        self = self * other
