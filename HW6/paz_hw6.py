
# NONLINEAR PENDULUM - ASSIGNMENT 6 -  THOMAS PAZ


# Building on the results from Example 8.6, calculate the motion of a nonlinear pendulum as follows.
# a.) Write a program to solve the two first-order equations, Eqs. (8.45) and (8.46), 
# 		using the fourth-order Runge–Kutta method for a pendulum with a 14 cm arm. 
# 		Use your program to calculate the angle θ of displacement for several periods of the pendulum 
# 		when it is released from a standstill at θ = 178 deg from the vertical. (pointing almost upward)
# 	Make a graph of θ as a function of time.

# b.) Write a program to solve the two first-order equations, Eqs. (8.45) and (8.46), 
# 		using the fourth-order Leapfrog method for a pendulum with a 14 cm arm. 
# 		Use your program to calculate the angle θ of displacement for several periods of the pendulum 
# 		when it is released from a standstill at θ = -90 deg from the vertical. (pointing almost horizontal)
# 	Make a graph of θ as a function of time.


# c.) Extend your program to create an animation of the motion of the pendulum. 
# 		Your animation should, at a minimum, include a representation of the moving pendulum bob and the pendulum arm. 
# 		(Hint: You will probably find the function rate discussed in Section 3.5 useful for making your animation run at a sensible speed. 
# 		Also, you may want to make the step size for your RungeKutta calculation smaller than the framerate of your animation, i.e., do several Runge–Kutta steps per frame on screen. 
# 		This is certainly allowed and may help to make your calculation more accurate.)




import numpy as np
from math import sin, pi
from numpy import arange, array
from pylab import plot,xlabel,ylabel,show, xlim, ylim
import matplotlib.pyplot as plt
import matplotlib.animation as animation


##*************************************************************************************
##  a.) Write a program to solve the two first-order equations, using the fourth-order Runge–Kutta method

theta_i = 178 							# [degrees] from vertical
l = 0.14 								# [meters]
g = 9.81								# [m/s^2]

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega 						# [eq.8.45]
    fomega = -g/l*sin(theta) 			# [eq.8.46]
    return array([ftheta,fomega],float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
theta = []
r = array([theta_i,0],float)

for t in tpoints:
    theta.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6



plot(tpoints,theta)
ylim(min(theta)-1,max(theta)+1)
xlabel('Time [seconds]')
ylabel('θ(t) - angle [degrees]')
plt.title('RK-4 Method')

show()


##*************************************************************************************
# # b.) Write a program to solve the two first-order equations, using the fourth-order Leapfrog method

# # 		**** NOTE! ****  PART B IS NOT RUNNING IN ORDER FOR PART C TO FUNCTION


# theta_i2 = -90 						# [degrees] from vertical
# # h = 0.01
# # h = 0.001
# # h = 0.005
# h = 0.002							# determining best size of 'h' after plotting	
 
# tpoints = arange(a,b,h)
# theta = []


# r = array([theta_i2,0],float)

# for t in tpoints:
# 	theta.append(r[0])
# 	lf1 = h * f(r, t)
# 	lf2 = h * f(r + 0.5*lf1, t + 0.5*h)
# 	lf3 = h * f(r + lf2, t + h)
# 	r += 0.5*lf1 + lf3


# plot(tpoints,theta)
# xlabel('Time [seconds]')
# ylabel('θ(t) - angle [degrees]')
# plt.title('LF Method')
# plt.show()


## *************************************************************************************
## c.) Extend your program to create an animation of the motion of the pendulum. 


x = tpoints
y = theta

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k')

def update(num, x, y, line):
    line.set_data(tpoints[:num], theta[:num])
    line.axes.axis([-1, 10, 170, 180])
    return line,


ani = animation.FuncAnimation(fig, update, len(x) ,fargs=[x, y, line], interval=5, blit=False)		# IF ON MAC; blit=False !!!
# ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line], interval=25, blit=True)   # IF ON WINDOWS; blit=True !!!


ylim(min(theta)-1,max(theta)+1)
xlabel('time [seconds]')
ylabel('x(t) - angle [degrees]')


plt.show()

# # *************************************************************************************

