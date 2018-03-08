import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style
import numpy as np 

style.use('fivethirtyeight')

## ----DIRECTION TO USE-----
## run this probram
## open the example.txt file
## append the values/add the values/ remove the values to example.txt
## save the example.txt and note the changes in graph

fig = plt.figure()
## add_subplot(x,y,z) returns xth subplot with y rows and k columns
ax1 = fig.add_subplot(1,1,1)

## interval of refresing a graph
def animate(i):
	x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

	## clearign previously drawn plot in order to draw new and appended plot
	ax1.clear()
	## plotting the appended data
	ax1.plot(x, y)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


 
