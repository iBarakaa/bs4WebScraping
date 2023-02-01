from bs4 import BeautifulSoup
import requests

# live NSE company shareprices listings website
site_url = 'https://live.mystocks.co.ke/m/pricelist'

shares_page = requests.get(site_url)
soup = BeautifulSoup(shares_page.content,'lxml')

# table of shares
shares = soup.find_all('tr', class_ = 'row')
print(shares)


for share in shares:
    inactive = share.find('tr', class_ = 'row r1 inact')

    if not inactive:
        category = share.find('th', class_ = 'head').text
        company_name = share.find('td', class_ = 'nm').text
        share_price = share.find('td', class_ = 'n').text

        


         

