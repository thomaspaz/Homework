These files in this folder are for Assignment #3 

Including codes and required output for 
Problem 1.) Plotting Experimental Data  
Problem 2.) The Quadratic Equation
Problem 3.) Heat Capacity of a Solid
Problem 4.) Numerical Integration


Specific instructions for each problems are below.

******************************************************************

PRECISION AND PLOTTING - ASSIGNMENT 3 - PROB 1 
There is a file in the on-line resources called stm.txt, which contains a grid of values from scanning tunneling microscope measurements of the (111) surface of silicon. 

A scanning tunneling microscope (STM) is a device that measures the shape of a surface at the atomic level by tracking a sharp tip over the surface and measuring quantum tunneling current as a function of position. The end result is a grid of values that represent the height of the surface and the file stm.txt contains just such a grid of values.

Write a program that reads the data contained in the file and makes a density plot of the values. 
Use the various options and variants you have learned about to make a picture that shows the structure of the silicon surface clearly.
******************************************************************

THE QUADRATUC EQUATION - ASSIGNMENT 3 - PROB 2 

a) Write a program that takes as input three numbers, a, b, and c, and prints out the two solutions to the quadratic equation 
ax2 + bx + c = 0 using the standard formula.
Use your program to compute the solutions of 
0.001x2 + 1000x + 0.001 = 0.

b) There is another way to write the solutions to a quadratic equation. Multiplying top and bottom of the solution above by −b ∓ √b2 − 4ac, show that the solutions can also be written as [EQ 2]Add further lines to your program to print these values in addition to the earlier ones and again use the program to solve 0.001x2 + 1000x + 0.001 = 0. 



What do you see? How do you explain it?

ANSWERS:
I SEE THAT THE ANSWERS FOR THE STANDARD EQUATION INTRODUCE A LARGER ERROR THAN WHEN CALCULATED WITH [EQ 2].
THIS IS DUE TO THE FACT THAT THE STANDARD EQ'N HAS SUBTRACTION OF A LARGE TERM IN THE RADICAL IN THE 		NUMERATOR VS. IN [EQ 2], WHICH THE SUBTRACTION OCCURS IN THE DENOM., WHICH MAKES THE DIFFERENCE SMALLER


c) Using what you have learned, write a new program that calculates both roots of a quadratic equation accurately in all cases.

******************************************************************

HEAT CAPACITY OF A SOLID - ASSIGNMENT 3 - PROB 3 

Debye’s theory of solids gives the heat capacity of a solid at temperature T to be... where V is the volume of the solid, ρ is the number density of atoms, kB is Boltzmann’s constant, and θD is the so-called Debye temperature, a property of solids that depends on their density and speed of sound.

a) Write a Python function cv(T) that calculates C_v for a given value of the temp, for a sample consisting of 1000 cubic centimeters of solid aluminum,  which has a number density of 
ρ = 6.022 × 1028 m−3 and a Debye temperature of θD = 428 K. 
Use Gaussian quadrature to evaluate the integral, with N = 50 sample points.

b) Use your function to make a graph of the heat capacity as a function of temp  from T = 5 K to T = 500 K.

******************************************************************

NUMERICAL INTEGRATION - ASSIGNMENT 3 - PROB 4

a) Write a program to calculate E(x) for values of x from 0 to 3 in steps of 0.1.Choose for yourself what method you will use for performing the integral and a suitable number of slices.

b) When you are convinced your program is working, extend it further to make a graph of E(x) as a function of x. 