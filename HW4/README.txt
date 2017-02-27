These files in this folder are for Assignment #4 

Including source codes and required output for 
Problem 1.) Radioactive Decay 
Problem 2.) Monte Carlo Integration

Specific instructions for each problems are below.

******************************************************************

RADIOACTIVE DECAY - ASSIGNMENT 4 - PROB 1

The isotope 213-Bi decays to stable 209-Bi via one of two different routes.
Starting with a sample consisting of 10 000 atoms of 213Bi, 
simulate the decay of the atoms as in Example 10.1 by dividing time into slices of length δt = 1 s each and on each step doing the following:

a.) For each atom of 209-Pb in turn, decide at random, with the appropriate probability, whether it decays or not. (The probability can be calculated from Eq. (10.3).) Count the total number that decay, subtract it from the number of 209Pb atoms, and add it to the number of 209Bi atoms.

b.) Now do the same for 209Tl, except that decaying atoms are subtracted from the total for 209Tl and added to the total for 209Pb.

c.) For 213Bi the situation is more complicated: when a 213Bi atom decays you have to decide at random with the 	appropriate probability the route by which it decays. Count the numbers that decay by each route and add and subtract accordingly.

******************************************************************

MONTE CARLO INTEGRATION - ASSIGNMENT 4 - PROB 2

Calculate a value for the integral using the importance sampling formula, Eq. (10.42), with w(x) = x**(1/2), as follows.

a) Show that the probability distribution p(x) from which the sample points should be drawn is given by 
p(x)=1/	(2sqrt(x))
and derive a transformation formula for generating random numbers between zero and one from this distribution.

b) Using your formula, sample N = 1 000 000 random points and hence evaluate the integral. 