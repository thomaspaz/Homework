These files in this folder are for Assignment #5 

Including codes and required output for 
Problem 1.) Data Fitting
	  - Text file for problem 1
	  - Text output from problem 1
	  - Graph of problem 1
Problem 2.) SDSS Data Fitting 
	  - FITS file for problem 2
	  - Text output from problem 2
	  - Graph of problem 2




Specific instructions for each problems are below.

******************************************************************

 DATA FITTING - ASSIGNMENT 5 - PROB 1    

 Use this data file, which gives the temperature in Munich every day fro several years. 
 Read in the data, and mask the bad values, then try and fit the following function to the data: 
 						f(t) = a * cos(2 * pi * t + b) + c
 		where t is the time in years. Make a plot of the data and the best-fit model in range 2008 to 2012. 
 a.) What are the best-fit values of the parameters? 
 b.) What is the overall average temperature in Munich, 
 	  and what are the typical daily average values predicted by the model for the coldest and hottest time of year?
 c.) What is the meaning of the ‘b’ parameter, and does its value make sense? 
 d.) Generate plot along with the best-fit model

******************************************************************

 SDSS DATA FITTING - ASSIGNMENT 5 - PROB 2     THOMAS PAZ

 Download the data from the SDSS DR13 APOGEE Survey main summary file. 
 You will be looking at fitting the any trend in radial velocity versus position. 
 Make the following selection of the data:
 Select APOGEE stars only with  -1< GLAT <+1

 Fit VHELIO_AVG (VERR) vs. GLATT (no error needed) 
 Fit three different functions:
   1) Linear; 2) quadratic fit ; 3) Periodic (sin or cos)

 a.) What are the best-fit values of the parameters?
 b.) Which function fits the data best?
 c.) Generate a plot for each fit (i.e. linear & polynomial) 
