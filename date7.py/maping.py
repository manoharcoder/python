"""MAP"""
#map function return a map objects(which is an iterator)of the results 
# ofter applying the given function to each item of a given iterable(list,tuple etc)
#map(fun,iter)
  #fun==it is a function to which map passes each element of a given iterable 
  #iter==it is iterable which is to be mapped
  # NOTE:we can pass one more iterables to the map()function
  #note::the return value from the map()(map object)then can be passed to function like list(to create list),set(to create set)

# #return doublr of n
# def add(n):
#     return n+n
# #we double all the numbers using map
# numbers=(1,2,3,4,5)
# result=map(add,numbers)
# print(list(result))
print("----------------------------------------------------")
# #double all the numbers using map()and lambda
# numbers=(1,2,3,4,5,6)
# result=map((lambda x:x+x),numbers)
# print(list(result))
print("----------------------------------------------------")
# #add two lists using map,lambda
# list1=[1,2,3,4]
# list2=[9,8,7,6]
# total=map(lambda x,y:x+y,list1,list2)
# print(list(total))
print("----------------------------------------------------")

#list of string
# l=['sat','bat','cat','mat']
# test=list(map(list,l))  # map can listfy the list of strings individually
# print(test)
print("----------------------------------------------------")
def sqare(a):
    return a*2
def cube(a):
    return a**3
functions=[sqare,cube]
numbers=[1,2,3,4,5,6,7,8,9]
for i in numbers:
    result=list(map(lambda x:x(i),functions))
    print(result)
print("----------------------------------------------------")
def salary(a):
    sal=a
    return sal
def bonus_salary(a):
    bonus=a+((a*20)/100)
    return bonus
functions=[salary,bonus_salary]
normal_salary=[10000,20000,30000,40000,50000]
for i in normal_salary:
    total_salary=list(map(lambda x:x(i),functions))
    print(total_salary)
    
print("----------------------------------------------------")