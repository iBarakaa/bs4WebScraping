#begin with first installing the requests library
from bs4 import BeautifulSoup
import requests #this library requests info from a specific website

#retrieve information in the specified URL
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text) #should return 200 to mean successful request if .text not specified
soup = BeautifulSoup(html_text, 'lxml')

#in the website time jobs, this is the procedure to grab joblistings
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx' ) #results of only current page

#we aim to replace our whitespaces with nothing
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
skills = job.find('span', class_='srp-skills').text.replace(' ','')

print(f'''
Company Name: {company_name}
Required Skills: {skills}
''')