#begin with first installing the requests library
from bs4 import BeautifulSoup
import requests #this library requests info from a specific website

#retrieve information in the specified URL
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text) #should return 200 to mean successful request if .text not specified
soup = BeautifulSoup(html_text, 'lxml')

#in the website time jobs, this is the procedure to grab joblistings
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx' ) #results of only current page

#for this looping structure, we aim to fetch all jobs and put them through a check
#the filter is for few days ago
for job in jobs:
    #we have to make sure that this only takes published dates of few days ago
    publishedDate = job.find('span', class_ = 'sim-posted').span.text #.span is to enter within the span of the span
    if 'few' in publishedDate:
        #we aim to replace our whitespaces with nothing
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        #from the more info section, we aim to procure the link only
        moreInfo = job.header.h2.a['href']

        #.strip is used inside strings to get rid of undesired blank spaces
        print(f"Company Name: {company_name.strip()}")
        print(f'Required Skills: {skills.strip()}')
        print(f'More Info: {moreInfo}')
        print('')

        #special functionalities
            #while loop
            #executing project every certain amount of time
            #filtration for job posts not meeting owned skills
            #throw results of posts to new blank file


