from pylab import plot,show
y=[1.0,2.4,1.7,0.3,0.6]
plot(y)
show()



from numpy import loadtxt
#from pylab import plot,show,xlabel,ylabel
from pylab import imshow,show,xlabel,ylabel,gray



data = loadtxt("stm.txt",float)
# x = data[:,0]
# y = data[:,1]



#plot(x,y,"mo")
#imshow(data)
imshow(data,origin="lower")					
#imshow(data,origin="lower",extent=[0,10,0,5])	#extent argument affects how the plot is labeled
xlabel("x-axis")
ylabel("y-axis")

gray()
show()