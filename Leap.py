import math
yearBorn=input("What year were ypu born in ?")
a=int(yearBorn)%4
if a==0:
   print("The year you were born in is leap ")
else:
  print ("The year you were born in is not leap")
