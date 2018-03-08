import matplotlib.pyplot as plt 

x = [1,2,6,5,9,8,20,15]
y = [2,3,4,8,9,10,12,14]

## scatter plot
## marker just changes the point style in the graph
## s = size of the point , I guess default is 10
plt.scatter(x, y, label='scattered', color='k', marker='*', s=100)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('scatter plot')
plt.legend()
plt.show()