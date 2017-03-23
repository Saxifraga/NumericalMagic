import numpy as np

# Note that this is not complete. You need to include pivoting to make it work
# correctly.
######################################################################
# Perform forward elimination step of Gaussian elimination
'''
The purpose of reorder_mat is to swap the rows of matrix mat such that the diagonals
are not zero. Vector b must undergo the same transformation in order to get the
correct x
'''
def reorder_mat(mat, b):
    #print mat
    m,n = mat.shape
    for i in range(n):

        k = i
        kmax = mat.shape[0]  #j cannot exceed number of rows in matrix
        while mat[i,i] == 0 and k < kmax:
            row1 = mat[i,:].copy()
            brow1 = b[i,:].copy()
            swap_row = mat[k,:].copy()
            bswap = b[k,:].copy()
            mat[i,:] = swap_row
            b[i,:] = bswap
            mat[k,:] = row1
            b[k,:] = brow1
            k +=1
    # print 'final of A', mat
    # print 'final of b', b
    #print mat
    return mat, b

def forward_elimination(A,b):

    m,n = A.shape
    assert(m == n)

    # For each diagonal element i
    for i in range(n):

        # A[i,i] is our "pivot" element, which will appear in a quotient below.
        # it had better not be zero.
        if A[i,i] == 0:
            [A, b] = reorder_mat(A,b)

        # Make leading element a 1 and reduce row
        fact = 1.0/float(A[i,i])
        A[i,:] = A[i,:]*fact
        b[i] = float(b[i])*fact


        # For each subsequent row j
        for j in range(i+1, n):
            # Perform the operation row_j = row_j - A[j,i] / A[i,i] * row_i
            factor = float(A[j,i]) / float(A[i,i])
            # For each column k
            for k in range(n):
                # Note the range above could be range(i,n) but we want
                # to force getting zeros in A for clarity.

                A[j,k] -= factor * float(A[i,k])
            # Perform the operation b_j = b_j - A[j,i] / A[i,i] * b_i
            b[j,0] -= factor * b[i,0]
    # print 'final A \n', A
    # print 'final B \n', b


######################################################################
# Perform back substitution step of Gaussian elimination

def back_substitution(A,b):

    m,n = A.shape
    assert(m == n)

    x = np.empty_like(b)

    # For each row i from n-1 to 0
    for i in reversed(range(n)):

        total = b[i,0]

        # For each column greater than i
        for j in range(i+1,n):
            total -= A[i,j]*x[j,0]

        assert(A[i,i] != 0)


        x[i,0] = total / A[i,i]

    return x

######################################################################

def gaussian_elimination(A, b):

    AA = A.copy()
    bb = b.copy()

    forward_elimination(AA, bb)
    #print 'AA', AA
    #print 'bb', bb
    return back_substitution(AA, bb)


######################################################################



A = np.matrix('2.0 1.0 0.0 0.0; 1.0 4.0 1.0 0.0; 0.0 1.0 4.0 1.0; 0.0 0.0 1.0 2.0')
b = np.matrix('3.0; 12.0; 24.0; 15.0')
d = gaussian_elimination(A, b)
print d
print 'residual:', np.linalg.norm(A*d - b)**2
