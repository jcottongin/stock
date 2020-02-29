#!/usr/bin/python3
#getting different data places in the lists obtained
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#open firefox browser
options=Options()
options.headless = False
driver=webdriver.Firefox(options=options)


#browser get website
url = ("https://finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch") #website
driver.get(url) #put website inside of firefox
   
#afterhours = driver.find_element_by_css_selector("""span.C\(\$primaryColor\)""").text
#print('After Hours: ,'+afterhours)


openpr = driver.find_element_by_css_selector("""div.W\(1\/2\):nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1)""").text  #get open price

print('open price: ' ,openpr) #from open tree get open price
#index = open.index('48.78') #search for list position 
#get day range
dayrange = driver.find_element_by_css_selector("""div.W\(1\/2\):nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)""").text
##create list of prices in dayrange path
#dayranges= [dayrange.text_content() for dayrange in tree.xpath('//td[@class="Ta(end) Fw(600) Lh(14px)"]')] 
print('Day range ',dayrange)
##index = dayrange.index('46.79 - 48.57') #search for list position 

#print(type(openpr)) #get type of openpr
#get currentprice
currentPrice = driver.find_element_by_css_selector(""".Fz\(36px\)""").text
print ('Current Price: ',currentPrice)
#get change
change = driver.find_element_by_css_selector("""span.Trsdu\(0\.3s\):nth-child(2)""").text
print('Price Change: ',change)

##get date and time
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
#print("date and time =", dt_string)	

import csv
with open('test.csv', "a+", newline='') as f:
    f.write("Open price: ,"+openpr + ", Current Price: ,"+currentPrice+ ', Price Change: ,'+change+ ',Day Range: ,'+dayrange+ ',Date: '+dt_string+'\n')
#
#from pandas import DataFrame, read_csv
#import matplotlib.pyplot as plt 
#import pandas as pd ##load panda with pd as the alias
#
#file = r'test.csv'
#df = pd.read_csv(file, sep=',', error_bad_lines=False)
#
#
#print(df)   ##print file
#df.columns = ['open', 'price' ,'current' , 'price' ,'low' , 'avg', 'date']  #name columns to call 
##print(df['current'].head())
#print('current:',df['current'][0], 'date', df['date'][0])  ##print 'column' and 'row'
##print('date: ',df['date'][0])

def soffice():    
    import subprocess
    subprocess.call(['/usr/bin/soffice', '/root/python/stock/panda/test.csv'])  ##open output with soffice
    return
soffice()
