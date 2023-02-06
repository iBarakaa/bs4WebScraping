from bs4 import BeautifulSoup
from csv import writer
import requests
import time
import schedule

def find_shares():
    # live NSE companies shareprices listings from mystocks website
    site_url = 'https://live.mystocks.co.ke/m/pricelist'

    shares_page = requests.get(site_url)
    soup = BeautifulSoup(shares_page.content,'lxml')

    # table of shares
    table_of_shares = soup.find('table')
    rows = table_of_shares.find_all('tr', class_ = 'row')

    # creating csv file that stores shares details
    with open('NSEscrapper\shareSheet/shareprices.csv', 'w', encoding = 'utf8', newline = '' ) as sharesSheet:
        infoWriter = writer(sharesSheet)    # writing onto csv
        header = ['Company Name', 'Share Price']
        infoWriter.writerow(header)
        for row in rows:
            try:
                company_name = row.find('td', class_ = 'nm').text.replace('\n','')
                share_price = row.find('td', class_ = 'n').text
            except AttributeError:
                continue
            market_info = [company_name, share_price]
            # writes looped rows into the csv
            infoWriter.writerow(market_info)

# scheduling execution every Friday @ 12noon
schedule.every().friday.at("12:00").do(find_shares)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)


# the code below will run every 7 days, however, we have opted to use the schedule package for more concise execution as seen above
# if __name__ == '__main__':
#     while True:
#         find_shares()
#         # the spreadsheet will refresh weekly 
#         inactive_days = 7
#         print(f"Waiting {inactive_days} days ...")
#         time.sleep((inactive_days * 24) * 3600)


    


        


         

