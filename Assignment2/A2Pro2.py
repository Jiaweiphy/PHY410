import matplotlib.pyplot as plt
from Parameter import *
from fft import fft
from numpy import array
import math

plotfirst = False

if plotfirst == True : 
    # make some fake data :

    N = 1024
    f = 10.0

    x = array([ float(i) for i in xrange(N) ] )
    y = array([ math.sin(-2*math.pi*f* xi / float(N))  for xi in x ])
    #y = array([ xi for xi in x ])
    Y = fft(y)

    Yre = [math.sqrt(Y[i].real**2 + Y[i].imag**2) for i in xrange(N)]

    s1 = plt.subplot(2, 1, 1)
    plt.plot( x, y )

    s2 = plt.subplot(2, 1, 2)
    s2.set_autoscalex_on(False)
    plt.plot( x, Yre )
    plt.xlim([0,20])

    plt.show()


else : 
    # data downloaded from ftp://ftp.cmdl.noaa.gov/ccg/co2/trends/co2_mm_mlo.txt
    print ' C02 Data from Mauna Loa'
    data_file_name = 'co2_mm_mlo.txt'
    file = open(data_file_name, 'r')
    lines = file.readlines()
    file.close()
    print ' read', len(lines), 'lines from', data_file_name
    #I'm making separate arrays for each of the y-columns, so that I can have them all available at once
    average = []
    interpolated = []
    trend = []
    xinput = []

    for line in lines :
        if line[0] != '#' :
            try:
                words = line.split()
                #Putting the pieces into the right places
                xval = float(words[2])
                avg = float(words[3])
                interp = float( words[4] )
                tren = float(words[5])
                average.append( avg )
                interpolated.append( interp )
                trend.append( tren )
                xinput.append( xval )
            except ValueError :
                print 'bad data:',line

    y1 = array( average[0:256] )
    y2 = array( interpolated[0:256] )
    y3 = array( trend[0:256] )
    x1 = array([ float(i) for i in xrange(len(y1)) ] )
    x2 = array([ float(i) for i in xrange(len(y2)) ] )
    x3 = array([ float(i) for i in xrange(len(y3)) ] )
    Y1 = fft(y1)
    Y2 = fft(y2)
    Y3 = fft(y3)
    Y1re = [math.sqrt(Y1[i].real**2+Y1[i].imag**2) for i in xrange(len(Y1))]
    Y2re = [math.sqrt(Y2[i].real**2+Y2[i].imag**2) for i in xrange(len(Y2))]
    Y3re = [math.sqrt(Y3[i].real**2+Y3[i].imag**2) for i in xrange(len(Y3))]
#giving initial parameters
    intercept = Parameter(0)
    linear = Parameter(1)
    quadratic = Parameter(0)
#defining my function:
    def f(x): return quadratic()*x**2 + linear()*x + intercept()
#And now I find the best fit for each of these
    fit(f,[intercept, linear, quadratic],y2,x2)
    print 'The best fit interpolated curve is y = ', quadratic(), 'x^2 + ', linear(), 'x + ', intercept(), '.'
    a2 = quadratic()
    b2 = linear()
    c2 = intercept()
    f2 = c2 + b2*x2 + a2*x2**2
    fit(f,[intercept, linear, quadratic],y3,x3)
    a3 = quadratic()
    b3 = linear()
    c3 = intercept()
    f3 = c3 + b3*x3 + a3*x3**2
    print 'The best fit trend curve is y = ', quadratic(), 'x^2 + ', linear(), 'x + ', intercept(), '.'

#Plotting all the things
    plt.subplot(2, 3, 1)
    plt.plot( x1, y1)
    plt.title('the average data')
    plt.subplot(2, 3, 2)
    plt.plot( x2,y2)
    plt.plot( x2,f2)
    plt.title('the interpolated data and fitting')
    plt.subplot(2, 3, 3)
    plt.plot(x3,y3)
    plt.plot(x3,f3)
    plt.title('the trend data and fitting')

    plt.subplot(2, 3, 4)
    plt.plot( x1, Y1re )
    plt.yscale('log')
    plt.subplot(2, 3, 5)
    plt.plot( x2, Y2re )
    plt.yscale('log')
    plt.subplot(2, 3, 6)
    plt.plot( x3, Y3re )
    plt.yscale('log')


plt.show()
