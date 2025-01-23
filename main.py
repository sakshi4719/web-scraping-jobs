from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/jobs-in-mumbai/current-jobs').text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix joblistli')
for job in jobs:
    location = job.find('li', class_='srp-zindex location-tru').text.strip().replace(' ', '')
    skills = job.find('li', class_='key-skills__').text.strip().replace(' ', '')

    if 'Mumbai' in location and 'Python' in skills:
        comp_name = job.find('h3', class_='joblist-comp-name').text.strip()

        print(f"Skills: {skills}")
        print(f"Company Name: {comp_name}")
        print(f"Location: {location}")
        print('  ')