# stocks web scraper

import bs4
from bs4 import BeautifulSoup
import requests

"""
url = requests.get('https://www.fool.com/investing/top-stocks-to-buy/')
soup =bs4.BeautifulSoup(url.content, 'html.parser')
stocks = soup.find(class_='related-tickers')
stock_picks = stocks.find_all(class_='ticker-text-wrap')
# get stock names
stock_names = []
for stock in stock_picks:
    stock_names.append(stock.h3.get_text())
    print(stock_names)
"""
# todo add email bot

# todo add date and time when scraped


url = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup =bs4.BeautifulSoup(url.content, 'html.parser')
# print(soup.prettify())

stock_name = soup.find('h1', {'class':'D(ib) Fz(18px)'}).text
print(stock_name)

stock_price = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print("Stock Price is: $" + stock_price)
