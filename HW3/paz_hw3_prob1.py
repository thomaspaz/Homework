# PRECISION AND PLOTTING - ASSIGNMENT 3 - PROB 1 
# There is a file in the on-line resources called stm.txt, which contains a grid of values 
# from scanning tunneling microscope measurements of the (111) surface of silicon. 
# A scanning tunneling microscope (STM) is a device that measures the shape of a surface at 
# the atomic level by tracking a sharp tip over the surface and measuring quantum tunneling 
# current as a function of position. The end result is a grid of values that 
# represent the height of the surface and the file stm.txt contains just such a grid of values.
# Write a program that reads the data contained in the file and makes a density plot of the values. 
# Use the various options and variants you have learned about to make a picture that 
# shows the structure of the silicon surface clearly.


from numpy import loadtxt
from pylab import imshow,show,xlabel,ylabel,gray


data = loadtxt("stm.txt",float)


imshow(data,origin="lower")					
xlabel("x-axis")
ylabel("y-axis")

gray()
show()