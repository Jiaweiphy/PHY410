from cpt import *

print " Unbalanced Wheatstone bridge equations"
print " --------------------------------------"

v0 = 1.5
r = 1.

rv = 10.

v = Matrix(6, 1)       # column vector with 3 rows
v[0][0] = v0
print 'v = '
print v 

R = Matrix(6, 6)       # 3x3 resistance matrix
R[0][0] = r + rv      # set components using slicing notation
R[0][1] = rv
R[0][2] = rv
R[0][3] = 1.0+1.0
R[0][4] = 1.0
R[0][5] = 0.0

R[1][0] = r+1.0
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

R[3][0] = r
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

print 'R = '
print R

# the solve_Gauss_Jordan replaces R by R^-1 and v by i
# so save the original R and copy v into a vector i
R_save = Matrix_copy(R)
i = Matrix_copy(v)

solve_Gauss_Jordan(R, i)
print " Solution using Gauss-Jordan elimination"
print " i = "
print i


# total current
print " i_v = i_1 + i_2 + i_3 = " + str(i[0][0] + i[1][0] + i[2][0])

# effective resistance
print " R_eff = V0/i_v-R_v =" +str(v0/(i[0][0] + i[1][0] + i[2][0])-rv)



