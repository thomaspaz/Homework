# RADIOACTIVE DECAY CHAIN - ASSIGNMENT 4 - PROB 1

# The isotope 213-Bi decays to stable 209-Bi via one of two different routes 
#	 Starting with a sample consisting of 10 000 atoms of 213Bi, 
#		simulate the decay of the atoms as in Example 10.1 by dividing time into slices of length δt = 1 s each 
# 		and on each step doing the following:
#	
#  		a.) For each atom of 209-Pb in turn, decide at random, with the appropriate probability, whether
#			it decays or not. (The probability can be calculated from Eq. (10.3).) Count the total number
#			that decay, subtract it from the number of 209Pb atoms, and add it to the number of 209Bi atoms.

#  		b.) Now do the same for 209Tl, except that decaying atoms are subtracted from the total for 209Tl 
#			and added to the total for 209Pb.

#  		c.) For 213Bi the situation is more complicated: when a 213Bi atom decays you have to decide at random 
#			with the appropriate probability the route by which it decays. 
#			Count the numbers that decay by each route and add and subtract accordingly.



from random import random
from numpy import arange
from matplotlib import pyplot as plt



NBi_213 = 10000					 
NTl_209 = 0
NPb_209 = 0
NBi_209 = 0
tmax = 20000  						 	# Steps of Time
h = 1.0  							 	# Size of Steps of Time


tau_Bi_213 = 46 * 60  				 	# Bi 213 halflife in seconds
prob_Bi_213 = 1 - 2**(-h / tau_Bi_213)  # Probability of Bi 213 decay

tau_Tl_209 = 2.2 * 60  				 	# Tl 209 halflife in seconds
prob_Tl_209 = 1 - 2**(-h / tau_Tl_209)  # Probability of Tl 209 decay

tau_Pb_209 = 3.3 * 60  				 	# Pb 209 halflife in seconds
prob_Pb_209 = 1 - 2**(-h / tau_Pb_209)  # Probability of Pb 209  decay

prob_Pb_to_Tl = 0.9791  				# probability of Bi 213 decay to Pb 209 vs Tl 209

tval = arange(0.0, tmax, h)		 		# Time Value Array


Bi_213points = [[] for t in range(len(tval))]
Tl_209points = [[] for t in range(len(tval))]
Pb_209points = [[] for t in range(len(tval))]
Bi_209points = [[] for t in range(len(tval))]


for t in range(len(tval)):
	Bi_213points[t] = NBi_213		 
	Tl_209points[t] = NTl_209		 
	Pb_209points[t] = NPb_209
	Bi_209points[t] = NBi_209



	decay = 0						 
	dec_into_Pb = 0					 
	for i in range(NBi_213):		 
		if random() < prob_Bi_213:		 
			decay += 1
			if random() < prob_Pb_to_Tl:  
				dec_into_Pb += 1
	NBi_213 -= decay
	NPb_209 += dec_into_Pb
	NTl_209 += (decay - dec_into_Pb)  
									 
									 

	decay = 0						
	for i in range(NTl_209):
		if random() < prob_Tl_209:		 
			decay += 1
	NTl_209 -= decay
	NPb_209 += decay

	decay = 0						 
	for i in range(NPb_209):
		if random() < prob_Pb_209:		 
			decay += 1
	NPb_209 -= decay
	NBi_209 += decay



fig, ax = plt.subplots()			
ax.plot(tval, Bi_213points, label="Bi 213")
ax.plot(tval, Tl_209points, label="Tl 209")
ax.plot(tval, Pb_209points, label="Pb 209")
ax.plot(tval, Bi_209points, label="Bi 209")
ax.set_title("Bi-213 Radioactive Decay")
ax.set_ylabel("Number of Atoms")
ax.set_xlabel("Time [s])")
ax.legend(loc="best")
plt.show()


