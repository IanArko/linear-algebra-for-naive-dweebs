#  FILE: svd.py
#  -----------------------------------------------------------------------------
#  About Sigular Value Decomposition:
#
#       For Any Matrix A, there exists a U, S, and V such that
#          A= U@S@V
#       where U.T@U = I, V.T@V = I, with S being diagonal with singular
#       values equal to the sqrt(sigma) for all sigma where sigma an
#       eigenvalue of A.
#
#       NOTE: What is written below is not the most computationally efficient
#             means of finding the SVD, but is meant to demonstrates the concept.
#
#  Now let's calculate the SVD for an arbitrary matrix A.

import numpy as np

ROW_SIZE = 5
COL_SIZE = 5

A = np.random.rand(ROW_SIZE,COL_SIZE)

#  We can think of S as the major axis of our matrix.
eigenvalue_array = np.vectorize(np.linalg.eig(A@A.T))

#  The diagonal eigenvalues go in decending order down the diagonal,
#  so we should sort our eigenvalues.


eigenvalue_array.sort(reverse=True, key=float)

print(eigenvalue_array)




U_test, S_test, V_test = np.linalg.svd(A)
