'''LAMBDA FUNCTION'''
#s/y variable= lambda value : opreationfor value
# def add(n1,n2):
#     return n1+n2
# print(add(1,2))

#lambda functions are single line functions are defined without a name they are aslso calles as anonymous functions
#take the input and it return the o/p as like def method with function as like above 

# add= lambda n1,n2 : n1+n2
# print(add(1,2))

"""MAP FUNCTION """
#s/y variable=list(map(function,iterable))
# map function that applys the function to each item of an iterable
# for single iterable lists 

# numbers=[1,2,3,4,5,6,7,8,9]
# square_num=[]
# square= lambda X :X**2                #this lambda function applicable for each item in list 
# for i in numbers:                     #we take for loop for iteratingthe list
#     square_num.append(square(i))
# print(square_num)


# to reduce code and langth we use map()
# numbers=[1,2,3,4,5,6,7,8,9]           # we must use list to convert map objects in to list from {map function return a iterable objects}
# squares=map(lambda x:x**2,numbers)    # map(heare lambda function,itearable list)
# print(list(squares))                  # lambda function takes X argument:and returns the square of that argument  simillarly 
#                                     # we applying this function to each element of the number
#
#for 2 or more list itrables use in case
# n1=[1,2,3,4,5,6,7,8,9]
# n2=[9,8,7,6,5,4,3,2,1]
# total=list(map(lambda x,y :x+y ,n1,n2))
# print(total)

#convert celcious to farhenheeit
# temps=[("berlin",29),("cairo",36),("buenos aires",19),("los angeles",26),("tokyo",27),("new york",28),("london",22),("beijing",32)]
# c_to_f=lambda data :(data[0],(9/5)*data[1]+32)
# print(list(map(c_to_f,temps)))

"""FILTER FUNCTION"""
# # #s/y variable=list(filter(function,iterable))
# #filter() s/y is same as map() ..however instead of creating a new iterator by applying the give function 
# #filter filter out the only elements the function return true 

# # filter out the odd numbers from thr list usimg filter function
# n1=[1,2,3,4,5,6,7,8,9]
# odd_num=list(filter(lambda a : a%2!=0,n1))  # heare filter filters the values those true for the given condition only
# print("odd num list is::",odd_num)

# select the valus which are grater than avg of data  use case of filter
# from statistics import mean as m
# data=[1.3,2.7,0.8,4.1,4.3,-0.1]
# avg=m(data)
# print(avg)

# g_avg=list(filter(lambda z : z>avg ,data))    #data>avg printed 
# print(g_avg)                           

# l_avg=list(filter(lambda z : z<avg ,data))    # data<avg will be printed 
# print(l_avg)


# # remove missing data  
# countries=["","argentina","","brazil","chile","","colombia","","equador","","","venezuela"]
# print(list(filter(None,countries)))   #"",0,0.0,0j,[],{},(),false,None, instances which signal they are empty

"""REDUCE FUNCTION"""
# in python 3+ reduce is not built in function moved to the 'functools' module
# python creator Guido van Rossum
#"use functools.reduce()" if you really need it ;
#however 99% of the time an explicit for loop  is more readable 

#no need of list to store o/p beacuse it not generate the iterable obj it only returns the int or float

"""data:[a1,a2,a3,........,an]
   function:f(x,y)
   
   reduce(f,data):
   step1:val1=f(a1,a2)
   step2:val2=f(vla1,a3)
   step3:val3=f(vla2,a4)
   .
   .
   .
   step(n-1):val(n-1)=f(vla(n-2),an)
   return val(n-1)
   
   alternatly:
   returns f(f(f(a1,a2),a3),a4),........an)"""
   
from functools import reduce as r
# multiply the all numbers in a list
data=[2,3,5,7,11,13,17,19,23,29]
mult= lambda x,y :x*y
print(r(mult,data))

mult= r(lambda x,y :x*y,data)
print(mult)
print(type(mult))








































