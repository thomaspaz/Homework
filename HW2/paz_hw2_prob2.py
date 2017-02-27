# THE SEMI-EMPIRICAL MASS FORMULA - ASSIGNMENT 2 - PROB 1
# In nuclear physics, the semi-empirical mass formula is a formula for calculating the approximate nuclear binding energy B of an atomic nucleus 
# with atomic number Z and mass number A
# where, in units of millions of electron volts, the constants are a1 = 15.67, a2 = 17.23, a3 = 0.75, a4 = 93.2, 
# and a5
# 		= 0 if A is odd
# 		= 12.0 if A and Z are both even  
# 		= -12.0 if A is even and Z is odd 
# Write a program that takes as its input the values of A and Z, and prints out the binding energy for the corresponding atom.
#  Use your program to find the binding energy of an atom with A = 58 and Z = 28. 



a1 = 15.67 	#UNITS: MeV 	
a2 = 17.23  #UNITS: MeV  
a3 = 0.75   #UNITS: MeV  
a4 = 93.2   #UNITS: MeV  

Z = int(input("Enter the atomic mass number Z:"))
A = int(input("Enter the mass number A:"))



if A % 2 == 0.0:

	if Z % 2 == 0.0 :
		a5 = 12.0
	else:
		a5 = -12.0 
else: 
	a5 = 0.0 


def mass_formula(A,Z) :
	B =  (a1*A) - (a2*(A**(2/3))) - (a3*((Z**2)/A**(1/3))) - (a4*((A-(2*Z))**2 / A)) - (a5/(A**(1/2)))
	return B

B=mass_formula(A,Z)  

BEnucleon= B/A


# part a.)
print ("The binding energy, B, for the corresponding atom is: ""{0:.3f}".format(B))


# part b.)
print ("The binding energy per nucleon, B/A, for the corresponding atom is: ""{0:.3f}".format(BEnucleon))


#Use your program to find the binding energy of an atom with A = 58 and Z = 28.
# Also with A = 59 and Z = 28.  Also with A = 58 and Z = 27.

B1= mass_formula(58,28)
print ("\nThe binding energy, B, for an atom with A=58 and Z=28 is: ""{0:.3f}".format(B1))

B2= mass_formula(59,28)
print ("The binding energy, B, for an atom with A=59 and Z=28 is: ""{0:.3f}".format(B2))

B3= mass_formula(58,27)
print ("The binding energy, B, for an atom with A=58 and Z=27 is: ""{0:.3f}".format(B3))

