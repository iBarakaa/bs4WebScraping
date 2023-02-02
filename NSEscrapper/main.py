from bs4 import BeautifulSoup
from csv import writer
import requests

# live NSE company shareprices listings website
site_url = 'https://live.mystocks.co.ke/m/pricelist'

shares_page = requests.get(site_url)
soup = BeautifulSoup(shares_page.content,'lxml')

# table of shares
table_of_shares = soup.find('table')
rows = table_of_shares.find_all('tr', class_ = 'row')


# creating csv file that stores shares details
with open('shareprices.csv', 'w', encoding = 'utf8', newline = '' ) as sharesSheet:
    infoWriter = writer(sharesSheet)    # writing onto csv
    for row in rows:
        try:
            company_name = row.find('td', class_ = 'nm').text.replace('\n','')
            share_price = row.find('td', class_ = 'n').text
            percentage_change = row.find('td')
            percentage_change = percentage_change['class'][1]

        except AttributeError:
            continue
        market_info = [company_name, share_price]
        print(market_info)


    


        


         

