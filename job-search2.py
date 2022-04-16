from bs4 import BeautifulSoup
import requests
import time

print('Put some skill you are not familiar with: ')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    # print("1. Website: ")
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        # Reminder why Python is so powerful
        # Access nested span element
        published_date = job.find('span', class_='sim-posted').span.text
        # Reminder why Python is so powerful
        if 'few' in published_date:
            # Reminder why Python is so powerful
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')
            # Reminder why Python is so powerful
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:

                with open(f'posts/{index}.txt', 'w') as f:
                    # Reminder .strip() why python is so powerful
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f'More Info: {more_info} \n')
                    # Reminder .strip() why python is so powerful

                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
