#example histogram plot routine
#
import matplotlib.pyplot as plt
import numpy as np
from numpy import *; from pylab import *
#
data=[]
n=0

#Just a different way to read in data if you'd like
filename='Q.txt'

f=open(filename,"r")
# 
#	
data=loadtxt(filename)
f.close()
#
# note this data file had Qc's ranging from 0 to 12, that is, I ditched the x10^-19 
# the histogram will go over this whole range with "steps" of 0.2
#
# you should adjust the min, max, and bin size as you need or like
#
bin_size = 0.2; min_edge = 0; max_edge =12.
N = int((max_edge-min_edge)/bin_size)
Nplus1 = N + 1
bin_list = np.linspace(min_edge, max_edge, Nplus1)


#This section lets you plot histograms in the classic bar graph
# It is not particularly useful for fitting data but is useful for visualization
plt.hist(data,bin_list)
plt.title("Bin size 0.2E-19 C")
plt.xlabel("charge (C x 10-19)")
plt.ylabel('number of drops')
#plt.axis([0.,12,0,120])
plt.grid()
plt.show()
plt.close()


#This calculates the histogram data so you can manipulate it later
#The a value is the number of items in each bin
#The b value is the edges of the bins
a,b=np.histogram(data,bin_list)

#This line is needed so you can find the middle x posistion for each bin,
#as the line above gives you the left and right edges (and will have one more
# data pointt han will the a values
bplot = b+(b[0]+b[1])/2
bplot = bplot[:-1] - min_edge

plt.plot(bplot,a,'-o')
plt.title("Bin size 0.2E-19 C")
plt.xlabel("charge (C x 10-19)")
plt.ylabel('number of drops')
#plt.axis([0.,12,0,120])
plt.grid()
plt.show()
plt.close()
