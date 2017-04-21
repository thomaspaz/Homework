
# DATA FITTING - ASSIGNMENT 5 - PROB 1     THOMAS PAZ

# Use this data file, which gives the temperature in Munich every day fro several years. 
# Read in the data, and mask the bad values, then try and fit the following function to the data: 
# 						f(t) = a * cos(2 * pi * t + b) + c
# 		where t is the time in years. Make a plot of the data and the best-fit model in range 2008 to 2012. 
# a.) What are the best-fit values of the parameters? 
# b.) What is the overall average temperature in Munich, 
# 	  and what are the typical daily average values predicted by the model for the coldest and hottest time of year?
# c.) What is the meaning of the ‘b’ parameter, and does its value make sense? 
# d.) Generate plot along with the best-fit model

import numpy as np  
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from numpy import loadtxt, pi, cos, logical_and, std, mean, array
from pylab import imshow,show,xlabel,ylabel, plot, xlim, ylim


data= array(np.loadtxt("munich_temperatures_average_with_bad_data.txt", usecols=[0,1], unpack=True)) 

date = data[0]
temp = data[1]	

keep = np.abs(temp) < 90   	

date = date[keep]
temp = temp[keep]

keep_date = date[logical_and(date >= 2008,date<2013)]			
keep_temp = temp[logical_and(date >= 2008,date<2013)]
date = keep_date
temp = keep_temp


date_mod = date[abs(temp) < (3 * std(temp) + mean(temp))]
temp_mod = temp[abs(temp) < (3 * std(temp) + mean(temp))]


guess_freq = 2* pi
guess_amplitude = 25
guess_phase = 0
guess_offset = mean(temp_mod)


p0 = array([guess_freq, guess_amplitude, guess_phase, guess_offset])	

	
def cos_func (x , freq, amplitude, phase, offset):					# defining function to fit data. 
	return amplitude * cos(x  * freq + phase )  + offset 


fit = curve_fit(cos_func, date_mod, temp_mod, p0 = p0)				

data_first_guess = cos_func(temp_mod, *p0)			# plots initial guess.

data_fit = cos_func(date_mod, *fit[0])					# recreates fitcurve using optimized parameters.

# *************************************************************************************
# d.) Generate plot along with the best-fit model

plt.plot(date,temp, '-')
plt.plot(date_mod, data_first_guess, alpha= 0.2,label='first guess')
plt.plot(date_mod, data_fit, label='after fitting')

xlim(min(date_mod),max(date_mod))
plt.legend()
xlabel("Time [years]")
ylabel("Temperature [C$\degree$]")
show()

# *************************************************************************************
# a.) What are the best-fit values of the parameters? 

print("The best-fit values of the parameters:")							# determined from the data files
print("Amplitude: {0:.2f}".format(fit[0][0]))
print("Phase: {0:.2f}".format(fit[0][1]))
print("Offset: {0:.2f}".format(fit[0][2]))

# *************************************************************************************
# b.) What is the overall average temperature in Munich, 
# 	  and what are the typical daily average values predicted by the model for the coldest and hottest time of year?

print("\nThe overall average temperature in Munich: ---------------- {0:.2f} degrees Celsius".format(mean(data_fit)))
print("The typical daily avaerages predicted by the model:")
print("  Daily average for coldest time of year: ----------------- {0:.2f} degrees Celsius".format(min(data_fit)))
print("  Daily average for hottest time of year: ----------------- {0:.2f} degrees Celsius".format(max(data_fit)))

# *************************************************************************************
# c.) What is the meaning of the ‘b’ parameter, and does its value make sense? 

# print("c\n")
# print("The b parameter is the horizontal shift of the cosine function.") 
# print("	If the shift were zero, we'd be assuming the minimum temperature occurred on January 1st of every year.") 
# print("	This isn't quite true, though we know it probably occurs sometime around there, so the shift shouldn't be too large.") 
# print("The value here makes sense, and suggests the minimum temperature occurs a short time after January 1st.")

print("\nThe b parameter represents the phase shift of the cosine function.") 
print("This value makes sense because this represents the amount the cosine wave has horizontally shifted from the original wave")
print("This is also apparent from the context of our data, as a local minimum - physically meaning that the minimum temperature in Munich occurs around mid-January")


