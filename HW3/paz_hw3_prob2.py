# THE QUADRATUC EQUATION - ASSIGNMENT 3 - PROB 2 


# a) Write a program that takes as input three numbers, a, b, and c, and prints out 
#	the two solutions to the quadratic equation ax2 + bx + c = 0 using the standard formula
#	Use your program to compute the solutions of 0.001x2 + 1000x + 0.001 = 0.

from math import sqrt 
from decimal import Decimal 

# a = float( input("Enter the value of a: ") )
# b = float( input("Enter the value of b: ") )
# c = float( input("Enter the value of c: ") )
a = float(0.001)
b = float(1000)
c = float(0.001)

x1 = (-b + sqrt(b**2 - 4*a*c) ) / (2 * a)		# [EQ 1]
x2 = (-b - sqrt(b**2 - 4*a*c) ) / (2 * a)		# [EQ 1]

print("The solution to 0.001x^2 + 1000x + 0.001 = 0 using the standard formula is:")
print("  x = ",x1)
print("  or x = ",x2)


#*************************************************************************************
# b) There is another way to write the solutions to a quadratic equation. 
#	Multiplying top and bottom of the solution above by −b ∓ √b2 − 4ac, 
#	show that the solutions can also be written as [EQ 2]
#	Add further lines to your program to print these values in addition to the earlier ones 
#	and again use the program to solve 0.001x2 + 1000x + 0.001 = 0. 


x3 = (2 * c) / (-b - sqrt(b**2 - 4*a*c) ) 		# [EQ 2]
x4 = (2 * c) / (-b + sqrt(b**2 - 4*a*c) ) 		# [EQ 2]

print("\nThe solution to 0.001x^2 + 1000x + 0.001 = 0 using 2c / (−b ∓ √(b2 − 4ac)) is:")
print("  x = ",x3)
print("  or x = ",x4)

#	What do you see? How do you explain it?
#		ANSWERS:
#			I SEE THAT THE ANSWERS FOR THE STANDARD EQUATION INTRODUCE A LARGER ERROR 
#				THAN WHEN CALCULATED WITH [EQ 2]
#			THIS IS DUE TO THE FACT THAT THE STANDARD EQ'N HAS SUBTRACTION OF A LARGE TERM
#				IN THE RADICAL IN THE NUMERATOR VS. IN [EQ 2], WHICH THE SUBTRACTION OCCURS
#				IN THE DENOM., WHICH MAKES THE DIFFERENCE SMALLER



#*************************************************************************************
# c) Using what you have learned, write a new program that calculates 
#	both roots of a quadratic equation accurately in all cases.

a = Decimal(0.001)
b = Decimal(1000)
c = Decimal(0.001)


det = b - ((4*a*c)/(2*b))   	# [EQ 3]  		# Using √(b2 − 4ac) approx. = [EQ 3]

x5 = (2 * c) / (-b - det ) 		# [EQ 4]		# Using [EQ 2] & plugging in [EQ 3]
x6 = (2 * c) / (-b + det ) 		# [EQ 4]

print("\nThe solution to 0.001x^2 + 1000x + 0.001 = 0 using a more acurate formula is:")
print("  x = ",x5)
print("  or x = ",x6)



