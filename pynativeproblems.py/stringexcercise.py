#1) create a string madeup of first, middle,last character
#ex manohar o/p=mor

# string="manohar"
# newstring=string[0]+string[len(string)//2]+string[-1]       # use // to get integer value 
# print(newstring)                                            # float vlaues are not axcepted for accesing the index positions 

# # create a string made up of the middle three characters 
# str1="jhondippeta"
# midleindex=len(str1)//2
# m=midleindex
# print(str1[m-1:m+2])
# str2="jasonay"
# midleindex=len(str2)//2
# m=midleindex
# print(str2[m-1:m+2])
#2) append the new string in the middle of the of the given string
# give 2 strings s1,s2  write py to create new s3 by appending s2 in in the midle of the s1
# s1="ault"
# s2="kelly"
# l=len(s1)
# m=l//2
# part1=s1[:m]
# part2=s1[m:]
# s3=part1+s2+part2
# print(s3) 

# def addstr(str1,str2):
#     m=len(str1)//2
#     p1=str1[:m]
#     p3=str1[m:]
#     p2=str2
#     return p1+p2+p3
# print(addstr("ault","kelly"))

#made a string  that made by start,middle,end charecter of each string
# s1="america"
# s2="japan"
# s3=s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
# print(s3)
# def mix_string(s1,s2):
#     frist_char=s1[0]+s2[0]
#     middle_char=s1[int(len(s1)/2):int(len(s1)/2)+1]+s2[int(len(s2)/2):int(len(s2)/2)+1]
#     last_char=s1[len(s1)-1]+s2[len(s2)-1]
#     res=frist_char+middle_char+last_char
#     print("mix string i s::",res)
# mix_string("america","japan")

# #4) arrange string characters such tthat lowecase letters should comoe first
# str1="PyNaTive"    # op=yaivePNT
# lower=[]
# upper=[]
# for char in str1:
#     if char.islower():
#         lower.append(char)
#     else:
#         upper.append(char)
# totalstr="".join(lower+upper)  #yaivePNT
# #totalstr=lower+upper          # ['y', 'a', 'i', 'v', 'e', 'P', 'N', 'T']
# print(totalstr)

#5) count all letters ,digits,and special symbols from a given a string
str1="p@#yn26at^&i5ve"
#o/p chars=8,digits=3,symbol=4
# char=[]
# digits=[]
# symbols=[]
# for i in str1:
#     if i.isalpha():
#         char.append(i)
#     elif i.isnumeric():
#         digits.append(i)
#     else:
#         symbols.append(i)
# print("char=",len(char))
# print("digits=",len(digits))
# print("symbols=",len(symbols))

# char=0
# digits=0
# symbols=0
# for i in str1:
#     if i.isalpha():
#         char+=1
#     elif i.isnumeric():
#         digits+=1
#     else:
#         symbols+=1
# print("char=",char)
# print("digits=",digits)
# print("symbols=",symbols)

print("--------------------------------------------------------------------")
#6)create a mixed string using the fallowing rules
#s1,s2  create s3 that is  frist char of s1,then last char of s2 and second char  of s1 and last second char of s2 as like contiounue
# def mixchar(s1,s2):
#     s3=[]
#     for idx i,j in enumrate(s1,s2):
#         first_char=s1
# s1="abc"
# s2="xyz"
# s1len=len(s1)
# s2len=len(s2)
# s3=""
# hlength=s1len if s1len>s2len else s2len
#  # we need to add s2 in reverse mane=er so rever it first
# s2=s2[::-1]

# # s1 accending and s2 decending
# for i in range(hlength):
#     if i<s1len:
#         s3+=s1[i]
#     if i< s2len:
#         s3+=s2[i]
# print(s3)


# s1="abc"
# s2="xyz"
# s1len=len(s1)
# s2len=len(s2)
# s2=s2[::-1]
# s3=""
# hlength=s1len if s1len>s2len else s2len
# for i in range (hlength):
#    s3+=s1[i]+s2[i]     # if lengths are same it will work else check inindividua using if loop
# print(s3)
print("--------------------------------------------")
#7)sting charecter balance test and return true 
#s1 of all charecters should be present in the s2 sting but not necesary of vicevers of it then it calles as  string balance test
# s1="yn"
# s2="pYnative"
# lenth=len(s1) if len(s1)>len(s2) else len(s2)
# count=0
# # note : iterate tthough s1 and check for is that element prest in s2 also return true finally else false
# for i in s1:
#     for j in s2:
#         if i==j:    # case sensetive 
#             count+=1
#         else :
#             pass
# print(True if count==len(s1) else False )

# def string_balnce_test(s1,s2):
#     flag=True
#     for char in s1:
#         if char in s2:
#             print(char)
#             continue
#         else:
#             flag=False
#     return flag
# s1="Yn"
# s2="pYnative"
# result=string_balnce_test(s1,s2)
# print(result)

# s1="ynf"
# s2="pYnative"
# result=string_balnce_test(s1,s2)
# print(result)

# #8)  find the all occurences of a substring in a give sting by ignoring  the case 
# #write  a program to to find  all occurence of a "USA"  in a given string ignoring the cae
# str1="Welcome to USA.usa awesome"
# the usa count is :2
# str1="Welcome to USA.usa awesome"
# str1=str1.lower()
# print(str1)
# print(str1.count("usa"))

# str1="Welcome to USA.usa awesome"
# s_case=str1.lower()
# check="USA"
# s_check=check.lower()
# count=s_case.count(s_check)
# print(" the usa count is :",count)

#9) claculate sum and average of digits present in  a string 
# str="Pynative29@8496"
#sum is :38 Average is 6.3333333333333
# str="Pynative29@8496"
# digits=[]
# for i in str:
#     if i.isnumeric():
#         digits.append(i)  # truncation importantent heare 
#     else:
#         continue
# print(digits)
# # print("sum is :",sum(digits),"Average is :",sum(digits)/len(digits))
# total="+".join(digits)
# print(total)
# sum=eval(total)
# count=len(digits)
# print("sum is :",sum,"Average is :",sum/count)

# str="Pynative29@8496"
# total=0
# count=0
# for char in str:
#     if char.isdigit():
#         total+=int(char)
#         count+=1
# avg=total/count
# print("sum is :",total,"Average is :",avg)

# import re
# str="Pynative29@8496"
# digit_list=[int(num) for num in re.findall(r"\d",str)]
# print(digit_list)

#10) write a program to count occuences of all within a string
# str1="Apple"
# {"A":1,"p":2,"e":1}

# str="Apple"
# mdict=dict()
# for char in str:
#     count=str.count(char)
#     mdict[char]=count

# print(mdict)

#11)reverse a given string
# str="PYnative"
# # print(str[::-1])

# # # and also we can use reversed()
# str=reversed(str)    # reversed creates a objs
# # print(list(str))
# str="".join(str)
# print(str)

#12) find the last position of  give substring
# str1="Emma is a data scientist who know python.Emma works at google."
# o/p= last oocuence of Emma  starts at index is 43
# str1="Emma is a data scientist who knows python. Emma works at google."
# index=str1.rfind("a")
# print("last oocuence of Emma  starts at index is ",index)

#13) split a string on hyphens
#str1="Emma-is-a-data-scientist"
#o/p=Emma  is  a  data  scientist
# str1="Emma-is-a-data-scientist"
# listt=str1.split("-")  # split method split anyrhing based on condition and stored it in list from
# for i in listt:
#     print(i)

#14) remove empety string from a list of strings
#str_list=["Emma","jon","","kelly",None,"eric",""]
# o/p=["Emma","jon","kelly","eric"]    # use filter or if

# str_list=["Emma","jon","","kelly",None,"eric",""]
# new_list=list(filter(None,str_list))
# print(new_list)

# str_list=["Emma","jon","","kelly",None,"eric",""]
# new_list=[]
# for element in str_list:
#     if element:
#         new_list.append(element)
# print(new_list)

#15) remove special symbols/ punctuation from a string
# str1="/*jon is @developer & musician"
# o/p=jon is developer musician
# str1="/*jon is @developer & musician"
# new_str=[]
# for i in str1:
#     if i.isnumeric():
#         new_str.append(i)
#     elif i.isalpha():
#         new_str.append(i)
#     elif i.isnumeric():
#         new_str.append(i)
#     elif i.isspace():
#         new_str.append(i)
#     else:
#         pass
# print(new_str)
# new_list="".join(new_str)
# print(new_list)

# import re   # using regex replace pattren in a string
# str1="/*jon is @developer & musician"
# print("original string is :",str1)
# #replace special symbols with  ""
# result_str=re.sub(r"[^\w\s]",'',str1)
# print(result_str)


#using functions
#transulate() and maketrans() [the string.punctuation constant contains all special symbols]
#use translate() function to get a new string  where specified characters are replaced with the character described in a dictionary or or a mapping table
# use the maketrans() function to create a mapping table 

# import string
# str1="/*jon is @developer & musician"
# print("original string is :",str1)

# result_str=str1.translate(str.maketrans(" "," ",string.punctuation))
# print(result_str)

#16)remove all characters feom a string except integers
str1=" i am 25 years and 10 months old"
# op=2510
# new_str=[]
# for i in str1:
#     if i.isnumeric():
#         new_str.append(i)
# print(new_str)
# new_list="".join(new_str)
# print(new_list)

# res="".join([i for i in str1 if i.isdigit()])
# print(res)

#17) find the words with both alphabets and numbers
str1="Emma25 is data sicient50 and AI expert"
# op=Emma25
#    scientist50
# use the built in function any() with the combination of string functions alpha() and digit()
# res=[]
# temp=str1.split()
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)
# for i in res:
#     print(i)

#18) replace each special symbol with # in the fallowing string

import string
str1="/*jon is @developer & musician!"
#str1=str1.replace("#",string.punctuation)  # we cant give like this 
for char in string.punctuation:
    str1=str1.replace(char,"#")
print(str1)






