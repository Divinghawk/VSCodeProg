from bs4 import BeautifulSoup
import requests
import numpy as np


# Create a for loop for the amount of pages you wish to query
for page in range(1, 11):
    # Dynamically pass the page number to the URL
    page = requests.get('https://www.ebay.de/b/Kleider/63861/bn_1619088?_pgn=' + str(page))
    
    # Initialize BeautifulSoup and find all spans with specified class
    soup = BeautifulSoup(page.text, 'html.parser')
    prices = soup.find_all('span', class_='s-item__price')
    p = page.text.strip(' bis EUR ')
    ps = p.replace(',','.')


    # Print the prices from each span element
    
def price(fprice):
    avg_price = []
    avg_price.append(fprice)
        
    average_price = sum(avg_price) / len(avg_price)
    print(str(round(average_price, 2)))
        
print(price)      
