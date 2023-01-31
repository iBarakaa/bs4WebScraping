#begin with first installing the requests library
import time
from bs4 import BeautifulSoup
import requests #this library requests info from a specific website

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

# we define this as a function, for all information that is related to scraping the job listings
def find_jobs():
    #retrieve information in the specified URL
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text) #should return 200 to mean successful request if .text not specified
    soup = BeautifulSoup(html_text, 'lxml')

    #in the website time jobs, this is the procedure to grab joblistings
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx' ) #results of only current page

    #for this looping structure, we aim to fetch all jobs and put them through a check
    #the filter is for few days ago
    for index, job in enumerate(jobs): #   allows us to iterate over the index of the job lists and content
        #we have to make sure that this only takes published dates of few days ago
        publishedDate = job.find('span', class_ = 'sim-posted').span.text #.span is to enter within the span of the span
        if 'few' in publishedDate:
            #we aim to replace our whitespaces with nothing
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            #from the more info section, we aim to procure the link only
            moreInfo = job.header.h2.a['href']

            #filters out to suit only job listings that are in accordance to your skills
            if unfamiliar_skill not in skills:
                #   .strip is used inside strings to get rid of undesired blank spaces
                #   posts dir is read now only because we used the relative path
                with open(f'webscraping\posts/{index}.txt', 'w') as f:
                    #   each job is written inside a file
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f'Required Skills: {skills.strip()} \n' )
                    f.write(f'More Info: {moreInfo}')
                print(f'File saved: {index}')


            #special functionalities
                #while loop
                #executing project every certain amount of time
                #filtration for job posts not meeting owned skills
                #throw results of posts to new blank file

if __name__ == '__main__':
    while True:
        find_jobs()
        #   the time_wait and its corresponding print message are meant to notify user how long they will wait for updates
        time_wait = 5
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60) #   wait certain amount of time it runs after
        

