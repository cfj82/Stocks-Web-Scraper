# stocks web scraper

from bs4 import BeautifulSoup
from datetime import datetime
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

def scrape_stock():
    search_stock = input("What is the stock ticker you would like to search?\n").upper()  # must convert to uppercase
    # yahoo finance with {} for ticker symbol
    # url = 'https://finance.yahoo.com/quote/FB?p=FB&ncid=stockrec'
    url = 'https://finance.yahoo.com/quote/' + search_stock + '?p=' + search_stock + '&ncid=stockrec'

    url_request = requests.get(url)
    print(url_request)

    if url_request == '404':
        print("Failed request")
    else:
        soup = BeautifulSoup(url_request.text, 'html.parser')
        # print(soup.prettify())
        stock_name = soup.find('h1', {'class':'D(ib) Fz(18px)'}).text
        #  print(stock_name)
        stock_price = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        t = datetime.now()
        time_scraped = t.strftime("%d/%m/%Y %H:%M")
        print(stock_name + "'s Price is: $" + stock_price + " at " + time_scraped)


scrape_stock()
