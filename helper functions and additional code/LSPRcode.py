from math import*
import numpy as np

#det3x3

def det3x3 (m):
    v1 = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
    v2 = m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])
    v3 = m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])

    return v1 - v2 + v3

def spliceColumn(coef, const, j):
    coefficient = np.copy(coef)
    coefficient[:,j] = const
    return coefficient

def cramer(coef, const):
    coefficient = np.copy(coef)
    x = det3x3(spliceColumn(coefficient, const, 0)) / det3x3(coef)
    y = det3x3(spliceColumn(coefficient, const, 1)) / det3x3(coef)
    z = det3x3(spliceColumn(coefficient, const, 2)) / det3x3(coef)

    return (x, y, z)

print(det3x3(np.array([[1,2,3],[3,-10,-16],[13,21,18]])))
print(det3x3(spliceColumn(np.array([[1,2,3],[3,-10,-16],[13,21,18]]), np.array([3,20,44]), 0)))
print(det3x3(spliceColumn(np.array([[1,2,3],[3,-10,-16],[13,21,18]]), np.array([3,20,44]), 1)))
print(det3x3(spliceColumn(np.array([[1,2,3],[3,-10,-16],[13,21,18]]), np.array([3,20,44]), 2)))
print (cramer(np.array([[1,2,3],[3,-10,-16],[13,21,18]]) , np.array([3,20,44])))
