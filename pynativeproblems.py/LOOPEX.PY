#1) print frist 10 natural numbers using while loop 
# counter=0
# while counter<11:
#     print("number:",counter)
#     counter+=1
print("--------------------------------------")

#2) print permid pattren 1,12,123,1234,12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

print("--------------------------------------")
#3)clculate summ of n numbers from the 1
# n=int(input('enter the number N::'))
# mlist=[]
# for i in range(1,n+1):
#     mlist.append(i)
# print("sum of all n numbers is ::",sum(mlist))
#OR
# n=int(input('enter the number N::'))
# total=0
# for i in range(1,n+1):
#     total+=i
# print("sum of all n numbers is ::",total)

print("--------------------------------------")
#4) write a program print tables

# n=int(input('enter the number N to get their table ::'))
# for i in range(1,11):
#     print(f"{n} * {i} = {i*n}")
print("--------------------------------------")
#5) display numbers feom a list using loop
# num devide by five ,must be 150 only,if the num is grater than 500 stop loop
numbers=[12,75,150,180,145,525,50]
# for i in numbers:
#     if i%5==0:
#         if i>500:
#             break
#         elif i>150:
#             continue
#         print(i)
# print("____________________________")
# for item in numbers:
#     if item>500:
#         break
#     elif item>150:
#         continue
#     elif item%5==0:
#         print(item)
print("--------------------------------------")
##6) count the total no.of digits in a number  using while loop
#Ex 75869 so o/p is 5
# num=75869
# count=0
# while num!=0:
#     num=num//10
#     count+=1
# print(count)
print("--------------------------------------")
#7)print the fallowing pattren  reverse pattren 
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j ,end=" ")
#     print()
print("--------------------------------------")
#8) print list in reverse order using a loop
#list1=[10,20,30,40,50]
#exp o/p is 50,40,30,20,10 in down manner
# list1=[10,20,30,40,50]         # method1
# count=len(list1)-1
# print(count)
# for i in list1:
#     print(list1[count])
#     count-=1

# print("_____________________________")


# list1=[10,20,30,40,50]       #method2
# size=len(list1)-1
# for i in range(size,-1,-1):
#     print(list1[i])

# print("_____________________________")

# list1=[10,20,30,40,50]  # method3
# mlist=reversed(list1)
# for i in mlist:
#     print(i)
# print("--------------------------------------")
# #9) display numbers from -10 to -1 using foe loop
# # for i in range(-10,0):
# #     print(i)
# print("--------------------------------------")
# #10)use else block to display message "done" after successful execution of for loop
# # for i in range(6):
# #     print(i)
# # else:
# #     print("Done !")
# print("--------------------------------------")
# #11) write a program to display all prime numbers with in arange
# # prime num that cann't be made by multplying other whole numbers 
# #a prime num is a natural number grater than 1 that is not a product of two smaller natural numbers 
# # range  # start=25,end=50

# # start=int(input("enter start value "))
# # end=int(input("enter end values ::"))
# # print("prime numbers in between ",start,"and ",end,"are ::")
# # for num in range(start,end+1):
# #     if num>1:
#         for j in range(2,num):
#             if num%j==0:
#                 break
#         else:
#             print(num)
print("--------------------------------------")
#12) fibonacci series up to 10 terms 
# the fiboncci sequence is a series of numbers 
# tyhe next number is found by adding up the two numbers before it 
# the frist two numbers are 0,1 
# ex 0,1,1,2,3,5,8,13,21,34.....
start1=0
start2=1
for i in range(10):
    print(start1,end=" ")
    # start1=start2    # wrong way it
    # start2=start2+start1
    start1,start2=start2,start2+start1

num1,num2=0,1
for i in range(10):
    print(num1,end=" ")
    # res=num1+num2
    # num1=num2 
    # num2=res
    num1,num2=num2,num1+num2
print("--------------------------------------")
#13)find the factorial of the given number 
# the factorial ( symbol:! ) means to multily all whole numbers from the chosen numberrs down to 1
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         res=n*factorial(n-1)
#         return res

# n=int(input(" enter n to get their factorial ::"))
# factnum=factorial(n)
# print(factnum)
# factorial=1
# for i in range(1,6):
#     factorial*=i
# print(factorial)

# num=5
# factorial=1
# if num<0:
#     print("factorial does not exists for negative number ::")
# elif num==0:
#     print(" the factorial of 0 is 1 ")
# else:
#     for i in range(1,num+1):
#         factorial*=i
#     print(" the factorial of num",num,"is",factorial)
print("--------------------------------------")
#14) riverse a given integer number 24567 in to 76542
# reversenum=0
# num=24567
# while num>0:
#     lastdigit=num%10
#     num=num//10
#     print(lastdigit,end="")

# num="24567"
# size=len(num)
# for i in range(size-1,-1,-1):
#     print(num[i],end="")

# reversenum=0
# num=24567                                    #1st iteration       2nd iteratioon          3rd            4th            5th
# while num>0:                                 #24567               #2456                   245            24             2
#     remainder=num%10                         #remainder=7         #raminder=6             5              4              2
#     num=num//10                              #num=2456            #245                    24             2              0
#     reversenum=(reversenum*10)+remainder     #reversenum=0+7=7    #rversenum=7*10+6=76    76*10+5=765    765*10+4=7654   7654*10+2=76542  
# print(reversenum)                             
#                                               #76542
print("--------------------------------------")
#15)use loops to display odd index element from the list 
# mlist=[10,20,30,40,50,60,70,80,90,100]
# print("even index values are ::",mlist[::2],end="")
# print()
# print("odd index values are ::",mlist[1::2],end="")
# print()

# for idx,item in enumerate(mlist):
#     if idx%2==0:
#         print("odd index items ::",mlist[idx])
#     else:
#         print("even index items ::",mlist[idx])
print("--------------------------------------")
#16)find cube of n numbers from 1 
# n=int(input("enter nuumber to get  cube numbers of it from 1::"))
# for i in range(n+1):
#     cubenum=i**3
#     print("cube value for :",i,"is :",cubenum)
print("--------------------------------------")
#17) find the sum of the series up to n terms  :: if n=5 then 2+22+222+2222+22222=24690
# start=2
# sumseq=0
# for i in range(0,5):
#     print(start,end="+")  # for this line 2+2+2+2+2+
#     start=start*10+2      #for this line 2+22+222+2222+22222+
#     sumseq+=start         # adding eatch start 
# print("\ntotal sum is ",sumseq )    #  total sum is  246910
print("--------------------------------------")
#18)print the fallowing pattren 
# *
# * *
# * * *
# * * * *
# * * * * * 
# * * * * 
# * * *
# * * 
# *
# for i in range(6):
#     for  j in range(i):
#         print(end="* ")
#     print()
# for i in range(6,0,-1):
#     for  j in range(i):
#         print(end="* ")
#     print()

# row=5
# for i in range(0,row):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\r")
# for i in range(row,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print("\r")

print("--------------------------------------")













