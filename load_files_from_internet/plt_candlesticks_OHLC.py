import matplotlib.pyplot as plt  
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import numpy as np 
import urllib




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

	
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))
	## Open High Low Close graph
	## we need to create a special list  for ohlc graphs. let the required lists be ohlc[]
	x = 0
	y = len(date)
	ohlc = []

	## to plot the full graph condition should be while x < y:
	## but since we are just takign a sample we did x < 31 (approx. 1 month)
	while x < 31:
		append_me = date[x], openp[x], highp[x], lowp[x], closep[x], adjusted[x], volume[x]
		ohlc.append(append_me)
		x+=1 

	## plotting teh candlesticks
	candlestick_ohlc(ax1, ohlc, width=0.5, colorup='g', colordown='r')

	## date formatting and setting it to 45degree
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	ax1.grid(True)

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
