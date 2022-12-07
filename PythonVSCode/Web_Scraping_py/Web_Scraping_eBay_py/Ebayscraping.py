import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'EbayDamenBekleidungAvg'

def get_data(searchterm):
    for pages in range(1,10):
        url = 'https://www.ebay.de/b/Kleider/63861/bn_1619088?_pgn=' + str(pages)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        product = {
            #'title': item.find('h3', {'class': 's-item__title'}).text,
            'soldprice': item.find('span', {'class': 's-item__price'}).text.replace('EUR','').strip(),
            #'avgprice' : sum(productslist) / len(productslist)
        }
        productslist.append(product)
    return productslist

def output(productslist, searchterm):
    productsdf =  pd.DataFrame(productslist)
    productsdf.to_csv(searchterm + 'output.csv', index=False)
    print('Saved CSV')
    return

soup = get_data(searchterm)
productslist = parse(soup)
output(productslist, searchterm)

