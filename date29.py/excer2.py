'''#6)write a program to validate a person can vote or not 
take the age as input 
if the age is less than 18 print he can't vote
if the age is grater than 18 print he can vote 
if the age is grater than 90 print please stay at home 
if the age is 18 than print please  make the voter id'''

name=input("enter name of the person :\t")
age=int(input("enter the person age :\t"))
if(age>0 and age<100):
    if (age<18):
        print(name,"can't vote and his age is ",age ,"only")
    elif(age==18):
        print(name,"please  make the voter id and your age is",age)
    elif(age>18 and age<90):
        print(name,"can vote  and his age is",age)
    elif(age>=90):
        print(name,"please stay at home your age is",age)  
else:
   print("enter valid age ")