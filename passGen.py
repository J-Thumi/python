import random

pas='1234567890!@#$%^&*~,.qwertyuioplkjhgfdsazxcvbnm'

password=''

for i in range(16):
  password+=random.choice(pas)
  
print(password)
  
