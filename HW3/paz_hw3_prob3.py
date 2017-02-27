# HEAT CAPACITY OF A SOLID - ASSIGNMENT 3 - PROB 3 

# Debye’s theory of solids gives the heat capacity of a solid at temperature T to be...
# where V is the volume of the solid, ρ is the number density of atoms, kB is Boltzmann’s constant, 
# and θD is the so-called Debye temperature, a property of solids that depends on their density and speed of sound.


# a) Write a Python function cv(T) that calculates C_v for a given value of the temp, 
#	 for a sample consisting of 1000 cubic centimeters of solid aluminum, 
#	 which has a number density of ρ = 6.022 × 1028 m−3 and a Debye temperature of θD = 428 K. 
#	 Use Gaussian quadrature to evaluate the integral, with N = 50 sample points.

from numpy import exp,linspace
from pylab import plot,show,xlabel,ylabel



kB = 1.38064852E-23	#UNITS:  J*K^-1		Boltzmann’s constant
ρ = 6.022E+28		#UNITS:  m^-3 		Number density
θD = 428			#UNITS:  K 			Debye temp.
V = 1000			#UNITS:  cm^3		Volume
T = 50				#UNITS:  K 			Temperature 
#T = float( input("Enter the value of T, kelvin: ") )	#Temperature 


def cv(x):
	return  x**4 * exp(x) / (exp(x)-1**2)

N = 1000
a = 0.0
b = θD / T
h = (b-a)/N

s = 0.5*cv(a) + 0.5*cv(b)
for k in linspace(1,N):
	s += cv(a+k*h)


Cv = ( 9 *  V * ρ * kB * (T / θD)**3 ) * (h*s)

print("The heat capacity for solid Al for the given temperature is: ",Cv)


#*************************************************************************************
# b) Use your function to make a graph of the heat capacity as a function of temp 
#	 from T = 5 K to T = 500 K.

yaxis = []   					#Creates an empty array to populate 
xaxis = []

# for n in range(5,505,25):
# 	t = n + 25
# 	yaxis.append(cv(t))			#Appends values calculated from function 
# 	xaxis.append(t)				# and puts them into the empty array one by one on the end

for n in linspace(5,505,25):
	t = n + 25
	yaxis.append(cv(t))			#Appends values calculated from function 
	xaxis.append(t)				# and puts them into the empty array one by one on the end 

plot(xaxis,yaxis,"mo")
xlabel("Temperature [K]")
ylabel("Heat Capacity  [Cv]")
show()



