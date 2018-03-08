import matplotlib.pyplot as plt  
import numpy as np 
import urllib
import matplotlib.dates as mdates



def graph_data(stock):

	## enter the url from where to fetch the data
	## url must contain data in csv format

	stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement' 
	source_code = urllib.request.urlopen(stock_price_url).read().decode()

	## empty list for appending data to it
	stock_data = []


	## split the data by new line i.e. each line has data related to single quantity
	split_source = source_code.split('\n')

	## in the url, we have 6 elements separated by comma
	## but, the first row has 6 strings also separated by comma which we dont want
	for line in split_source:
		## .split('arg'), here the arg can be ',' or ':'or '/' etc depending upon how the entities are separated 
		split_line = line.split(',')
		## first line contains string 'Date'
		if 'Date' not in line:
			stock_data.append(line)


	## openp = openprice, closep = closeprice ...
	## storing the read values to python
	## converters = {column to converter, type of conversion}
	## %Y = full year - 2018
	## %y = partial year - 18
	## %m = month
	## %d = day
	## %H = hours
	## #M = minutes
	## %S = seconds

	## here the 0 column contains date stamp in wierd format so we need to convert it to readble format
	## 2017-07-26 = %Y-%m-%d
	## bypespdate2num is function defined below 
	date, openp, highp, lowp, closep, adjusted ,volume  = np.loadtxt(stock_data, delimiter=',', unpack=True,
																converters={0: bytespdate2num('%Y-%m-%d')})


	## plotting the acquired data
	plt.plot_date(date, openp, '-', label='price')
	plt.xlabel('dates')
	plt.ylabel('price')
	plt.title('loaded from internet')
	plt.legend()
	plt.show()

## decoding the date
## fmt is the format of the date that is there in csv file
def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s=b.decode(encoding)
		return strconverter(s)
	return bytesconverter  

## plotting graph for tesla stock
graph_data('TSLA')
