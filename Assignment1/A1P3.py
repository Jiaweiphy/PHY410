import math
import numpy as np
import matplotlib.pyplot as plt


def chi_square_fit(x, y, err):
    n = len(x)
    if n < 2 :
        print 'Error! Need at least 2 data points!'
        exit()
    S = sum(1/err[i]**2 for i in range(n))
    if abs(S) < 0.00001 :
        print 'Error! Denominator S is too small!'
        exit()
    S_x = sum(x[i]/err[i]**2 for i in range(n))
    S_y = sum(y[i]/err[i]**2 for i in range(n))
    t = [(x[i] - S_x/S) / err[i] for i in range(n)]
    S_tt = sum(t_i**2 for t_i in t)
    if abs(S_tt) < 0.00001 :
        print 'Error! Denominator S is too small!'
        exit()
    b = sum(t[i]*y[i]/err[i] for i in range(n)) / S_tt
    a = (S_y - S_x * b) / S
    sigma_a2 = (1 + S_x**2/S/S_tt) / S
    sigma_b2 = 1/S_tt
    if sigma_a2 < 0.0 or sigma_b2 < 0.0 :
        print 'Error! About to pass a negative to sqrt'
        exit()
    sigma_a = math.sqrt(sigma_a2)
    sigma_b = math.sqrt(sigma_b2)
    chi_square = sum(((y[i] - a - b*x[i]) / err[i])**2 for i in range(n))
    return(a, b, sigma_a, sigma_b, chi_square)

print ' Chi-square fit of supernova data to a straight line'
print ' Reference: http://dark.dark-cosmology.dk/~tamarad/SN/'
data_file = open('Davis07_R07_WV07.dat', 'r')

lines = data_file.readlines()
data_file.close()
data = [ str.split(line) for line in lines if line[0] != ';' ]
print ' read', len(data), 'data values'
lzlogz_data = []
lzmu_data = []
lzmu_err_data = []
hzlogz_data = []
hzmu_data = []
hzmu_err_data = []


#Separate low and high redshift
for datum in data:
    if math.log10(float(datum[1])) < -1 :
        lzlogz_data.append(math.log10(float(datum[1])) )
        lzmu_data.append(float(datum[2]) )
        lzmu_err_data.append(float(datum[3]) )
    else:
        hzlogz_data.append(math.log10(float(datum[1])) )
        hzmu_data.append(float(datum[2]))
        hzmu_err_data.append(float(datum[3]) )


for i_mu_err_data in lzmu_err_data :
    if abs(i_mu_err_data) < 0.000001 :
        print 'Error! Uncertainties are too small!'
        exit()

for i_mu_err_data in hzmu_err_data :
    if abs(i_mu_err_data) < 0.000001 :
        print 'Error! Uncertainties are too small!'
        exit()

plt.scatter( lzlogz_data, lzmu_data, color='blue' )
plt.scatter (hzlogz_data, hzmu_data,color = 'red')
#print lzlogz_data and hzlogz_data

lzfit = chi_square_fit(lzlogz_data, lzmu_data, lzmu_err_data)
hzfit = chi_square_fit(hzlogz_data, hzmu_data, hzmu_err_data)
#plt.plot(lzfit,color='blue')
#plt.plot(hzfit,color='red')
print 'high redshift slope =', hzfit[1], ' +- ', hzfit[3]
print ' intercept =', hzfit[0], '+-', hzfit[2]
if len(data) - 2 > 0 :
    print ' chi-square/d.o.f. = ', hzfit[4]/(len(data)-2)
else :
    print ' chi-square/d.o.f. undefined'

print 'low redshift slope =', lzfit[1], ' +- ', lzfit[3]
print ' intercept =', lzfit[0], '+-', lzfit[2]
if len(data) - 2 > 0 :
    print ' chi-square/d.o.f. = ', lzfit[4]/(len(data)-2)
else :
    print ' chi-square/d.o.f. undefined'

plt.show()
