import math
total_bill=input("What is the total amount bill")
total_paid=input("What is the total paid ")
tip=int(total_paid)-int(total_bill)
ppleToPay=input("How many people are paying")
eachPay=int(total_paid)/int(ppleToPay)
tipPercent=(int(tip)*100)/int (total_bill)
pay=float(eachPay)
print("How much did each person pay "+str(pay))
