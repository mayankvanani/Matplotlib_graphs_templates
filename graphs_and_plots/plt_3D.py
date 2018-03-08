from matplotlib import style
import  matplotlib.pyplot as plt 
import random

style.use('fivethirtyeight')

## fig is no. of different screen that we want
fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()

## defining a function to create random (x, y)
def create_plot():
	xs = []
	ys = []

	for i in range(10):
		x = i
		y = random.randrange(10)
		xs.append(x)
		ys.append(y)

	return xs, ys

##defining axes
## fig.add_subplot(height, width, index of plot)
ax1 = fig1.add_subplot(2,1,1)
ax2 = fig1.add_subplot(2,1,2)

## calling the function to generate data
## FIG-1 
x, y = create_plot()
ax1.plot(x,y)
x, y = create_plot()
ax2.plot(x,y)

## FIG-2
ax3 = fig2.add_subplot(2,1,2)
ax4 = fig2.add_subplot(2,2,1)
ax5 = fig2.add_subplot(2,2,2)

x, y = create_plot()
ax3.plot(x,y)
x, y = create_plot()
ax4.plot(x,y)
x, y = create_plot()
ax5.plot(x,y)

## FIG-3 (subplot2grid)
## easy to index and manipulate
ax6 = plt.subplot2grid((7,1), (0,0), rowspan=2, colspan=1)
ax7 = plt.subplot2grid((7,1), (2,0), rowspan=4, colspan=1)
ax8 = plt.subplot2grid((7,1), (6,0), rowspan=1, colspan=1)

x, y = create_plot()
ax6.plot(x,y)
x, y = create_plot()
ax7.plot(x,y)
x, y = create_plot()
ax8.plot(x,y)



plt.show()