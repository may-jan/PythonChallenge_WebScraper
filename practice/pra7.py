"""
12/04
  1. 요청
  2. 응답
  3. 응답파싱
  4. 데이터 가공
"""
# Request & BeautifulSoup 라이브러리
from bs4 import BeautifulSoup  # 응답 결과를 파싱,가공하기 위한 library
from requests import get  # http 요청을 위한 library

# http 요청할 url
base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_term = 'java'

# 요청 후 응답 받기
response = get(f"{base_url}{search_term}")

# 응답에 따른 조건문
if (response.status_code != 200):
  print("Can't request website")
else:
  results = []  # 데이터를 저장할 list
  soup = BeautifulSoup(response.text, 'html.parser')  # html 파싱
  jobs = soup.find_all('section', class_='jobs')  # find_all()을 사용하여 원하는 데이터 추출
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)  # 마지막 요소 제거
    for post in job_posts:
      anchors = post.find_all('a')
      anchor = anchors[1]
      link = anchor['href']  # Dictionary처럼 태그의 요소 가져오기
      company, kind, region = anchor.find_all('span', class_='company')
      title = anchor.find('span', class_='title')

      job_data = {
          'company': company.string,
          'region': region.string,
          'position': title.string,
      }
      results.append(job_data)

for result in results:
  print(result)
  print('==========================')