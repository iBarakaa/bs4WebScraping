# beautifulsoup4 library installation
# method specifier to parse html code 
# hence we install lxml parser library

# importing beautiful soup
from bs4 import BeautifulSoup

#accessing content inside home.html file
#second entry either decides whether we read, write or both
with open('home.html', 'r') as html_file: 
    content = html_file.read()

    #using beautiful soup to prettify html and work with its tags like python objects
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify()) #outputs read file
    
    #displaying all the courses?
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)

    #grabbing specific information
    #.find searches for specified tags
    #tags = soup.find('h5') #searches for the first element and stops execution
    #tags = soup.find_all('h5')
    #print(tags)

    #with real websites, we have to use inspect of browsers

    # grabbing courses and prices
    course_cards = soup.find_all('div', class_='card') #Storage of all course cards
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] #split helps us procure a specific section of string, ini this case we took the last section

        #printing output with f-string
        print(f'{course_name} costs {course_price}')

#   In finding list of tags we can use "find_all(['','','', ... ])"
#   for all tags, we use find_all(true)
#   findall looks through descendants and retrieves
#   to find a limit of args, we use: find_all("p", limit = '3')
#   find_all will always return a list
