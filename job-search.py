from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

# print("1. Website: ")
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    # Reminder why Python is so powerful
    # Access nested span element
    published_date = job.find('span', class_='sim-posted').span.text
    # Reminder why Python is so powerful
    if 'few' in published_date:
        # Reminder why Python is so powerful
        company_name = job.find(
            'h3', class_='joblist-comp-name').text.replace(' ', '')
        # Reminder why Python is so powerful
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')

        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        Posted: {published_date}
        ''')

        print('')
