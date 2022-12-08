# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:05:00 2019

@author: Axel
"""

#source of stock symbols traded at different exchanges
#http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs

url_nasdaq = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'
url_others = 'ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt'

import pandas
df1 = pandas.read_csv(url_nasdaq, sep ='|')
df2 = pandas.read_csv(url_others, sep = '|')

df1['Symbol'] = [symbol + '.O' for symbol in df1['Symbol']]
stocks = df1['Symbol'].tolist()
stocks.extend(df2['ACT Symbol'].tolist())

import requests
from bs4 import BeautifulSoup

news_list = list()
for x in stocks[0:5]:
	url = 'http://www.reuters.com/companies/' + x + '/key-developments'
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'lxml')

	#Google Chrome - Menu - Weitere Tools - Entwicklertools
	#Ctrl+Shift+C - Select section of interest
	#Right click html code and copy XPath: 
    
	try:
		for i in range(10):
			news = soup.body.find(id="__next").find_all('div', recursive=False)[0].find_all('div', recursive=False)[3].find_all('div', recursive=False)[0].find_all('div', recursive=False)[0].find_all('div', recursive=False)[0].find_all('section', recursive=False)[0].find_all('div', recursive=False)[0].find_all('div', recursive=False)[1].find_all('div', recursive=False)[i].find_all('div', recursive=False)[0] 
			message = news.find('h4').get_text()
			time = str.split(news.find('p').get_text())
			news_list.append([x,time[0],time[1],'2019',message])
	except:
		print('No findings.')

news_df = pandas.DataFrame(news_list, columns=['StockID','Month','Day','Year','News'])

#Goto Anaconda Prompt and start as administrator
#conda install -c anaconda pymysql 
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://hochstein:hochstein@bwa2.f4.htw-berlin.de:3306/reuters_v2?charset=utf8')
news_df.to_sql('reuters_news', engine, if_exists='append')