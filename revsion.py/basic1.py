# in python everything is a objects even variables and functions also
# num=[1,2,3,4,5]
# print(type(num))     #<class "list">
# flag=True
# print(type(flag))     #<class "bool">
# def my_function():
#     pass
# print(type(my_function)) #<class "function">

# all the entities instantiate feom a class  so (list,bool,function ) they are all objects

#dir()
num=[1,2,3,4,5]
print(dir(num))
# r=num.__add__([6,7,8,9])
# print(r)
# R=num+[1,2,3,4,5]
# print(R)

# #id()
# num=[1,2,3,4,5]
# print(id(num))
# a=10
# print(id(a))
# print(id(10))

##how variables will work
# a=[1,2,3]
# b=a           # ids will be same 
# a.append(4)
# print("a=",a)
# print("b=",b)

# a=[1,2,3]
# b=a.copy()  #it copys first given data only  so now their ids also be different
# a.append(4)
# print("a=",a)
# print("b=",b)

'''count=0
while count<0:
    print("hi")
'''
#WHILE
# count=0
# while (count<3):
#     print("hi")
#     print("hello")
#     count+=1

#tables with while
# num=int(input("enter number to get their table;;"))
# count=1
# while count<=10:
#     product=count*num
#     print(f'{num} * {count} ={product}')
#     count+=1
# #tables using for and range
# number=int(input("enter the number :\t"))
# for i in range (1,11):
#     print(f"{number} X {i}={number*i}")
#     #print("{} X {} = {}".format(number,i,number*i))
#     #print(number," X ",i," = ",number*i)

#find out sum of 1 to 100 numbers
# total=0
# for i in range(1,101):
#     total+=i
# print(total)   #5050



