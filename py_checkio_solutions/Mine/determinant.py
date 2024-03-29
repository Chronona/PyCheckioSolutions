#!/home/user/.local/bin/checkio --domain=py run determinant

# In linear algebra, thedeterminantis a value associated with a square    matrix. It can be computed from the entries of the matrix by a specific    arithmetic expression (There are other ways to determine its value as    well.)
# 
# The determinant of a matrixAis denoteddet(A),det A, or|A|.    In the case where the matrix entries are written out in full, the determinant is    denoted by surrounding the matrix entries by vertical bars instead of the    brackets or parentheses of the matrix.
# 
# There are various ways to define the determinant of a square matrixA, i.e.    one with the same number of rows and columns. Perhaps the most natural way    is expressed in terms of the columns of the matrix. If we write anN×Nmatrix in terms of its column vectors:
# 
# A = [a1, a2, ..., an]
# 
# Where there are vectors of size n, then the determinant of A is defined so    that:
# 
# det[a1, ..., b*aj+c*v, ..., an] = b*det(A)+c*det[a1, ..., v, ..., an]
# det[a1, ..., aj, aj+1, ..., an] = -det[a1, ..., aj+1, aj, ..., an]
# det(I) = 1
# 
# Wherebandcare scalars,vis any vector of sizeNandIis the identity    matrix of sizeN. These properties state that the determinant is an    alternating multilinear function of the columns, and they suffice to    uniquely calculate the determinant of any square matrix. Provided the    underlying scalars form a field (more generally, a commutative ring with    unity).    Equivalently, the determinant can be expressed as a sum of products of    entries of the matrix where each product hasNterms and the coefficient of    each product is −1 or 1 or 0 according to a given rule: it is a polynomial    expression of the matrix entries. This expression grows rapidly with the    size of the matrix (anNxNmatrix contributesN!terms), so it will first    be given explicitly for the case of 2×2 matrices and 3×3 matrices,    followed by the rule for arbitrary size matrices, which subsumes these two    cases.
# 
# For more information about the determinant visitWikipedia
# 
# Input:A square matrix as a list of lists with integers.
# 
# Output:The determinant of the matrix as an integer.
# 
# Precondition:
# 0 < len(matrix) ≤ 5
# all(len(row) == len(matrix) for row in matrix)
# all(all(0 ≤ x < 10 for x in row) for row in matrix)
# 
# 
# END_DESC

#%%
def main(data, m):
    d = [i[::m] * 2 for i in data]
    tmp2 = []
    for i in range(len(data)):
        tmp = 1
        for j in range(len(data)):
            tmp *= d[j][j+i]
        tmp2.append(tmp)
    if len(tmp2) > 2:
        print(tmp2)
        return sum(tmp2)
    else:
        return tmp2[0]

def checkio(data):
    if len(data) < 2:
        return data[0][0]
    a = main(data, 1)
    b = main(data, -1)
    print(a,b)
    return a - b

# checkio([[2, 7, 6, 4, 2, 0], [3, 0, 8, 2, 5, 6], [3, 8, 9, 1, 0, 3], [9, 4, 5, 0, 8, 6], [8, 9, 0, 6, 4, 6], [1, 6, 3, 0, 7, 1]])

#%%
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([[4, 3], [6, 3]]) == -6, "First example"

    assert checkio([[1, 3, 2], [1, 1, 4], [2, 2, 1]]) == 14, "Second example"

#%%

# %%