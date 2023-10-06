#Josphat Waweru SCT211-0003/2022
height=input("What is your height in metres")
weight=input("What is your weight in kilograms")
BMI=int(weight)/ math.pow(float(height),2)
if BMI<18:
  print("You are underweight")
elif BMI>24:
  print("You are overweight")
else :
  print("You are normal")
