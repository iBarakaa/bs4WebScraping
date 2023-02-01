from bs4 import BeautifulSoup
import requests

from_nse = requests.get('https://www.nse.co.ke/').text

soup = BeautifulSoup(from_nse,'lxml')
