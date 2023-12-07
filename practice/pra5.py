"""
11 / 31
"""
# Method
# 데이터에 결합된 function (JS 배열 형태)
name1 = 'jan'
name2 = 'JAN'

print(name1.upper())  # JAN (대문자로 변경)
print(name2.lower())  # jan (소문자로 변경)
print(name1.isupper())  # False (대문자인지 확인)
print(name1.islower())  # True (소문자인지 확인)
print(name1.capitalize())  # Jan (첫글자를 대문자로 변경)
print(name1.replace('n', '🐣'))  # ja🐣 (기존 글자를 원하는대로 변경)
print(name1.startswith('j'))  # True (시작문자가 맞는지 확인)
print(name1.endswith('m'))  # False (끝문자가 맞는지 확인)

# Lists
# 데이터 추가 및 변경 가능
days_of_week = ['월', '화', '수', '목', '금']

days_of_week.append('토')
print(days_of_week)  # ['월', '화', '수', '목', '금', '토']
days_of_week.append('일')

print(days_of_week)  # ['월', '화', '수', '목', '금', '토', '일']
days_of_week.remove('월')  # ['화', '수', '목', '금', '토', '일']

print(days_of_week[2])  # 목
print(days_of_week[-1])  # 일

days_of_week.clear()
print(days_of_week)

# Tuples
# 튜플은 불변성을 가짐, 데이터 추가 및 변경 불가
days = ('월', '화', '수', '목', '금')

# Dictionary (JS 객체 형태)
# 데이터 추가 및 변경 가능
player = {
  'name' : 'jan',
  'age' : 20,
  'fav_food' : ['🥐', '☕']
}

print(player.get('name'))  # jan
print(player.get('fav_food'))  #  ['🥐', '☕']
print(player['fav_food'])  #  ['🥐', '☕']

player.pop('age')
print(player)  # {'name':'jan', 'fav_food':['🥐', '☕']}

player['height'] = 160
print(player)  # {'name':'jan', 'fav_food':['🥐', '☕'], 'height':160}

player['fav_food'].append('🍝')
print(player['fav_food'])  # ['🥐', '🍝']