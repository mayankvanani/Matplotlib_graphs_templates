import matplotlib.pyplot as plt  
import numpy as np 

## using numpy to read data from csv/txt files
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='loaded from file!')

plt.xlabel('colums_0 nos')
plt.ylabel('colums_1 nos')
plt.title('loaded from file')
plt.legend()
plt.show()