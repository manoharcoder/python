"""PYTHON OUTPUT  USING PRINT FUNCTION """
#print(*objects,sep=" ",end="\n",file=sys.stdout,flush=false)
# print(1,2,3,4,5)
# print(1,2,3,4,5,sep="   ")
# print(1,2,3,4,5,sep="#",end="$")

"""OUTPUT FORMATING"""
# x=5.34546
# y=6
# z=x+y
# # print("the value of x is {} and value of y is {} then the sum is {}".format(x,y,z))
# # print(f"the value of x is {x} and value of y is {y} then the sum is {z}")
# # print("the value of x is ",x," and value of y is ",y," then the sum is ",z)
# # print("hello{name}\n{greeting}".format(greeting='good morning',name="manu"))
# print("the value of x is %i"%x)
# print("the value of x is %f"%x)
# print("the value of x is %0.2f"%x)

'''PYTHON INPUT'''
# name=input("enter name :\n")
# num=str(input("enter name :\n"))
# num=int(input("enter integernumber :\n"))
# num=float(input("enter floating point number :\n"))
# num=complex(input("enter complex number :\n"))

# print(int("10"))
# print(float('10'))
# print(complex('10'))

# print(int("0+1"))
# print(eval("0+1"))    '''eval function is used to do operation on string based naumbers '''

"""PYTHON IMPORT"""
# # import math
# # r=10
# # PI=math.pi
# # print(PI*r*r)

# import math as m
# r=10
# PI=m.pi
# print(PI*r*r)

# # from math import pi 
# # r=10
# # print(pi*r*r)

'''WHILE'''
#add numbers from 1 to 10
'''sum=0
i=1
n=int(input("enter numberto get sum up to the number:: "))

while n>=i:
    sum=sum+i  #increasing sum every time while runing this while loop
    i+=1   #update counter

print("the sum is ",sum)  '''

# #while loop else
# sum=0
# i=1
# n=int(input("enter numberto get sum up to the number:: "))
# while n>=i:
#     sum=sum+i  #increasing sum every time while runing this while loop
#     i+=1   #update counter
# else:
#     print("we reaches your deasired number ")
# print("the sum is ",sum)


# counter=0
# while counter<=3:
#     counter+=1
#     print("i am in side loop")
# else:
#     print("i am at out side of the loop")

''' FOR LOOP'''
# num=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in num:
#     sum+=i
# print(sum)

''' RANGE FUNCTION'''
#range(start,stop,step)
# print(range(10))
# print(list(range(10)))
# print(list(range(2,5)))
# print(list(range(2,10,2)))

#eterate through a list using its len()

# name=["hi","hello","good"]
# for i in name:
#     print(i)

# name=["hi","hello","good"]
# for i in range(len(name)):
#     print("i say to all",name[i])

#for loop with else case
# digits=[1,2,3,4,5]
# for i in digits:
#     print(i)
# else:
#     print("no items left")

# program to display student marks from record 

# name=input("enter student name tha do want to get their marks :: ")
# marks={"vanu":90,"james":80,"manu":90,"mohan":89}
# for student in marks:
#     if name==student:
#         print(marks[student])
#         break
# else:
#     print("no entry with that name found")

''' BREAK AND CONTINU USE CASE IN WHILELOOP ,FOR LOOP'''
# # for value in "string":
# #     if value=="i":
# #         break
# #     print(value)
# # print("the end")

# # for value in "string":
# #     if value=="i":
# #         continue
# #     print(value)
# # print("the end")

num=int(input("enter number ::"))
i=0
while i<num:
    i+=1
    if i==5:
        break
    print(i)

# num=int(input("enter number ::"))
# i=0
# while i<num:
#     i+=1
#     if i==5:
#         continue
#     print(i)
