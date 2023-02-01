from bs4 import BeautifulSoup
import requests

from_nse = requests.get('https://www.nse.co.ke/', verify = False).text

soup = BeautifulSoup(from_nse,'lxml')
