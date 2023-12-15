from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
broswer = webdriver.Chrome(options=options)

def get_page_count(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    broswer.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(broswer.page_source, 'html.parser')
    pagination = soup.find('nav', attrs={'aria-label':'pagination'})
    pages = pagination.select('li')
    count = len(pages)
    if(count == 0):
        return 1
    else:
        return count-1

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        base_url = 'https://kr.indeed.com/jobs'
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        broswer.get(final_url)

        soup = BeautifulSoup(broswer.page_source, 'html.parser')
        job_list=soup.find('ul', class_="css-zu9cdh eu4oa1w0")
        jobs=job_list.find_all('li',recursive=False)

        for job in jobs :
            zone=job.find('div', class_="mosaic-zone nonJobContent-desktop")
            if zone == None :
                anchor = job.select_one("h2 a")
                title = anchor.find('span')
                link = anchor['href']
                company = job.find('span', attrs={'data-testid':'company-name'})
                location = job.find('div', attrs={'data-testid':'text-location'})
                job_data = {
                    'link' : f"https://kr.indeed.com{link}",
                    'company' : company.string.replace(",", " "),
                    'location' : location.string.replace(",", " "),
                    'position' : title['title'].replace(",", " "),
                }
                results.append(job_data)
    return results