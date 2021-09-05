#import numpy to handle arrays
import numpy as np

#import matplotlib to create plots
import matplotlib.pyplot as plt

#allows for curve fitting
import scipy.optimize as opt;

#import data. assumes comments are # are data is separated by white space
#the unpack is required to read in vertical data arrayss

xdata,ydata, yerror = np.loadtxt('extension-data.txt' ,unpack=True)



#the function we are fitting, called func

def func(x,a):
     return a*x


#fit the data
#The sigma = means you will be doing a fit weighted by the uncertainty in y
parameters, covariance = opt.curve_fit(func, xdata, ydata,sigma = yerror)

#Plots the data.  You can play around with the paramters of the plot to change color, shape, etc
#You will likely want to give it a better name than 'data' and will want to change colors, etc
# when you have multiple fits ont he same page
plt.errorbar(xdata,ydata,yerr=yerror,capsize = 5,marker = 'o',linestyle = 'None', label = 'data')

#Plots the fit
plt.plot(xdata,func(xdata,*parameters),label = 'fit')

#insert the legend
plt.legend(loc = 'upper left')


#This prints the fitting parameter
print(parameters)

#calculate the error on the fits from the covariacne matrix
perr = np.sqrt(np.diag(covariance))

#Print the erros on the fits


print(perr)

#print(covariance)


#plt.yscale('log')
#plt.yscale('linear') 



#axes titles
plt.xlabel('x-axis name (units)', fontsize = 16)
plt.ylabel('y-axis name (units)', fontsize = 16)

plt.title('Plot title!', fontsize = 18)


#Show the plot!
#plt.show()

