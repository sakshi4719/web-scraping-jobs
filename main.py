from bs4 import BeautifulSoup
import requests
import time

known_skill = input("enter skill: ")

def job_finder():
    html_text = requests.get('https://www.timesjobs.com/jobs-in-mumbai/current-jobs').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix joblistli')

    for job in jobs:
        location = job.find('li', class_='srp-zindex location-tru').text.strip().replace(' ', '')
        skills = job.find('li', class_='key-skills__').text.strip().replace(' ', '')

        if 'Mumbai' in location and known_skill in skills:
            with open()
            comp_name = job.find('h3', class_='joblist-comp-name').text.strip()
            a_tag = soup.find('a', class_='posoverlay_srp')
            relative_link = a_tag['href']
            full_link = "https://www.timesjobs.com" + relative_link
            print(f"Skills: {skills}")
            print(f"Company Name: {comp_name}")
            print(f"Location: {location}")
            print('  ')
            print(full_link)

if __name__ == '__main__':
    while True:
        job_finder()
        time_wait = 1
        print(f'waiting for {time_wait} minutes')

        time.sleep(time_wait*60)
