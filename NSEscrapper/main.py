from bs4 import BeautifulSoup
import requests

from_marketlist = requests.get('https://live.mystocks.co.ke/m/pricelist')
soup = BeautifulSoup(from_marketlist.content,'lxml')

#   table of shares
shares = soup.find_all('tr', class_ = 'row')
print(shares)


for share in shares:
    inactive = share.find('tr', class_ = 'row r1 inact')

    if not inactive:
        category = share.find('th', class_ = 'head').text
        company_name = share.find('td', class_ = 'nm').text
        share_price = share.find('td', class_ = 'n').text

        


         

