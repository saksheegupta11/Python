# Write a program to calculate electricity bills based on consumption slabs.
units = int(input("Enter units consumed:"))
sgst = (18*units)/100
service_tax = (5*units)/100
if 1 <= units <= 30:
    amount = (units * 3.34) + sgst
    print("Amount to be paid:", amount)
elif 31 <= units <= 50:
    amount = (units * 4.27) + sgst
    print("Amount to be paid:", amount)
elif 51 <= units <= 150:
    amount = (units * 5.23) + sgst    
    print("Amount to be paide: ", amount)
elif 151 <= units <= 300:    
    amount = (units * 6.61) + sgst
    print("Amount to be paid:", amount)
else:
    amount = (units * 7.11) + sgst + service_tax
    print("Amount to be paid:", amount)    