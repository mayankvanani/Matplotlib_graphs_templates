import matplotlib.pyplot as plt  
import csv
import numpy as np 

## example.txt is used here to read values from it
## create an empty list to store/ append values read from files
x = []
y = []

## with open(path, read/write) as csvfile
## the read values have dtype=strings and it needs to be converted to integer
with open('example.txt', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for column in plots:
		print(column)
		x.append(np.int8(column[0]))
		y.append(np.int8(column[1]))

plt.plot(x,y, label='loaded from file!')

plt.xlabel('colums_0 nos')
plt.ylabel('colums_1 nos')
plt.title('loaded from file')
plt.legend()
plt.show()
