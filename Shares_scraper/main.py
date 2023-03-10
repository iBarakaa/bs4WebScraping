from bs4 import BeautifulSoup
from csv import writer
import requests
import time
import schedule
import datetime

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
        header = ['Company Name', 'Share Price','Sector', 'Date']
        infoWriter.writerow(header)
        for row in rows:
            # scraping and refining the row data of names and prices 
            # the reason for placement into the try-except block is so as to filter out rows that have NONE values
            try:
                company_name = row.find('td', class_ = 'nm').text.replace('\n','')
                # Companies within the stock market stored within arrays in their respective sectors
                agricultural_companies = [
                    'EGAD', 
                    'KUKZ', 
                    'KAPC', 
                    'LMT', 
                    'SASN', 
                    'WTK'
                    ]

                automobile_companies = ['CGEN']

                banking_companies = [
                    'ABSA',
                    'BKG',
                    'COOP',
                    'DTK',
                    'EQTY',
                    'HFCK',
                    'IMH',
                    'KCB',
                    'NBK',
                    'NCBA',
                    'SBIC',
                    'SCBK'
                ]

                commercial_companies = [
                    'DCON',
                    'EVRD',
                    'XPRS',
                    'HBE',
                    'KQ',
                    'LKL',
                    'NBV',
                    'NMG',
                    'SMER',
                    'SGL',
                    'TPSE',
                    'UCHM',
                    'SCAN'
                ]

                construction_companies = [
                    'ARM',
                    'BAMB',
                    'CRWN',
                    'CABL',
                    'PORT'
                ]

                energy_companies = [
                    'KEGN',
                    'KPLC-P4',
                    'KPLC-P7',
                    'KPLC',
                    'TOTL',
                    'UMME'
                ]

                insurance_companies = [
                    'BRIT',
                    'CIC',
                    'JUB',
                    'KNRE',
                    'LBTY',
                    'SLAM'
                ]

                investment_companies = [
                    'CTUM',
                    'HAFR',
                    'KURV',
                    'OCH',
                    'TCL'
                ]

                investmentservices_companies = ['NSE']

                manufacturing_companies = [
                    'BOC',
                    'BAT',
                    'CARB',
                    'EABL',
                    'FTGH',
                    'ORCH',
                    'MSC',
                    'UNGA'
                ]

                telecommunication_companies = ['SCOM']

                realestate_companies = ['FAHR']

                etf_companies = ['GLD']


                # assignment of companies into sectors within the csv
                if company_name in agricultural_companies:
                    sector = 'Agricultural'

                if company_name in automobile_companies:
                    sector = 'Automobiles'

                if company_name in banking_companies:
                    sector = 'Banking'

                if company_name in commercial_companies:
                    sector = 'Commercial'

                if company_name in construction_companies:
                    sector = 'Construction'

                if company_name in energy_companies:
                    sector = 'Energy'

                if company_name in insurance_companies:
                    sector = 'Insurance'

                if company_name in investment_companies:
                    sector = 'Investments'

                if company_name in investmentservices_companies:
                    sector = 'InvestmentServices'

                if company_name in manufacturing_companies:
                    sector = 'Manufacturing'

                if company_name in telecommunication_companies:
                    sector = 'Telecommunication'

                if company_name in realestate_companies:
                    sector = 'Investment'

                if company_name in etf_companies:
                    sector = 'ExchangeTradedFunds'
                    
                share_price = row.find('td', class_ = 'n').text
                scraped_date = datetime.date.today()
            except AttributeError:
                continue

            # storing of procured data into an array
            market_info = [company_name, "KES."+share_price, sector, scraped_date]
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


# scheduling every 5 seconds
if __name__ == '__main__':
    while True:
        find_shares()
        # refreshing after every 15 minutes
        sleep = 5
        print(f"Waiting {sleep} seconds ...")
        time.sleep(sleep)


    


        


         

