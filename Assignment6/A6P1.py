from cpt import *
from math import *
import numpy as np


def V (r) :
    x = r[0]
    y = r[1]
    return -x*x/2 - y*y/2 + (x*x + y*y)*(x*x + y*y)/4

def nV (r) :
    x = r[0]
    y = r[1]
    return x*x/2 + y*y/2 - (x*x + y*y)*(x*x + y*y)/4

def dV(r) :
    x = r[0]
    y = r[1]
    x = -x + x*x*x + x*y*y
    y = -y + y*y*y + y*x*x
    return np.array( [x,y] )

def ndV(r) :
    x = r[0]
    y = r[1]
    x = x - x*x*x - x*y*y
    y = y - y*y*y - y*x*x
    return np.array( [x,y] )


print " Minimization using Broyden-Fletcher-Goldfarb-Shanno Algorithm"
print " Find minimum of f(x,y) given an initial guess for x, y"
r = input(" Enter starting point coordinates x y: ")
gtol = input( " Enter desired accuracy: ")
V_min = 0.0
iterations = 0
res = scipy.optimize.fmin_bfgs(f=V, fprime=dV,x0=r, gtol=gtol)
ma = scipy.optimize.fmin_bfgs(f=nV, fprime=ndV,x0=r, gtol=gtol)
print res
print ma
