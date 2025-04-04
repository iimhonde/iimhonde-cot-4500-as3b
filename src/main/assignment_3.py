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

    for i in reversed(range(n)):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * sol_vector[j]
        sol_vector[i] = (b[i] - sum_ax) / A[i][i]
    
    return sol_vector

    #backward elimination 
  

#LU Factorization
def lu_factor(A):
   n = A.shape[0]
   L = np.zeros_like(A, dtype=float)
   U = np.zeros_like(A, dtype=float)

   for i in range(n):
       L[i][i] = 1.0

       for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

       for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
        
       det = np.prod(np.diag(U))

   return L.tolist(), U.tolist(), det
       
#Diagonol Dominance

def is_diagonal_dominant(A):
    pass

#Positive defnite

def is_pos_definite(A):
    pass




 
