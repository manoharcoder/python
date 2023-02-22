# 1).accept the number from the user 
# number=int(input("enter the number that you want to print ::"))
# print("your entered number is ",number)

print("------------------------------------------------------------------------")

#2).display the three strings "name","is","james" as name**is**james 
# str1="name"
# str2="is"
# str3="james"
# print(str1+"**"+str2+"**"+str3)

# print(str1,str2,str3,sep="**")

# print("name","is","manu",sep="**")

print("------------------------------------------------------------------------")

#3).convert decimal number to octal using print() output formating
#0b or 0B    binary
#0o or 0O    octal
#0x or 0X    hexa decimal
# print(0b11)           #3
# print(0o15)           #13 
# print(0xFB)           #251
# print(0b11+0o15+0xFB)  #3+12-251=267
# num=int(input("enter number to conert them in to different format::"))
# print("integer format %i"%num)
# print("floating point format %f"%num)
# #print("complex number format %complex"%num)
# #print("binary format %binary"%num)
# print("octal format %o"%num)
# print("hexadecimal format %x"%num)

print("------------------------------------------------------------------------")

#4) display the float number with 2 decimal place susing print()
# from math import pi
# print("original pi value",pi)
#print("print decimal places up 2 only %0.2f"%pi)  #while using % no need to  use ,

print("------------------------------------------------------------------------")
#5) accept a list of 5 float numbers as a n input from the user 
# floatingnumlist=[]
# for i in range(5):
#     number=float(input("enter floating point numbers ::"))
#     floatingnumlist.append(number)

# print("list of 5 floating numbers ::",floatingnumlist)


print("------------------------------------------------------------------------")

#6).write all content of a given file into a new file by skipping line number5
""" given test.txt"""         """expected o/p new_file.txt"""
#line1                        #line1
#line2                        #line2
#line3                        #line3
#line4                        #line4
#line5                        #line6
#line6                        #line7 
#line7

# with open("test.txt","x") as f:
#     print(f.writelines("line1\nline2\nline3\nline4\nline5\nline6\nline7"))

# with open("test.txt","r") as f:
#     print(f.read())
#     print("----------------")
#     print(f.tell())
#     print(f.seek(0))
#     print("----------------")
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.tell())
#     print(f.seek(35))
#     print(f.read())
  
with open("test.txt","r") as f:
    mylist=f.readlines()
    print(mylist)
    for idx,i in enumerate(mylist):
        if idx==4:
            continue
        print(i)


print("------------------------------------------------------------------------")
#7). accept any three strings from one input call
# mystr=[]
# for i in range(3):
#     str=input("enter tstrings::")
#     mystr.append(str)
# for i in mystr:
    # print
    
#     ####using split method 
# str1,str2,str3=input("enter string::").split()
# print("string1::",str1)
# print("string2::",str2)
# print("string3::",str3)

print("------------------------------------------------------------------------")
#8).format variables using string format()method

# x=5.34546
# y=6
# z=x+y
# # print("the value of x is {} and value of y is {} then the sum is {}".format(x,y,z))
# # print(f"the value of x is {x} and value of y is {y} then the sum is {z}")
# # print("the value of x is ",x," and value of y is ",y," then the sum is ",z)
# # print("hello{name}\n{greeting}".format(greeting='good morning',name="manu"))
# print("the int value of x is %i"%x)
# print("the float value of x is %f"%x)
# print("the float with truncated floating values  x is %0.2f"%x)
# print("the complex value of x is ",complex(z))


# totalmoney=1000
# quantity=3
# price=450
# # i have 1000 dollars so i can buy 3 foodball for 450.00dollars.
# print(f'i have {totalmoney} dollars so i can buy {quantity} foodball for {price:.2f} dollars.')
# print('i have {} dollars so i can buy {} foodball for {:.2f} dollars.'.format(totalmoney,quantity,price))
# print('i have ',totalmoney,' dollars so i can buy ',quantity,'foodball for ',price,' dollars.')
# print('i have %i dollars so i can buy %i foodball for %.2f dollars.'%totalmoney%quantity%price)

print("------------------------------------------------------------------------")

# # #9).check file is empty or not 
# f=open("test.txt","r")
# starting_point=f.tell()
# f.read()
# ending_point=f.tell()
# if(starting_point==ending_point):
#     print("test.txt is empty")
# else:
#     print("test.txt is not empty")
# print("from",starting_point,"to",ending_point,"characters of data that we had in this file ")
# f.seek(0)
# print(f.read())

#another way
# import os
# size=os.stat("sample.txt").st_size
# if size==0:
#     print("file is empty")
# else:
#     print("file is not empty")

print("------------------------------------------------------------------------")

#10).read the linenumber4 frome the fallowing file 
""" given test.txt"""         """expected o/p new_file.txt"""
#line1                        #line4
#line2                        
#line3                        
#line4                        
#line5                       
#line6                         
#line7

# with open("test.txt","r") as f:
# #     mylist=f.readlines()
# #     print(mylist[3])

# # #in another way 

# print("line no.4 is",mylist[3])
# for idx,i in enumerate(mylist):
#     if idx==3:
#         print(i)










