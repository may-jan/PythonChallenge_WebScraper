"""
11 / 30
"""
# input()
# 사용자에게 질문이 표시되는 function, 오직 1개의 argumnet만 받을 수 있다.
age = input('How old are you?')
print(f"user answer: {age}")

# type()
# 변수의 타입을 알려주는 function
print(type(age))  # <class 'str'>

# int()
# 정수 값으로 변경해주는 function
int_age = int(input('How old are you?'))
print(type(int_age)) # <class 'int'>

# and, or
if (int_age <= 4):
  print('아기')
elif (int_age >= 8 and int_age <= 13):
  print('초등학생')
elif (int_age >= 14 and int_age <= 16):
  print('중학생')
elif (int_age >= 17 and int_age <= 19):
  print('고등학생')
elif (int_age == 5 or int_age == 6 or int_age == 7):
  print('유치원생')
else:
  print('성인')

# while
# 조건이 참이면 코드 반복, 조건이 거짓이면 코드 종료
from random import randint
# 파이썬 표준 라이브러리 https://docs.python.org/ko/3/library/index.html

print('🎲Welcome to Python Game🎲')
pc_choice = randint(1, 30)
playing = True
count = 0

while (playing):
  user_choice = int(input('Chose number 1~30! '))
  if (user_choice > 30 or user_choice < 1):
    count += 1
    print('1~30 사이의 숫자를 입력해주세요')
    playing = True
  elif (user_choice == pc_choice):
    count += 1
    print(f"정답! {count}번 만에 맞추셨습니다!")
    playing = False
  elif (user_choice > pc_choice):
    count += 1
    print('Lower!')
    playing = True
  elif (user_choice < pc_choice):
    count += 1
    print('Higher!')
    playing = True