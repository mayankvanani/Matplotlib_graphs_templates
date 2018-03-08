import matplotlib.pyplot as plt

x1 = [2,4,6,8,10]
y1 = [1,5,3,5,10]

x2 = [1,3,5,7,9]
y2 = [10,20,40,20,30]

ages = [10,56,45,78,25,36,95,84,19,65,29,45,78,10,22,55,99,46,50,78,83,93,97,102,103,8,13,58,65,75,12,59,30,56,90,70,40,59,29,34,51,53,82,88]

## BARGRAPH
## thickness of the bar and ehight can be controlled -- look into the documentation 
## even though if not mentioned color, bargraphs will be differntly colored automatically
plt.bar(x1, y1, label='bar_chart_1', color='blue')
plt.bar(x2, y2, label='bar_chart_2', color='red')

## HISTOGRAM
## values of x for x in range ages
ids = [x for x in range(len(ages))]
plt.bar(ids, ages, label='id_ages')





plt.xlabel('rand_x')
plt.ylabel('rand_y')
plt.title('barcharts and histograms')
plt.legend()
plt.show()
