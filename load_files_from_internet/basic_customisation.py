import matplotlib.pyplot as plt  
import numpy as np 
import urllib
import matplotlib.dates as mdates



def graph_data(stock):

	stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement' 
	source_code = urllib.request.urlopen(stock_price_url).read().decode()
	stock_data = []
	split_source = source_code.split('\n')
	for line in split_source:
		split_line = line.split(',')
		if 'Date' not in line:
			stock_data.append(line)


	date, openp, highp, lowp, closep, adjusted ,volume  = np.loadtxt(stock_data, delimiter=',', unpack=True,
																converters={0: bytespdate2num('%Y-%m-%d')})

	#---------------- ---------------- CUSTOMIZING GRAPH -------------------------
	## to create figure object, define the figure
	## important to use figure in order to customise the plot
	fig = plt.figure()
	## define ax1; for more plots define more like ax2, ax3 and so on...
	## plt.subplot2grid(grid_shape((rows,colums), (axis_location(rows, cols)), rowspan, colspan, fig)
	##      default original          (1,1)     ,                   (0,0)
	ax1 = plt.subplot2grid((1,1),(0,0))
	## to rotate the label on x axis
	for label in ax1.xaxis.get_ticklabels():
		## setting the tilting angle of the x_labels
		## after tilting, configure the subplot and adjust the parameters to make the tilted labels clearly visible on the screen
		## and the code for that adjusted arguments in plt.subplot_adjust
		label.set_rotation(45)



	ax1.plot_date(date, openp, '-', label='price')
	## showing the grid
	## ax1.grid(True, color, '-/./*')
	ax1.grid(True, linestyle='--', color='g')
	plt.xlabel('dates')
	plt.ylabel('price')
	plt.title('loaded from internet')
	plt.legend()
	##       enter all the parameters that are visible on the configure-subplot option. 
	plt.subplots_adjust(left=0.12, bottom=0.21, right=0.90, top=0.88, wspace=0.20, hspace=0.20)
	plt.show()


def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s=b.decode(encoding)
		return strconverter(s)
	return bytesconverter  

graph_data('TSLA')
