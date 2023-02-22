#1) create function in python
# def demo(name,age):
#     print(name,age)
# demo("manohar",23)

print("-------------------------------------")
#2)create a function with variable length of arguments
# def function(*args):
#     print("printing values::")
#     print(*args)                             #or for i in args:print(i)
# function(1,2,3,4,5,6,7,8,9)
# function(1,2,3,4,5)
print("-------------------------------------")
#3)retun mutiple values  from a function 
# def calculation(a,b):
#     return a+b,a-b         # add=a+b,minus=a-b
# res=calculation(50,10)
# print(res)
# res1,res2=calculation(50,20)   # or res=calculation(30,50)    print(res) o/p=(80,-20)
# print(res1)
# print(res2)
print("-------------------------------------")
#4)create a function with a default arguments 
# def show_employe(ename,esalary=9000):
#     print("employe name is ::",ename,"\n and employe salary is ::",esalary)
# show_employe("mahesh",40000)
# show_employe("manu")            # if place dafault value  even if it not call that default treated as ip to function call
print("-------------------------------------")
#5) create a n inner funtion to calculate the addition in the fallowing way 
## create a outer function that will accepet two parameters a,b
##create a inner function in side a outer function that will claculate addition of a,b
## at last outer function will add  5 in to addition and return it 
# def calculations(a,b):
#     def add(a,b):
#         return a+b
#     sum=add(a,b)
#     return sum+5
# total=calculations(20,30)
# print(total)
print("-------------------------------------")
#6) create a recursive function that call itself for n no.of times 
# heare we need to calculate sum of frist 10 numbers using recursive function
# def num_sum(i):
#     if i==0:
#         return 0
#     elif i==1:
#         return 1
#     else:
#         return i+num_sum(i-1)
# result=num_sum(10)
# print(result)

# def num_sum(num):
#     if num>0:
#         return num+num_sum(num-1)
#     else:
#         return 0
# result=num_sum(10)
# print(result)
print("-------------------------------------")
#7)  assign a diffrent name to functiono and call it through the new name 
# display_student(name,age).assigh a new name show_student(name,age) to it and call it using new name
# heare we use assignment operator to assing new function name to the old function name 
# def display_student(name,age):
#     print(f"student name {name} and his age is {age}")

# display_student("manu",23)
# show_student=display_student      ## new_func_name=old_fun_cname
# show_student("manu",33)
#8)generate a py list of even numbers in between 4 to 30 
# def genrate_even(a,b):
#     evenlist=[]
#     for i in range(a,b):
#         if i%2==0:
#             evenlist.append(i)
#         else:
#             pass
#     return evenlist
# a=int(input("a::"))
# b=int(input("b::"))
# res=genrate_even(a,b)
# print(res)

# print(list(range(4,30,2)))

#9)find the lagest item from the giiven list
#x=[4,6,8,24,12,2]
x=[4,6,8,24,12,2]
# print(max(x))    # it is a single liine answer max(),sum() are built in functions 
# sorted=x.copy()
# sorted.sort()
# print(sorted)
# print(sorted[-1])

# max=0
# for num in x:     #4       6       8       24       12             2
#     if num>max:   #4>0     6>4     8>6     24>8     12>24 fails    2>24fails 
#         max=num   #max=4   #max=6  #max=8  #max=24
# print(max)                                                       #o/p is max=24only

# max of 2,3 numubers using the functions 
# def max_of_two_num(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def max_of_three_num(x,y,z):
#     return max_of_two_num(x,max_of_two_num(y,z))

# print(max_of_two_num(4,5))
# print(max_of_three_num(4,5,6))












