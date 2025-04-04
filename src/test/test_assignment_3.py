import numpy as np

from src.main.assignment_3 import (
    gaussian_jordan , lu_factor , is_diagonal_dominant, is_pos_definite

)

m_gj = np.array([
    [2, -1, 1, 6],
    [1, 3, 1, 0],
    [-1, 5, 4, -3]

], dtype =float)

m_lu = np.array([
    [1, 1, 0, 3],
    [2, 1, -1, 1],
    [3, -1, -1, 2],
    [-1, 2, 3, -1]
], dtype =float)

m_dd = np.array([

    [9,0, 5, 2, 1],
    [3, 9, 1, 2, 1],
    [0, 1, 7, 2, 3],
    [4, 2, 3, 12, 2],
    [3, 2,4, 0, 8]
], dtype =float)


m_pd = np.array([
    [2, 2, 1],
    [2, 3, 0],
    [1, 0, 2]
], dtype =float)


gauss_elim_sol = gaussian_jordan(m_gj)
print(f"{gauss_elim_sol}")


L, U, det= lu_factor(m_lu)

def printMe(A):
    for row in A:
        formatted_row = [f"{val}"for val in row] 
        print("[ " + "  ".join(formatted_row) + " ]")  
print(det)
print("\n")
printMe(L)
print("\n")
printMe(U)

print("\n")
dd_sol = is_diagonal_dominant(m_dd)
print(f"{dd_sol}")

pd_sol = is_pos_definite(m_pd)
print(f"{pd_sol}")
