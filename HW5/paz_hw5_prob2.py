
# SDSS DATA FITTING - ASSIGNMENT 5 - PROB 2     THOMAS PAZ

# Download the data from the SDSS DR13 APOGEE Survey main summary file. 
# You will be looking at fitting the any trend in radial velocity versus position. 
# Make the following selection of the data:
# Select APOGEE stars only with  -1< GLAT <+1

# Fit VHELIO_AVG (VERR) vs. GLATT (no error needed) 
# Fit three different functions:
#   1) Linear; 2) quadratic fit ; 3) Periodic (sin or cos)

# a.) What are the best-fit values of the parameters?
# b.) Which function fits the data best?
# c.) Generate a plot for each fit (i.e. linear & polynomial) 


# *************************************************************************************
# >VHELIO_AVG ----  TYPE: [float32]  UNITS: [km/s]  		# average radial velocity, weighted by S/N 
#   using RVs determined from cross-correlation of individual spectra with combined spectrum 

# > VERR ---------  TYPE: [float32]   UNITS:[km/s]  		# Uncertainty in VHELIO_AVG from S/N-weighted individual RVs

# > GLAT ---------  TYPE: [float64]   UNITS:[degrees] 		# Galactic latitude 

# > GLAN ---------  TYPE: [float64]   UNITS:[degrees] 		# Galactic longitude 
# *************************************************************************************

import fitsio
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import show,xlabel,ylabel, plot, xlim, ylim
from numpy import loadtxt, pi, cos, logical_and, std, mean, array



data = fitsio.FITS('allStar-l30e.2.fits')
cut = data[1].where('GLAT >-1 && GLAT<1')


position = data[1]['GLON'][cut]							# cut w/ GLAT but plotting w/ GLON
v_err = data[1]['VERR'][cut]
radial_velocity = data[1]['VHELIO_AVG'][cut]

# 														#Filtering out outliers.
v_err_cut = np.logical_and(v_err < 0.01,v_err > 0)		#from 1->0.5->0.2->0.02->0.01

x = position[v_err_cut]
y_err = v_err[v_err_cut]
y = radial_velocity[v_err_cut]



#Defining functions to be used in curve-fit
def line(x,slope,intercept):								# linear
	return slope * x + intercept

popt, pcov = curve_fit(line, x, y,sigma=y_err)			



def quad(x,a,b,intercept):									# quadratic
	return a * x**2 + b*x + intercept	

# guess_a = 0												# initial guess
# guess_b =-1
# guess_intercept = 50
# p01=[guess_a,guess_b,guess_intercept]
# fit1=curve_fit(quad,x,y,p0=p01)
# data_first_guess1=quad(x,*p01)
# data_fit1=quad(x,*fit1[0])

popt2, pcov2 = curve_fit(quad, x, y,sigma=y_err)



def cos_func (x , freq, amplitude, phase, offset):			# periodic 
	return amplitude * cos(x  * freq + phase )  + offset 

guess_freq = pi/100							
guess_amplitude = 100 					
guess_phase = 3.57
guess_offset = -1
p0 = array([guess_freq, guess_amplitude, guess_phase, guess_offset])	


fit = curve_fit(cos_func, x, y, p0 = p0)
data_first_guess = cos_func(x, *p0)				# initial guess. 
data_fit = cos_func(x, *fit[0])					# recreates fitcurve using optimized parameters.



fig, ax = plt.subplots()

ax.plot(np.sort(x),popt[0]*np.sort(x)+popt[1],label="Linear",linewidth=2)
ax.plot(np.sort(x),popt2[0]*np.sort(x)**2 + popt2[1]*np.sort(x)+popt2[2],label="Quadratic",linewidth=2)
plt.plot(x, data_first_guess, 'y',alpha= 0.5,label='First guess periodic')
plt.plot(x, data_fit, 'r',label='Periodic')


plt.scatter(x,y)
xlabel("Position [degrees]")
ylabel("Radial Velocity [km/s]")
plt.legend()
show()


# *************************************************************************************
# a.) What are the best-fit values of the parameters?
print("\na.)")
print("Best-Fit Values - Linear:")
print("Slope: {0:.2f}".format(popt[0]))
print("Intercept: {0:.2f}".format(popt[1]))

print("\nBest-Fit Values - Quadratic:")
print("Quadratic Coefficient: {0:.2f}".format(popt2[0]))
print("Linear Coefficient: {0:.2f}".format(popt2[1]))
print("Constant: {0:.2f}".format(popt2[2]))

print("\nBest-Fit Values - Periodic:")							# determined from the data files
print("Amplitude: {0:.2f}".format(fit[0][0]))
print("Phase: {0:.2f}".format(fit[0][1]))
print("Offset: {0:.2f}".format(fit[0][2]))


# *************************************************************************************
# b.) Which function fits the data best?"
print("\nb.)")
print("The periodic function fit the best,")
print("The data is not linear, and the quadratic is not following the trend of the data.")
print("We would want this to move peroidically, with it's position") 



