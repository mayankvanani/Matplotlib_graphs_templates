import matplotlib.pyplot as plt



ages = [10,56,45,78,25,36,95,84,19,65,29,45,78,10,22,55,99,46,50,78,83,93,97,102,103,8,13,58,65,75,12,59,30,56,90,70,40,59,29,34,51,53,82,88]


## HISTOGRAM
## values of x for x in range ages
## uncomment the 
# ids = [x for x in range(len(ages))]
# plt.bar(ids, ages, label='id_ages')

## bins in histograms are like classes 
## values between 0 to 9 will be classifies under 1 bin, 10 to 19 will be classified under another bin... and at the end
## 110 to 120 will be classified under one bin
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

## plotting the histogram
## rwidth is relative width whereas width is absolute width
plt.hist(ages, bins=bins, histtype='bar', rwidth=0.8)





plt.xlabel('rand_x')
plt.ylabel('rand_y')
plt.title('barcharts and histograms')
plt.legend()
plt.show()
