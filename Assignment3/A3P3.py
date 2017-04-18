import matplotlib.pyplot as plt

from fft import fft, fft_power, ifft
from numpy import array, real
import math
import time


# data downloaded from ftp://ftp.cmdl.noaa.gov/ccg/co2/trends/co2_mm_mlo.txt
print ' C02 Data from Mauna Loa'
data_file_name = 'co2_mm_mlo.txt'
file = open(data_file_name, 'r')
lines = file.readlines()
file.close()
print ' read', len(lines), 'lines from', data_file_name

window = True

yinput = []
xinput = []
ywin = []

for line in lines :
    if line[0] != '#' :
        try:
            words = line.split()
            xval = float(words[2])
            yval = float( words[4] )
            yinput.append( yval )
            xinput.append( xval )
        except ValueError :
            print 'bad data:',line

#Substract a linear fit from Assignment 2
for iy in xrange(len(yinput)) :
    yinput[iy]=yinput[iy]-315.472649452-0.0441692549556*iy-0.000155314201252*(iy**2)

N = len(yinput)
log2N = math.log(N, 2)
if log2N - int(log2N) > 0.0 :
    print 'Padding with Zeroes!'
    pads = [0.0] * (pow(2, int(log2N)+1) - N)
    yinput = yinput + pads
    N = len(yinput)
    print 'Padded : '
    print len(yinput)
    # Apply a window to reduce ringing from the 2^n cutoff
    if window :
        for iy in xrange(len(yinput)) :
            ywin.append(yinput[iy] * (0.5 - 0.5 * math.cos(2*math.pi*iy/float(N-1))))

y = array( yinput )
yw = array (ywin)
x = array([ float(i) for i in xrange(len(y)) ] )
Y = fft(y)
YW = fft(yw)


maxfreq = 200
# Now smooth the data
for iY in range(maxfreq, len(Y)-maxfreq ) :
    Y[iY] = complex(0,0)
    if window:
        YW[iY] = complex(0,0)


powery = fft_power(Y)
poweryw = fft_power(YW)
powerx = array([ float(i) for i in xrange(len(powery)) ] )
Yre = [math.sqrt(Y[i].real**2+Y[i].imag**2) for i in xrange(len(Y))]


#Inverse transform
IY = ifft(Y)
IYW = ifft(YW)


#Adding back the linear fit
for iy in xrange(len(IY)) :
    IY[iy]=IY[iy]+315.472649452+0.0441692549556*iy+0.000155314201252*(iy**2)
    IYW[iy]=IYW[iy]+315.472649452+0.0441692549556*iy+0.000155314201252*(iy**2)


ax1 = plt.subplot(2, 1, 1)
p1, = plt.plot( x, y )
p2, = plt.plot( x, IYW )
ax1.legend( [p1,p2], ['Substracted', 'Smoothed'])

ax2 = plt.subplot(2, 1, 2)
p4, = plt.plot( powerx, powery )
p5, = plt.plot(powerx,poweryw)
ax2.legend( [p4, p5], ["Power", "Windowed Power"])
plt.yscale('log' )


plt.savefig('A3P3.png')
plt.show()
