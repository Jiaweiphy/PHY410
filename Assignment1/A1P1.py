import math
import numpy as np
import matplotlib.pyplot as plt

# individual distances in Mpc
r = [ 0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5,
     0.5,   0.63,  0.8,   0.9,   0.9,   0.9,   0.9,  1.0,
     1.1,   1.1,   1.4,   1.7,   2.0,   2.0,   2.0,  2.0 ]

# individual velocities in km/s
v = [ +170, +290, -130, -70,  -185, -220, +200, +290,
     +270, +200, +300, -30,  +650, +150, +500, +920,
     +450, +500, +500, +960, +500, +850, +800, +1090 ]

# group distances in Mpc
rg = [0.032, 0.034, 0.25675, 0.576, 0.9, 0.925, 1.2, 1.925, 2.0]

# group velocities in km/s
vg = [ +170, +290, +151.25, 252, -30, 555, 483.33, 925, 500]

n = len(r)   # number of points
ng = len(rg) #number of groups

#variables for points
s_x = 0
s_y = 0
s_xx = 0
s_xy = 0
sigma2 = 0

#variables for groups
s_xg = 0
s_yg = 0
s_xxg = 0
s_xyg = 0
sigma2g = 0

#Points computation
for i in range (0, n ):
    s_x += r[i]
    s_y += v[i]
    s_xx += r[i]**2
    s_xy += r[i]*v[i]
denom = n * s_xx - s_x**2
if abs( denom ) < 0.000001 :
    print 'Error! Denomominator is zero!'
    exit()

# Compute y-intercept and slope
a = (s_xx * s_y - s_x * s_xy) / denom
b = (n*s_xy - s_x * s_y) / denom

# Compute uncertainties
sigma = math.sqrt(sum((v[i] - (a+b*r[i]))**2 for i in range(n)) / (n-2))
sigma_a = math.sqrt(sigma**2 * s_xx / denom)
sigma_b = math.sqrt(sigma**2 * n / denom)


#Groups computations
for i in range (0, ng ):
    s_xg += rg[i]
    s_yg += vg[i]
    s_xxg += rg[i]**2
    s_xyg += rg[i]*vg[i]
denomg = ng * s_xxg - s_xg**2
if abs( denomg ) < 0.000001 :
    print 'Error! Denomominator is zero!'
    exit()

# Compute y-intercept and slope
ag = (s_xxg * s_yg - s_xg * s_xyg) / denomg
bg = (ng*s_xyg - s_xg * s_yg) / denomg

# Compute uncertainties
sigmag = math.sqrt(sum((vg[i] - (ag+bg*rg[i]))**2 for i in range(ng)) / (ng-2))
sigma_ag = math.sqrt(sigmag**2 * s_xxg / denomg)
sigma_bg = math.sqrt(sigmag**2 * ng / denomg)

#Get the line
x = np.arange(0,2.5,0.001)
y = b*x + a
xg = np.arange(0,2.5,0.001)
yg = bg*xg + ag

# Plot v-r
plt.scatter(r,v,marker='o')
plt.scatter(rg,vg,marker='o',facecolors='white')
plt.xlabel('r(Mpc)')
plt.ylabel('v(km/s)')
plt.title('Hubble\'s datas and 9 groups of nebulae')
# Plot fitting lines
plt.plot(x,y)
plt.plot(xg,xg,linestyle='--')

# Print out results
print ' Least squares fit of', n, 'data points'
print ' -----------------------------------'
print " Hubble's constant slope   b = {0:6.2f} +- {1:6.2f}  km/s/Mpc".format( b, sigma_b)
print " Intercept with r axis     a = {0:6.2f} +- {1:6.2f}  km/s".format( a, sigma_a)
print ' Estimated v error bar sigma =', round(sigma, 1), 'km/s'

plt.show()
