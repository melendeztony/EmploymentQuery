import requests
import re
from bs4 import BeautifulSoup


def job_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://search.lockheedmartinjobs.com/ListJobs/ByState/TX/Country-US/Page-' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', href=re.compile(r'.*Engineer*.')):
            href = 'https://search.lockheedmartinjobs.com' + link.get('href')
            title = link.string
            if ('Engineer' and 'Software') in title:
                print(title + ': ' + href)
                get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('div', {'class': 'jobdescription-value'}):
        print(item_name.get_text())

job_spider(2)
