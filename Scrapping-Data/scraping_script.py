import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = soup.find_all('a', class_='flex items-center hover:underline')

    data = []

    for job in jobs:
        title = job.find('span').text.strip()
        job_url = "https://www.je-change-de-metier.com" + job['href']

        job_data = {
            'title': title,
            'job_url': job_url
        }
        data.append(job_data)

    return data

def write_to_csv(data, filename='jobs_data.csv'):
    fields = ['title', 'job_url']

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

base_url = "https://www.je-change-de-metier.com/les-metiers-de-a-a-z"
data = scrape_page(base_url)

write_to_csv(data)
