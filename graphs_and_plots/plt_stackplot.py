import matplotlib.pyplot as plt

## day number. eg: day1, day2, day3, ...
day = [1,2,3,4,5]

## activities during days and hrs dedicated to each activities correspoding to that day
sleeping = [7,8,7,6,9]
eating = [2,3,1,2,3]
working = [10,11,8,10,10]
playing = [1,2,1,1,0]


## stack plot
## plt.stackplot(x_element, Y_ELEMENTS, color for each element)
plt.stackplot(day, sleeping, eating, working, playing, colors=['b','r','g','y'], labels=['sleep','eat','work','play'])

## sometimes if labels or any other stuff can be done the nfake plots can be created
## eg : 
## plt.plot([],[], color='b', label='sleep')
## plt.plot([],[], color='r', label='eat')
## plt.plot([],[], color='g', label='work')
## plt.plot([],[], color='y', label='play')
##  so see what this does uncomment the above and remove labels from plt.stackplot()


plt.xlabel('rand_x')
plt.ylabel('rand_y')
plt.title('stack_plot')
plt.legend()
plt.show()
