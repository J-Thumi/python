import random

num='1234567890'

number=''

for i in range(8):
  number +=random.choice(num)

print(f'07{number}')
