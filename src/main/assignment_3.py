import numpy as np

#Gaussian Elimination


def gaussian_jordan(A):
    n= len(A)

    #forward elimination - turning into a triangle
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] -= factor * A[i,i:]
   
    sol_vector = np.zeros(n)
    b = A[:, -1].copy()

    #backward elimination 
    for i in reversed(range(n)):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * sol_vector[j]
        sol_vector[i] = (b[i] - sum_ax) / A[i][i]
    
    return sol_vector

    
  

#LU Factorization
def lu_factor(A):
   n = A.shape[0]
   L = np.zeros_like(A, dtype=float)
   U = np.zeros_like(A, dtype=float)

   for i in range(n):
       L[i][i] = 1.0

       for j in range(i, n):
            U[i][j] = A[i][j] - np.dot(L[i, :i], U[:i, j])

       for j in range(i + 1, n):
            L[j][i] = (A[j][i] - np.dot(L[j, :i], U[:i, i])) / U[i][i]
        
   det = np.prod(np.diag(U))

   return L.tolist(), U.tolist(), det

       
#Diagonol Dominance

def is_diagonal_dominant(A):
    n = A.shape[0]
    for i in range(n):
        row_sum = 0
        for j in range(n):
            if i != j:
                row_sum += abs(A[i][j])
        if abs(A[i][i]) < row_sum:
            return False
    
    return True



#Positive defnite

def is_pos_definite(A):
    if np.array_equal(A, A.T):
        try:
            np.linalg.cholesky(A)
            return True
        except np.linalg.LinAlgError:
            return False

    else:
        return False


 
