# stocks web scraper

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

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
        result = stock_name + "\'s Price is: $" + stock_price + " at " + time_scraped
        print(result)
        # call email function
        email_bot(stock_name, result)


def email_bot(stock_name, result):
    from_address = 'cfowlerNoReply@gmail.com'
    from_pw = 'JhgJhg>.'
    to_address = 'colinjunfowler@gmail.com'
    mail_content = """result"""

    # set up MMIME
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = "{stock_name} + 'Stock Price'"
    # body and attachments for the email
    message.attach(MIMEText(mail_content, 'plain'))

    try:
        # create SMTP session for sending email
        server = smtplib.SMTP('64.233.184.108')  # IP address of smtp.gmail.com to bypass DNS resolution
        server.starttls()  # enables security
        server.login(from_address, from_pw)
        text = message.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email Sent Successfully!")
    except Exception as ex:
        print("Something went wrong" + str(ex))

'''    try:
        # send email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # stating from gmail and port 465
        server.login(sender_address, pw)
        server.sendmail(sender_address, email_recepients, mail_message)  # (email from, email to, email message)
        server.close()
        print("Email Sent Successfully!")
    except Exception as ex:
        print("Something went wrong" + str(ex))'''

# run
scrape_stock()
