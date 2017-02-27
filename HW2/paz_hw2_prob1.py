# SPECIAL RELATIVITY - ASSIGNMENT 2 - PROB 1
# Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, 
# then print out the time in years that the spaceship takes to reach its destination 
# (a) in the rest frame of an observer on Earth and 
# (b) as perceived by a passenger on board the ship. 
# Use your program to calculate the answers for a planet 10 light years away with v = 0.90c, v = 0.98c, v = 0.999c.

from math import sqrt 


# for part a.) & b.)
x = float( input("Enter the value of x, in lightyears: ") )
v = float( input("Enter the value of speed, v, as a fraction of the speed of light: ") )

# v = Relativistic speed to another planet		#UNITS: m / s^2 
# x = Distance from earth  					    #UNITS:  c  
# gamma = Relativistic factor 


gamma  =  1 / (sqrt(1 - (v**2)))

propertime = x * gamma 
tprime = x * ( 1/gamma )

print ("\nThe time in years that the spaceship takes to reach its destination is:")
print ("For an observer on Earth:" "{0:.2f}".format(propertime),"years")
print ("For passenger on ship:""{0:.2f}".format(tprime), "years")




# Use your program to calculate the answers for a planet 10 light years away with v = 0.90c, v = 0.98c, v = 0.999c.
t = 10 				#UNITS:  ly
v1 = 0.90			#UNITS:  c  
v2 = 0.98			#UNITS:  c  
v3 = 0.999			#UNITS:  c  

gammav1  =  1 / (sqrt(1 - (v1**2)))
gammav2  =  1 / (sqrt(1 - (v2**2)))
gammav3  =  1 / (sqrt(1 - (v3**2)))

tv1 = t * gammav1
tv1prime = t * (1/gammav1)

tv2 = t * gammav2
tv2prime = t * (1/gammav2)

tv3 = t * gammav3
tv3prime = t * (1/gammav3)

print ("\nThe time it takes a spaceship to reach a planet 10 light years away:")
print ("For an observer on Earth with v = 0.90c :" "{0:.3f}".format(tv1),"years")
print ("For passenger on ship with   v = 0.90c :" " {0:.3f}".format(tv1prime),"years")

print ("\nFor an observer on Earth with v = 0.98c :""{0:.3f}".format(tv2), "years")
print ("For passenger on ship with   v = 0.98c :"" {0:.3f}".format(tv2prime), "years")

print ("\nFor an observer on Earth with v = 0.999c :" "{0:.3f}".format(tv3),"years")
print ("For passenger on ship with   v = 0.999c :" "  {0:.3f}".format(tv3prime),"years")

