# iterable :: aything  that you can loop over in py is called aniterable 
#num=[1,2,3,4]
#in python an object which implements the __iter__() method is called an iterable

# num=[1,2,3,4,5]
# value=num.__iter__()

# print(next(value))
# print(next(value))

# num=[1,2]
# value=num.__iter__()
# item1=value.__next__()
# item2=value.__next__()
# item3=value.__next__()

# print(item1)
# print(item2)
# print(item3)


# num=[1,2]
# value=iter(num)
# item1=next(value)
# item2=next(value)
# #item3=next(value)

# print(item1)
# print(item2)
# #print(item3)

# num=[1,2,3,4]
# iter_obj=iter(num)
# while True:
#     try:
#         element=next(iter_obj)
#         print(element) 
#     except StopIteration:
#          break
# num=[1,2,3,4]
# for i in num:
#     print(i)

'''print only even numbers'''
# class even:
#     def __init__(self,max):
#         self.n=2
#         self.max=max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n<=self.max:
#             result=self.n
#             self.n+=2
#             return result
#         else:
#             raise StopIteration

# number=even(10)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))


# class powtwo:
#     def __init__(self,max):
#         self.n=0
#         self.max=max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n<=self.max:
#             result=2**self.n
#             self.n+=1
#             return result
#         else:
#             raise StopIteration

# number=powtwo(10)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))

# class powtwo:
#     def __init__(self,max):
#         self.max=max
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#         if self.n<=self.max:
#             result=2**self.n
#             self.n+=1
#             return result
#         else:
#             raise StopIteration

# '''# number=powtwo(10)
# # i=iter(number)
# # print(next(number))
# # print(next(number))
# # print(next(number))
# # print(next(number))
# # print(next(number))
# # print(next(number))
# # print(next(number))
# # print(next(number))'''

# for i in powtwo(5):
#     print(i)

""" infinite iterator"""
# print(int())  #0
# int=iter(int,1)  # iterator call this function until the returns value is equal to the sentinel
# print(next(int))
# print(next(int))
# print(next(int))


# class Infinite:
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#         result=self.n
#         self.n=self.n+2
#         return result

# # for i in Infinite():
# #     if i ==20:
# #         break
# #     print(i)

# a=iter(Infinite())
# print(next(a))
# print(next(a))









