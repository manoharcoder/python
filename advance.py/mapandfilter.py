"""FILTER AND MAP FUNCTIONS ALONG WITH LAMBDA"""

# def add(n1,n2):
#     return n1+n2
# print(add(10,11))

# add=lambda n1,n2 :n1+n2
# print(add(10,11))
# must be function  name is same as name of lambda

"""map function()"""
# map() is used to apply a function to each element of an iterable

numbers=[1,2,3,4,5]
sqre_num=[]
sqnum= lambda n:n**2
for n in numbers:
    sqre_num.append(sqnum(n))
print(sqre_num)

# now lets use filter to apply it
# map  must be take two arguments(function,iterable)we first get map object(return a iterable obj)
#  we need to convert this iterable obj in to thelist to access


numbers=[1,2,3,4,5]
sqre_num=list(map(lambda n:n**2 ,numbers))
print(sqre_num)

# mutiple iterabke using map
n1=[1,2,3,4]
n2=[5,6,7,8]
rsum=list(map(lambda x,y:x+y, n1,n2))
print(rsum)

"""MAP FUNCTIONS"""
# filter filter outs the  elements for which the function returns true
num=[1,2,3,4,5,6,7,8,9]
evnum=list(filter(lambda x:x%2==0,num))
print(evnum)