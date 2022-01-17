# Uses python3
import numpy as np



# Naive Divide and Conquer Solution:
# *********************************
# The dividing approach takes place by dividing each nxn matrices into 4 sub-matrices of size n/2 recursively, until nxn = 1x1, 
# The conquering approach is then satisfied by obtaining eight sub-problems of size n/2 (4 belonging to A_, and 4 belonging to B_, recursively)
# So A_ = [ [A, B],   and   B_ = [ [E, F],    So A_B_ = [ [AE + BG, AF + BH],  
#           [C, D] ]               [G, H] ]               [CE + DG, CF + DH] ]

# in which AE, BG, AF, BH, CE, DG, CF & DH are the 8 sub-problems/8 sub-matrices whose multiplication have to be computed
# Each sub-problem, when reaching base case size of 1x1, is computed by multiplying A_[ai, aj] x B_[bi, bj],
# where ai --> A's row pointer, aj --> A's column pointer, bi --> B's row pointer, bj --> B's column pointer,
# according to these pointers' values in the reached recursive step, 
# then each is summed and placed in its right place in the product matrix

# RECURRANCE EQUATION: 8xT(n/2) + Kxn^2
# TIME COMPLEXITY: Θ(n^3)

def wrapped_matrix_mult(A, B, n, ai, aj, bi, bj):

    # Initializing product array to be filled with zeros
    product = np.zeros((n,n))

    # Base case of recursion: returning 1x1 matrix according to pointer values at this recursion step
    if n == 1:
        product[0,0] = A[ai, aj] * B[bi, bj]
        return product

    # Division into 8 sub-problems/sub-matrices recursively
    # Each is computed according to A pointers and B pointers, indicating the sub-matrices to be multiplied in both A and B

    AE = wrapped_matrix_mult(A, B, n//2, ai, aj, bi, bj)
    BG = wrapped_matrix_mult(A, B, n//2, ai, aj + n//2, bi + n//2, bj)

    AF = wrapped_matrix_mult(A, B, n//2, ai, aj, bi, bj + n//2)
    BH = wrapped_matrix_mult(A, B, n//2, ai, aj + n//2, bi + n//2, bj + n//2)

    CE = wrapped_matrix_mult(A, B, n//2, ai + n//2, aj, bi, bj)
    DG = wrapped_matrix_mult(A, B, n//2, ai + n//2, aj + n//2, bi + n//2, bj)

    CF = wrapped_matrix_mult(A, B, n//2, ai + n//2, aj, bi, bj + n//2)
    DH = wrapped_matrix_mult(A, B, n//2, ai + n//2, aj + n//2, bi + n//2, bj + n//2)

    # Placement of all 8 sub-matrices in their right places in the product matrix,
    # with the guide of pi --> product's row pointer, pj --> product's column pointer
    # by addition of the right 2 sub-matrices in their right places

    # Upper left sub-matrix placement: AE + BG
    pi = 0
    for i in range(n//2):
        pj = 0
        for j in range(n//2):
            product[pi, pj] += AE[i, j] + BG[i, j]
            pj += 1
        pi += 1

    # Upper right sub-matrix placement: AF + BH
    pi = 0
    for i in range(n//2):
        pj = n//2
        for j in range(n//2):
            product[pi, pj] += AF[i, j] + BH[i, j]
            pj += 1
        pi += 1

    # Lower left sub-matrix placement: CE + DG
    pi = n//2
    for i in range(n//2):
        pj = 0
        for j in range(n//2):
            product[pi, pj] += CE[i, j] + DG[i, j]
            pj += 1
        pi += 1

    # Lower right sub-matrix placement: CF + DH
    pi = n//2
    for i in range(n//2):
        pj = n//2
        for j in range(n//2):
            product[pi, pj] += CF[i, j] + DH[i, j]
            pj += 1
        pi += 1

    return product

# The previous algorithm only works if n is of power of 2 (to be able to divide each n x n matrix into 4 n/2 x n/2 sub-matrices)
# but n cannot be limited to these values.
# Another issue is that the original matrix mult function does not have ai, aj, bi, bj among its parameters.
# So, this is handled by placing the core algorithm in a wrapped matrix_mult function while the original call of matrix_mult handles these issues

# In matrix_mult, n is checked if it is a power of 2: if log2(n) is a whole number in range 0-6,
# since the largest input n = 100, so the last n as power of 2 in range 0-100 is 64 = n^6)
# If condition is true call the wrapped matrix_mult function with initial values of all pointers as zeros (begining of both matrices)
# If it is false, then the nearest power of 2 larger than n is found, and both A and B matrices are padded with zero columns and rows,
# equal to the value of difference between this nearest power of 2 and original n
# and the wrapped matrix_mult function is called with new zero padded A and B, and nearest power of 2 as new size
# Then the result is sliced, to take only the original non-zero columns and rows of indices 0:n-1

def matrix_mult(A, B, n):

    # n is checked if it is a power of 2, with the methodolgy explained above
    if np.log2(n) not in range(0,7):

        # If n is not a power of 2, find nearest power of 2 larger than n
        new_n = int(2 ** (np.ceil(np.log2(n))))
        # Difference between nearest power of 2 and original n, so as to be added as number of
        # zero columns and rows in A and B
        extra = new_n - n
        # Initializing 2D new_A of size nearest power of 2 value
        new_A = np.zeros((new_n, new_n))
        # Placing values of A in upper left part new_A, so extra rows are right, and extra columns are down
        new_A[:-extra, :-extra] = A
        # Same done with B as A, acquiring zero-padded new B
        new_B = np.zeros((new_n, new_n))
        new_B[:-extra, :-extra] = B
        # Call wrapped matrix_mult with new zero-padded A and B, and nearest power of 2 larger than n as new_n
        result = wrapped_matrix_mult(new_A, new_B, new_n, 0, 0, 0, 0)
        # Slicing result to obtain only original non-zero (non-padded) columns and rows of indices 0:n-1
        product = result[0:n, 0:n]

    # If n is originally a power of 2, call wrapped matrix_mult with all initial pointer values as zeros
    else:
        product = wrapped_matrix_mult(A, B, n, 0, 0, 0, 0)

    return product



# Optimized Divide and Conquer Solution:
# *************************************
# Here, optimization is represented in dividing the problem into 7 sub-problems/sub-matrices of size n/2 x n/2 instead of 8,
# whose multiplication have to be computed
# where A_ and B_ are sliced/partitioned into size n/2 as follows:  A_ = [ [A, B],   and   B_ = [ [E, F],
#                                                                           [C, D] ]               [G, H] ]
# and the matrix mutliplication of an algebraic expression of these partitions make up the 7 sub-problems: P1, P2, P3, P4, P5, P6, P7
# P1 = Ax(F-H), P2 = (A+B)xH, P3 = (C+D)xE, P4 = Dx(G-E), P5 = (A+D)x(E+H), P6 = (B-D)x(G+H), P7 = (A-C)x(E+F) --> Strassen
# where each of P1-P7 is computed when the base case of both matrices to be multiplied (to be of size 1x1) is recursively reached.
# Then, each sub-matrix is placed in its right place in the product matrix as follows A_B_ = [ [P5+P4-P2+P6, P1+P2],
#                                                                                              [P3+P4, P1+P5-P3-P7 ] ]
# Note: pointers are not used here, beacuse in each recursive call, as each sub-problem is furtherly reduced to size n/2,
#       both input matrices are sliced before the recursive function call, and are sent sliced in the function,
#       until their size reaches 1x1, in which step, their multiplication is calculated.
#       WHEREAS, in the naive divide and conquer, the sub-problems are also recursively reduced to size n/2, 
#       but the whole matrices are sent in the function call without slicing, and the pointers indicate which element
#       in both matrices (case of reaching size of 1x1) should be multiplied.

# RECURRANCE EQUATION: 7xT(n/2) + Kxn^2
# TIME COMPLEXITY: Θ(n^(log2(7))) ≈ Θ(n^2.81)

def wrapped_matrix_mult_fast(A, B, n):

    # Base case of recursion: returning 1x1 matrix of multiplication of first (and only) elements left in A and B,
    #                         as in each recursive step, each input matrix is sliced into 4 sub-matrices of size n//2
    if n == 1:
        return np.array([[A[0,0] * B[0,0]]])

    # Slicing A into A_, B_, C and D, each of size n//2
    A_ = A[0:n//2, 0:n//2]
    B_ = A[0:n//2, n//2:n]
    C = A[n//2:n, 0:n//2]
    D = A[n//2:n, n//2:n]
    # Slicing B into E, F, G and H, each of size n//2
    E = B[0:n//2, 0:n//2]
    F = B[0:n//2, n//2:n]
    G = B[n//2:n, 0:n//2]
    H = B[n//2:n, n//2:n]

    # Division into 7 sub-problems/sub-matrices to be computed after slicing of A and B into 8 partitions of size n//2
    # Each is computed according to the algebraic expression stated by Strassen
    P1 = wrapped_matrix_mult_fast(A_, F - H, n//2)
    P2 = wrapped_matrix_mult_fast(A_ + B_, H, n//2)
    P3 = wrapped_matrix_mult_fast(C + D, E, n//2)
    P4 = wrapped_matrix_mult_fast(D, G - E, n//2)
    P5 = wrapped_matrix_mult_fast(A_ + D, E + H, n//2)
    P6 = wrapped_matrix_mult_fast(B_ - D, G + H, n//2)
    P7 = wrapped_matrix_mult_fast(A_ - C, E + F, n//2)

    # Initializing product array to be filled with zeros
    product = np.zeros((n, n))

    # Placement of all 7 sub-matrices/sub-problems in the right places in the product matrix,
    # with the guide of pi --> product's row pointer, pj --> product's column pointer
    # using the correct algebraic operations of the correct sub-matrices in their right places

    # Upper left sub-matrix placement: P5 + P4 - P2 + P6
    pi = 0
    for i in range(n//2):
        pj = 0
        for j in range(n//2):
            product[pi, pj] += ( P5[i, j] + P4[i, j] - P2[i, j] + P6[i, j] )
            pj += 1
        pi += 1

    # Upper right sub-matrix placement: P1 + P2
    pi = 0
    for i in range(n//2):
        pj = n//2
        for j in range(n//2):
            product[pi, pj] += ( P1[i, j] + P2[i, j] )
            pj += 1
        pi += 1

    # Lower left sub-matrix placement: P3 + P4
    pi = n//2
    for i in range(n//2):
        pj = 0
        for j in range(n//2):
            product[pi, pj] += ( P3[i, j] + P4[i, j] )
            pj += 1
        pi += 1

    # Lower right sub-matrix placement: P1 + P5 -P3 - P7
    pi = n//2
    for i in range(n//2):
        pj = n//2
        for j in range(n//2):
            product[pi, pj] += ( P1[i, j] + P5[i, j] - P3[i, j] - P7[i, j] )
            pj += 1
        pi += 1

    return product

# Like the naive divide and conquer approach, the previous algorithm only works if n is of power of 2, (to be able to divide
# each n x n matrix into 4 n/2 x n/2 sub-matrices) but n cannot be limited to these values. However, there are no pointers to worry about here.

# Again, this is handled by placing the core algorithm in a wrapped matrix_mult_fast function while the original call of matrix_mult_fast handles this issue,
# by checking if n is a power of 2, and case it is not, nearest power of 2 larger than n is found, and a number of extra zero columns and rows, 
# are added equal to the value of difference between it and original n --> zero padding until closest power of n is reached
# The zero-padded sub-matrices and new_n is sent to the function, and the result is sliced to take the original non-padded columns and rows only

def matrix_mult_fast(A, B, n):

    if np.log2(n) not in range(0,7):

        new_n = int(2 ** (np.ceil(np.log2(n))))
        extra = new_n - n
        new_A = np.zeros((new_n, new_n))
        new_A[:-extra, :-extra] = A
        new_B = np.zeros((new_n, new_n))
        new_B[:-extra, :-extra] = B
        result = wrapped_matrix_mult_fast(new_A, new_B, new_n)
        product = result[0:n, 0:n]

    else:
        product = wrapped_matrix_mult_fast(A, B, n)

    return product



if __name__ == '__main__':
    n = int(input())
    A = []
    B = []
    # Enter matrix 1 values, press enter after each row
    # Matrix 1 filling
    for i in range(n):
        A.append([int(j) for j in input().split()]) 

    # Enter matrix 2 values, press enter after each row
    # Matrix 2 filling
    for i in range(n):
        B.append([int(j) for j in input().split()]) 

    A = np.array(A)
    B = np.array(B)

    print(matrix_mult(A, B, n))

    ''' UNCOMMENT this line if you will submit BONUS'''
    print(matrix_mult_fast(A, B, n))