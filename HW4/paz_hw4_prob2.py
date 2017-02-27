# MONTE CARLO INTEGRATION - ASSIGNMENT 4 - PROB 2


#  Calculate a value for the integral    
#	using the importance sampling formula, Eq. (10.42), with w(x) = x**(1/2), as follows.

# a) Show that the probability distribution p(x) from which the sample points should be drawn is given by
#		p(x)=1/(2sqrt(x))
#	and derive a transformation formula for generating random numbers between zero and one from this distribution.

#	 b) Using your formula, sample N = 1 000 000 random points and hence evaluate the integral. 
	 

from numpy import exp, sqrt
from random import random

N = int(1000000) 
value_integral = 2 
			 


def prob_rand():
	
	value_random = (random())**2

	return value_random


sum_integral = float(0)

for i in range(N):  
	temp = prob_rand()  
	f_x = (temp**(-1 / 2)) / (exp(temp) + 1)
	w_x = temp**(-1 / 2)

	sum_integral += (f_x / w_x)

I = (1 / N) * sum_integral * value_integral  
								

print(I)


