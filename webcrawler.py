import requests
from bs4 import BeautifulSoup


def job_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://search.lockheedmartinjobs.com/ListJobs/ByState/TX/Country-US/Page-' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('td', {'class': 'coloriginaljobtitle'}):
            print('got one\n')
            href = link.get('href')
            print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('div', {'class': 'show-job-descr'}):
        print(item_name.string)


job_spider(1)
