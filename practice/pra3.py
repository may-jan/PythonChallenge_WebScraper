"""
11 / 29
"""
# Default Parameter 기본 파라미터
def say_hello2(name='default user'):
  print('Hello', name)

say_hello2('jan') # Hello jan
say_hello2() # Hello default user

# 과제 : 계산기 만들기 (에러 안나게)
def plus(a=0, b=0):
  print(a + b)

def minus(a=0, b=0):
  print(a - b)

def multiplication(a=0, b=0):
  print(a * b)

def division(a=0, b=1):
  print(a / b)

def power_of(a=0, b=1):
  print(a**b)

plus(1, 2)
minus(4, 2)
multiplication(3, 5)
division(10, 4)
power_of(4)

plus()
minus()
multiplication()
division()
power_of()

# Return Value : 함수의 바깥으로 값을 보낼 수 있게 해준다, return 이후의 코드는 death
def tax_cal(money):
  return money * 0.35

def pay_tax(tax):
  print('Thank you for paying', tax)

to_pay = tax_cal(30000)
pay_tax(to_pay)

# f"~~{}"  =>   JS의 `~~${}`역할(템플릿 리터럴)
name ='jan'
age=20

print(f"Hello I'm {name}! I'm {age} years old")  # Hello I'm jan! I'm 20 years old

# 조건문 if
# EX1) if else
if 10 > 5 : 
  print('True!')  # True!
else:
  print('False!')

# EX2) if elif else
score = 60
if (score > 90):
  print('Your Score is A')
elif (score > 80):
  print('Your Score is B')
elif (score > 70):
  print('Your Score is C')
else:
  print('Your Score is D, Cheer Up!')  # Your Score is D, Cheer Up!