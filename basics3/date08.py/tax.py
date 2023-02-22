income=int(input("Enter income:"))
tax=0
if income<=10000:
    tax=0
elif income<=20000:
    netamout=income-10000
    tax=(netamout)*10/100
else:
    tax=0
    tax=(10000)*10/100
    tax=tax+(income-20000)*20/100

print("tax is tax %0.2f"%tax )