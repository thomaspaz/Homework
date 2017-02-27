#ALTITUDE OF A SATELLITE

from math import pi

G = 6.67e-11 #UNITS: m^3 kg^-1 s^-2 	Newton's gravitiational constant
M = 5.97e24  #UNITS: kg     			Mass of the Earth
R = 6371     #UNITS: km 				Radius of the Earth



print("This program calculates the altitude, in meters, that a sattelite must have.")

T = int(input("Enter the desired value of T in standard notation: "))

h = ( (G*M*T**2) / (4*pi**2) ) **(1/3.0) - R

print("You have entered a period T=",T,"seconds")
print("The calculated altitude is","{:.2e}".format(h),"meters")

#PART (c) - Use your program to calculate the altitudes of satellites that orbit
 #the Earth once a day, once every 90 minutes, once every 45 minutes

input('\nPress enter to continue: ')
print("Here are some uselful altitude calculations for different periods:")


#PART (c) - Use your program to calculate the altitudes of satellites that orbit
 #the Earth once a day, once every 90 minutes, once every 45 minutes

T1 = 86400 		#UNITS: s     	Period of 24 hr
T2 = 5400		#UNITS: s     	Period of 90 min
T3 = 2700		#UNITS: s     	Period of 45 min


h1 = ( (G*M*T1**2) / (4*pi**2) ) **(1/3.0) - R
h2 = ( (G*M*T2**2) / (4*pi**2) ) **(1/3.0) - R
h3 = ( (G*M*T3**2) / (4*pi**2) ) **(1/3.0) - R


print("For 24 hr period,  h = ""{:.2e}".format(h1),"meters")
print("For 90 min period, h = ""{:.2e}".format(h2),"meters")
print("For 45 min period, h = ""{:.2e}".format(h3),"meters")



#Technically a geosynchronous satellite is one that orbits the Earthonce per day, which is 23.93 hours, not 24 hours. 
 #And how much difference will it make to the altitude of the satellite?

Tgeo = 86148 		#UNITS: s    Period for geosynchronous orbit
h3 = ( (G*M*Tgeo**2) / (4*pi**2) ) **(1/3.0) - R
diff = h1 - h3		#Difference b/w true geosync. orbit & 24 hr orbit


print("Difference between periods of 23.93 hrs & 24 hrs: ""{:.2e}".format(diff),"meters")


