from bs4 import BeautifulSoup
import requests

# live NSE company shareprices listings website
site_url = 'https://live.mystocks.co.ke/m/pricelist'

shares_page = requests.get(site_url)
soup = BeautifulSoup(shares_page.content,'lxml')

# table of shares
table_of_shares = soup.find('table')
rows = table_of_shares.find_all('tr', class_ = 'row')

for row in rows:
    try:
        company_name = row.find('td', class_ = 'nm').text
        share_price = row.find('td', class_ = 'n').text

    except AttributeError:
        continue
    market_info = [company_name, share_price]
    print(market_info)
    
# for share in shares:
    
#     category = share.find('th', class_ = 'head')
#     company_name = share.find('td', class_ = 'nm')
#     print(category)

        


         

