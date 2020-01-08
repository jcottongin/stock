#!/usr/bin/python3
#getting different data places in the lists obtained

from lxml import html

import requests
#import sys   #ascii code fix
#reload(sys)

#sys.setdefaultencoding('utf-8') #ascii code fix
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
##get pricey Average:  48.715
price = tree.xpath('//bg-quote[@class="value"]/text()')  #create tree of name lists

##get lists of different prices
openp = tree.xpath('//span[@class="kv__value kv__primary "]/text()')
openpr = [openp.text_content() for openp in tree.xpath('//span[@class="kv__value kv__primary "]')]
#print openpr
print ('AMD Current Stock Prices')
##get description of different prices
opendes = tree.xpath('//small[@class="kv__label"]/text()')
##index = openpr.index('$27.81') #search for list position 

# get low prices 
daylo = tree.xpath('//span[@class="text low"]/text()')
daylos = [daylo.text_content() for daylo in tree.xpath('//span[@class="text low"]')]
print ('Day Low: ',daylos[0]) 
print ('52 Week Low: ', daylos[1])

#get high prices 
dayhi = tree.xpath('//span[@class="text high"]/text()')
#dayhis = [dayhis.text_content() for dayhi in tree.xpath('//span[@class="text high]')]
print ('Day High: ', dayhi[0])
print ('52 Week High:', dayhi[1])




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

print ('Current Price: ', currentprice)
print ('Open Price: ',intprice)

def compareprice():

	if (currentprice < intprice) :
		print ('Current Price is ', (currentprice- intprice),'less than open price' )
	else:
		print ('Current Price is ', (currentprice-intprice), 'more than open price')
	return
compareprice()

def dayAvg(dayhigh,daylow):
	avg = float(dayhigh + daylow)/2
	

	print ('Day Average: ',avg)
	return avg
avg=dayAvg(dayhigh,daylow)



#zip diff prices and description
stock = {}
for na, pr in zip(opendes, openpr):   #na is name or first column pr is price or 2nd column
	stock[na] = pr

#print stock
#zip lists
import csv
with open('amd.csv', 'a') as f:  #open amd.csv and export financial summary data
	for na, pr in stock.items():
		f.write("%s,*%s\n"%(na, pr))

import csv
with open('amdprice.csv', 'a') as f:  #open amdprice.csv and write name and price
	f.write("Current Price: %s * Open Price: %s * Day High:  %s, * Day Low: %s * Day Average: %s * %s\n'"%(currentprice, intprice, dayhi[0] , daylos[0], avg, times))
	#f.write('Day High:  %s, * Day Low: %s * Day Average: %s\n' %(dayhi[0] , daylos[0], avg))
##prints same as amdprice except without the strings
#with open('price.csv', 'a') as f:  #open price.csv and write name and price
#	f.write("%s *  %s *  %s, *  %s *  %s * %s\n'"%(currentprice, intprice, dayhi[0] , daylos[0], avg, times))

from pandas import DataFrame, read_csv  #read csv file
import matplotlib.pyplot as plt 
import pandas as pd ##load panda with pd as the alias
import numpy as np #use np as numpy

file = r'output.csv'
df = pd.read_csv(file, sep='*', error_bad_lines=False)
df = pd.DataFrame(read_csv(file, sep='*', error_bad_lines=False))


#print(df)   ##print file
df.columns = ['current', 'open', 'high' , 'low' , 'avg', 'date']  #name columns to call 
#print(df['current'].head())
def low_high():
    #print('Low: ',df['low'][0], 'date', df['date'][0])  ##print 'column' and 'row'
    low = df['low'][0]  #define current from the column and row position to get just the price
    #print(current.split("Current Price:")) #split off the Current Price
    ##print(low) #print whats in df['low'][0]
    low_price = low[10:15]  #print only the price in df['low'][0]
    print(low_price)
    #print('date: ',df['date'][0])
    #print('high: ' ,df['high'][0], df['date'][0])
    high = df['high'][0]
    #print(len(high)) # get length of df['high'][0]
    high_price = (high[12:17])
    print(high_price)
    return
#low_high()
def rewrite():
    import csv
    text=open("amdprice.csv", "r")
    text= ''.join([i for i in text])\
        .replace("Day Average: ", "")
    x=open("output.csv", "w")
    x.writelines(text)
    x.close()
rewrite()
def average():
    avg = df['avg'][0:]
    ##avg2=df['avg'].str.strip('Day Average: ') #strip day average
    #print(avg2)
    ##df2=pd.DataFrame(avg2)
    ##df2['avg']=pd.to_numeric(df['avg'], errors='coerce')
    #print(avg)
    print("AMD price monthly avg",avg.mean())
    
    
average()
