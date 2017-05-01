from cpt import *
import numpy as np
import matplotlib.pyplot as plt

print " Unbalanced Wheatstone bridge equations"
print " --------------------------------------"

v0 = 1.5
r = np.arange(0.2, 5.2, 0.2)
R_eff = [0.0]*len(r)

print r

rv = 10.

v = Matrix(6, 1)       # column vector with 3 rows
v[0][0] = v0
print 'v = '
print v 

for j in range(25):
 #print r[j]
 R = Matrix(6, 6)       # 3x3 resistance matrix
 R[0][0] = r[j] + rv      # set components using slicing notation
 R[0][1] = rv
 R[0][2] = rv
 R[0][3] = 1.0+1.0
 R[0][4] = 1.0
 R[0][5] = 0.0
 
 R[1][0] = r[j]+1.0
 R[1][1] = 0.0
 R[1][2] = -1.0
 R[1][3] = -1.0
 R[1][4] = 0.0
 R[1][5] = -1.0
 
 R[2][0] = 0.0
 R[2][1] = -2.0
 R[2][2] = 2.0
 R[2][3] = 0.0
 R[2][4] = 1.0
 R[2][5] = -1.0
 
 R[3][0] = r[j]
 R[3][1] = -1.0
 R[3][2] = 0.0
 R[3][3] = 1.0
 R[3][4] = -1.0
 R[3][5] = 0.0
 
 R[4][0] = -2.0
 R[4][1] = 0.0
 R[4][2] = 0.0
 R[4][3] = 4.0
 R[4][4] = 1.0
 R[4][5] = -1.0
 
 R[5][0] = 0.0
 R[5][1] = -1.0
 R[5][2] = -2.0
 R[5][3] = 1.0
 R[5][4] = 3.0
 R[5][5] = 2.0
 
 #print R
 
 # the solve_Gauss_Jordan replaces R by R^-1 and v by i
 # so save the original R and copy v into a vector i
 R_save = Matrix_copy(R)
 i = Matrix_copy(v)
 
 solve_Gauss_Jordan(R, i)
 print " Solution using Gauss-Jordan elimination"
 print " i = "
 print i
 
 # effective resistance
 R_eff[j] = v0/(i[0][0] + i[1][0] + i[2][0])-rv
 #print R_eff

plt.plot(r, R_eff)
plt.show()







