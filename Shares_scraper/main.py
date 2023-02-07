from bs4 import BeautifulSoup
from csv import writer
import requests
import time
import schedule

# the main workflow is defined into a python function
def find_shares():
    # live NSE companies shareprices listings from mystocks website
    site_url = 'https://live.mystocks.co.ke/m/pricelist'

    shares_page = requests.get(site_url)
    # if we are to print(soup), the result is all the html code for the webpage
    soup = BeautifulSoup(shares_page.content,'lxml')

    # this is where we begin scraping specific content
    # table of shares search using the table element
    table_of_shares = soup.find('table')

    # identifying all the rows within the table
    rows = table_of_shares.find_all('tr', class_ = 'row')

    # creating csv file that stores shares details in the shareSheet folder, where 'writer' writes the data scraped into the csv
    with open('Shares_scraper\shareSheet/shareprices.csv', 'w', encoding = 'utf8', newline = '' ) as sharesSheet:
        infoWriter = writer(sharesSheet)

        # creation of header that classifies the columns
        header = ['Company Name', 'Share Price']
        infoWriter.writerow(header)
        for row in rows:
            # scraping and refining the row data of names and prices 
            # the reason for placement into the try-except block is so as to filter out rows that have NONE values
            try:
                company_name = row.find('td', class_ = 'nm').text.replace('\n','')
                share_price = row.find('td', class_ = 'n').text
            except AttributeError:
                continue

            # storing of procured data into an array
            market_info = [company_name, "KES."+share_price]
            # writes array into the csv
            infoWriter.writerow(market_info)

# scheduling execution every Friday @ 12noon
# schedule.every().friday.at("12:00").do(find_shares)

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# the code below will run every 7 days, however, we have opted to use the schedule package for more concise execution as seen above
# if __name__ == '__main__':
#     while True:
#         find_shares()
#         # the spreadsheet will refresh weekly 
#         inactive_days = 7
#         print(f"Waiting {inactive_days} days ...")
#         time.sleep((inactive_days * 24) * 3600)


# scheduling every 15 minutes 
if __name__ == '__main__':
    while True:
        find_shares()
        # refreshing after every 15 minutes
        sleep_minutes = 15
        print(f"Waiting {sleep_minutes} minutes ...")
        time.sleep(sleep_minutes * 60)


    


        


         

