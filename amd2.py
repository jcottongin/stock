#!/usr/bin/env python  
#getting different data places in the lists obtained

from lxml import html

import requests
import sys   #ascii code fix
reload(sys)
sys.setdefaultencoding('utf-8') #ascii code fix
page = requests.get('https://www.marketwatch.com/investing/stock/amd')
tree = html.fromstring(page.content)

#print pages.text

#get get time
time = tree.xpath('//span[@class="timestamp__time"]')  #create tree of time

times = [time.text_content() for time in tree.xpath('//span[@class="timestamp__time"]')] #get time inside of tree
#get names 

name = tree.xpath('//h1[@class="company__name"]/text()')  #create tree of name lists

#search for names column makes a list

names = [name.text_content() for name in tree.xpath('//div/h1[@class="company__name"]')]
##get price
price = tree.xpath('//bg-quote[@class="value"]/text()')  #create tree of name lists

##get lists of different prices
openp = tree.xpath('//span[@class="kv__value kv__primary "]/text()')
openpr = [openp.text_content() for openp in tree.xpath('//span[@class="kv__value kv__primary "]')]
#print openpr
print 'AMD Current Stock Prices'
##get description of different prices
opendes = tree.xpath('//small[@class="kv__label"]/text()')
##index = openpr.index('$27.81') #search for list position 

# get low prices 
daylo = tree.xpath('//span[@class="text low"]/text()')
daylos = [daylo.text_content() for daylo in tree.xpath('//span[@class="text low"]')]
print 'Day Low: ',daylos[0] 
print '52 Week Low: ', daylos[1]

#get high prices 
dayhi = tree.xpath('//span[@class="text high"]/text()')
#dayhis = [dayhis.text_content() for dayhi in tree.xpath('//span[@class="text high]')]
print 'Day High: ', dayhi[0]
print '52 Week High:', dayhi[1]




##compare price
from decimal import Decimal
openprice = openpr[0]
intprice = Decimal(openprice.strip('$')) ##turn open price from zip list to decimal
currentprice = price[0]  ##put currentprice list in startprice
currentprice = Decimal(price[0]) ##convert currentprice to decimal

daylo = daylos[0]
daylow = Decimal(daylos[0])
dayhig = dayhi[0]
dayhigh = Decimal(dayhi[0])

print 'Current Price: ', currentprice
print 'Open Price: ',intprice

def compareprice():

	if (currentprice < intprice) :
		print 'Current Price is ', (currentprice- intprice),'less than open price' 
	else:
		print 'Current Price is ', (currentprice-intprice), 'more than open price'
	return
compareprice()

def dayAvg(dayhigh,daylow):
	avg = float(dayhigh + daylow)/2
	

	print 'Day Average: ',avg
	return avg
avg=dayAvg(dayhigh,daylow)



#zip diff prices and description
stock = {}
for na, pr in zip(opendes, openpr):   #na is name or first column pr is price or 2nd column
	stock[na] = pr

#print stock
#zip lists
import csv
with open('amd.csv', 'a') as f:  #open stock.csv and write name and price
	for na, pr in stock.items():
		f.write("%s,*%s\n"%(na, pr))

import csv
with open('amdprice.csv', 'a') as f:  #open stock.csv and write name and price
	f.write("Current Price: %s * Open Price: %s * Day High:  %s, * Day Low: %s * Day Average: %s * %s\n'"%(currentprice, intprice, dayhi[0] , daylos[0], avg, times))
	#f.write('Day High:  %s, * Day Low: %s * Day Average: %s\n' %(dayhi[0] , daylos[0], avg))