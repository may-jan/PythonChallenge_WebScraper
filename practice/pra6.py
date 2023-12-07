"""
12/02
"""
# For Loops
# 튜플의 내역들을 하나씩 훑어보기
nums = (1, 2, 3, 4, 5, 6)
for num in nums:
  print(num)  # 1  # 2  # 3  # 4  # 5  # 6

# Request
# https://pypi.org/ => 사람들이 만든 project, module을 모아둔 곳
# $ pip install requests
from requests import get
request_results = {}

websites = (
    'google.com',
    'https://naver.com',
    'https://daum.net',
    'facebook.com',
    'https://youtube.com',
)

for website in websites:
  # not => js의 ! 역할
  if not (website.startswith('https://')):
    website = f"https://{website}"
  response = get(website)
  # print(response.status_code)
  if (response.status_code == 200):
    request_results[website] = "OK"
  else:
    request_results[website] = "FAILED"

print(request_results) 
'''
{'https://google':OK, 'https://naver.com':OK, 'https://daum.net':OK,
  'https://facebook.com':OK, 'https://youtube.com': OK}
'''