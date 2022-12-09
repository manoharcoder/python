# 8/12/2022
#1)return product if the product is <=1000 else print sum of  two numbers

# def mult_or_sum(n1,n2):
#     product=n1*n2
#     total=n1+n2
#     if(product<=1000):
#         print("product of two numbers is",product)
#     else:
#         print("sum of two numbers is ",total)

# n1=int(input("enter n1:"))
# n2=int(input("enter n2:"))
# mult_or_sum(n1,n2)
# n1=int(input("enter n1:"))
# n2=int(input("enter n2:"))
# mult_or_sum(n1,n2)
print("------------------------------------------------------------------------")
#2) print the sum of current number and the previous numbers start from 0 upto 10
# previous_value=0
# for i in range(1,11):
#     total=previous_value+i
#     print(f"previous value {previous_value} and current value {i} the sum is {total}")
#     previous_value=i
print("------------------------------------------------------------------------")
#7)print the pattrens 
#1            #1
#12           #22
#123          #333
#1234         #4444
# #12345        #55555

# for i in range(6):
#     for j in range(i):
#         print(i,end=" ")    # to get proper permid we must end="'"
#     print()         # if we not placed print() heare 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 

# # print("------------------------------------------------------------------------")

# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# print("------------------------------------------------------------------------")

#8)check given string is palindrom or not 
# to check paindrom we can do by comaring its revers to its original if it is same then it is palindrome
# myinput=input("enter the string to check wheather it is a palindrome or not ::")
# if myinput==myinput[::-1]:
#     print("our string is palindrome ")
# else:
#     print("our string is not palindrome ")

# print("------------------------------------------------------------------------")
#3) print the even index characters from the string
#heare we are passing value that is satatic value 
# name=input("enter the string to get even index characters::")
# print("even index characters are ::",name[1::2])
# print("odd index characters are ::",name[::2])
# print("------------------------------------------------------------------------")
#4)remove upto n characters in string print reamining string
# heare we dynamically passing value 
# def removechar(string,number):
#     print("original string::",string)
#     print("-----------")
#     print("truncated string is::",string[number:])
# string=input("enter the string ::")
# number=int(input("enter the nuber to truncated original string::"))
# removechar(string,number)
# print("------------------------------------------------------------------------")
#5)if element of a list frist and last same then it return True else False
# def my_lists(list1):
#     if(list1[0]==list1[-1]):
#         return True
#     else:
#         return False
# list1=[1,2,3,4,5,4,3,2,1,1,1]
# print(my_lists(list1))
# list1=[1,2,3,4,5,4,3,2,1,1,1,2]
# print(my_lists(list1))

# print("------------------------------------------------------------------------")
#6)print the numbers which are only divisible 5

# mylist=[10,26,45,44,34,57,55,90,400,45,67]
# for i in mylist:
#     if i%5==0:
#         print(i,"which is divisble by the 5")
#     else :
#         print(i,"which is not divisble by the 5")
# print("------------------------------------------------------------------------")

#9)create a mewlist from existing two lists append oddnum from the list1 and then append even numbers from list2

# def filter(list1,list2):
#     newlist=[]
#     for i,j in (list1,list2):         #ValueError: too many values to unpack (expected 2)
#         if i%2!=0 and j%2==0:
#             newlist.append(i)
#             newlist.append(j)
#     print("newlist is ",newlist)
# list1=[7,12,45,78,96,45,98,32]
# list2=[1,5,9,48,98,75,69,32,36,42]
# filter(list1,list2)
# print("------------------------------------------------------------------------")

#10)reverse a nuber abd sparate by sapace 1234 in to 4 3 2 1

# num=int(input("enter a number to get revers of it ::"))
# revnum=0
# while(num>0):
#     lastdigit=num%10     # to get last digit from num
#     num=num//10          #flore division is used to truncate the floating point values
#     print(lastdigit,end=" ")

# print("------------------------------------------------------------------------")
#11)caluclat tax % for frist10k it is 0% next 10k it is 10%  for reamining money it is 20% find total tax 

# income=int(input("entyer income to find out tax % ::"))
# tax=0
# if(income<=10000):
#     tax=0
# elif(income<=20000):
#     netamount=income-10000
#     tax=(netamount)*10/100
# else:
#     tax=0
#     tax=10000*(10/100)         # dont enter heare (income-10000)it gives more value
#     tax=tax+((income-20000)*20/100)
# print(f"total tax % for your income {income} is {tax}")

# print("------------------------------------------------------------------------")
#12)print the reverse pattren of 
#*****
#****
#***
#**
#*
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# print("------------------------------------------------------------------------")



