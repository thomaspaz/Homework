# NUMERICAL INTEGRATION - ASSIGNMENT 3 - PROB 4

# a) Write a program to calculate E(x) for values of x from 0 to 3 in steps of 0.1. 
#	 Choose for yourself what method you will use for performing the integral 
#	 and a suitable number of slices.


from math import erfc, sqrt,pi
from gaussxw import gaussxw
from numpy import exp,linspace
from pylab import plot,show,xlabel,ylabel

def E(x):
    return exp(x**2)
  

N = 30
a = 0.0
b = 3.0


x,w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w


s = 0.0
for k in range(N):
    s += wp[k]*E(xp[k])

print(s)


#*************************************************************************************
# b) When you are convinced your program is working, 
#	 extend it further to make a graph of E(x) as a function of x. 


yaxis = []   						#Creates an empty array to populate 
xaxis = []
 

for n in linspace(0,3):
	p = n + 0.10
	yaxis.append(E(p))				#Appends values calculated from function
	xaxis.append(p)					# and puts them into the empty array one by one on the end 
				

plot(xaxis,yaxis,"mo")
xlabel("x")
ylabel("E(x)")
show()