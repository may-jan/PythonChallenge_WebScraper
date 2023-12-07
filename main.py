from bs4 import BeautifulSoup
from requests import get
from extractors.wwr import extract_wwr_jobs

# search_keyword = input('Enter the search keyword : ')
jobs = extract_wwr_jobs('python')
print(jobs)

from selenium import webdriver
broswer = webdriver.Chrome()
broswer.get('https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=89395b6ac5014113')

soup = BeautifulSoup(broswer.page_source, 'html.parser')
job_list = soup.find('ul', class_="css-zu9cdh eu4oa1w0")
jobs = job_list.find_all('li', recursive=False)
results = []
for job in jobs :
    zone = job.find('div', class_="mosaic-zone")
    if zone == None :
        h2 = job.find('h2', class_='jobTitle')
        anchor = job.select_one('h2 a')
        link = anchor['href']
        title = anchor.find('span')
        company = job.find('span', attrs={'data-testid':'company-name'})
        location = job.find('div', attrs={'data-testid':'text-location'})
        job_data = {
            'link' : f"https://kr.indeed.com{link}",
            'company' : company.string,
            'location' : location.string,
            'position' : title.string
        }
        results.append(job_data)
for result in results:
    print(result, '\n\n')

while (True):
   pass