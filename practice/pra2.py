"""
11 / 28
"""

# 함수
print(True)


# def 키워드를 통해 function 을 정의
def say_hello():
  print('Hello How Are You?')

say_hello() # Hello How Are You?


# Indent 들여쓰기 (탭 1번 or 스페이스 2번)
# 들여쓰기를 통해 스코프가 지정된다
def say_bye():
  # 주석도 들여쓰기 규칙 지켜주기
  print('Bye~')
  say_hello()

say_bye() # Bye~  # Hello How Are You?


# Parameter 파라미터 (함수에 데이터를 전달해준다)

# name, age => 파라미터
def say_hello(name, age):
  print('Hello', name)
  print('You are', age, 'years old')

# jan, 20 => 인자
say_hello('jan', 20) # Hello jan  # You are 20 years old