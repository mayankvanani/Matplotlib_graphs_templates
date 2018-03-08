import matplotlib.pyplot as plt

## day number. eg: day1, day2, day3, ...
day = [1,2,3,4,5]

## activities during days and hrs dedicated to each activities correspoding to that day
sleeping = [7,8,7,6,9]
eating = [2,3,1,2,3]
working = [10,11,8,10,10]
playing = [1,2,1,1,3]

## slices here is the final slice viz. last element of all activities
slices = [9,3,10,3]
activities = ['sleep','eat','work','play']
colors = ['y','r','g','b']

## piechart
## start angle specifies at which angle to start the pie chart
## shadow=true adds the shadow effect and gives a more 3D kinda view
## explode() draws out that particular piece of chunk by the distance that you specify
## autopct='%1.1f%%' is a inbuilt code to view the percentage amount of each chunk in the pie chart 
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0,0.1,0,0), autopct='%1.1f%%')


plt.title('pie_chart')
plt.legend()
plt.show()
