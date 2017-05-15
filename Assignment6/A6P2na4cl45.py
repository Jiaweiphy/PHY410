from nacl import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

name="Na4Cl45"       # for output files
nNa = 4
nCl = 4
n = nNa + nCl
a = 0.2
d=0.02
sqrt2 = pow(2, 0.5)
sqrt3 = pow(3, 0.5)
r_Na = [  [ 0, 0, 0 ], [ 0, a, a], [0, 0, 2*a-d], [a, a/2+a/(2*sqrt2), -a/(2*sqrt2)] ]
r_Cl = [  [ a*sqrt3/2, a/2, 0 ], [ -a*sqrt3/2, a/2, 0 ], [0, a, 2*a], [0, -d, a-d/2] ]

# Initialize the cluster, add guesses at the
# minimum arrangement. 
cluster = Cluster()

for i in xrange(nNa) :
    r = Vector(r_Na[i])
    cluster.add(Na(r))

for i in xrange(nCl) :
    r = Vector(r_Cl[i])
    cluster.add(Cl(r))

print " " + name + " cluster"
print " Initial potential energy = " + str( cluster.potential_energy() )

# Minimize the function
accuracy = 1e-6

res = cluster.minimize( accuracy )

pe = res[1]
iterations = res[4]

# Print out resulting files, and also
# plot the values in matplotlib
print " Minimized potential energy = " + str(pe) + " eV"
print " Binding energy of cluster  = " + str( pe / 2.0 ) + " eV"
print " Number of function calls = " + str( iterations )

file_name = name + ".data"
outfile = open( file_name, 'w' )
for i in xrange( nNa + nCl - 1) :
    for j in range(i+1,nNa+nCl) :
        rij = cluster.ion(i).r - cluster.ion(j).r
        dr = sqrt( np.dot(rij,rij) )
        s =  "(" + cluster.ion(i).name + ")-(" + cluster.ion(j).name + ")"
        print " " + s + " r_" + str(i) + str(j) + " = " + str( dr ) + " nm"

outfile.write( str(cluster) )
outfile.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

[x,y,z] = cluster.convert()
ax.scatter( x,y,z )
plt.show()
