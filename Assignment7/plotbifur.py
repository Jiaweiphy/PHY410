from read_plot import *
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
from matplotlib import legend

x,y = read_plot("bifur_plot.txt")

plt.scatter(x,y)
plt.ylim( [-3.1415926,3.1415926] )
plt.xlim( [1.0,1.5] )

plt.show()
