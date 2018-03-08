import matplotlib.pyplot as plt

## plotting x vs y where x,y = [lists]
## plt.plot([x], [y], label)
## label is key of graph
x1 = [1,2,3,4]
y1 = [1,8,2,4]

x2 = [1,2,3,8]
y2 = [10,16,13,18] 

plt.plot(x2,y2, label='plot_1')
plt.plot(x1, y1, label='plot_2')

## labelling x axis and y axis
plt.xlabel('random nos x- axis')
plt.ylabel('random nos y-axis')

## title of graph
##\n is for pressing enter to write the title in new line
plt.title('rand_x V/S rand_y\ncheck it out!')

## this bring the labels of the plot to frontend as key of graph
plt.legend()









## plt.show() brings the backend processed stuff to forefront
plt.show()