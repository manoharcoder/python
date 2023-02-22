""" PYTHON DECORATOR """
# in python everything is object including classes as well as functions
# variables are identifiers bound to the objects 
# def inc(x):
#     return x+1

# def operate(func,x):
#     result=func(x)       # in py we can define or call function inside a function 
#     return result

# print(operate(inc, 3))

# def print_msg(message):
#     greeting="hello"
#     def printer():            # we can define a function inside of another function
#         print(greeting,message)
#     printer()                   

# print_msg("python is awesome")

""" function can also return another function as value """
"""clousers"""   ###; clousur is simply an inner function that remembers the values and variables 
 # in its enclosing scope  even if the outer function is done executing  


#when we call the func function we still have the access to message  and greeting variables in the inner printer function 
#  such a fuction is called as clouser
# def print_msg(message):
#     greeting="hello"
#     def printer():            # we can define a function inside of another function
#         print(greeting,message)
#     return printer              #function can also return another function as value      

# func=print_msg("python is awesome")
# #print(func)       #<function print_msg.<locals>.printer at 0x000001ABFA5704A0> error
# #func
# func()           # then only we can get o/p
print("-------------------------------------------------")

""" PYTHON DECORATOR """
# python decorator is a function that takes in a function ,adds some functionality to it  and then returns original function


# def printer():
#     print("hello world")
# def disply_info(func):
#     def inner():
#         print("executing",func.__name__,"function")
#         func()
#         print("finished execution")
#     return inner         # must be remove ()
# #printer()
# #disply_info_func(printer) # got o/P when no return on above functions 
# decorator_fun=disply_info(printer)
# decorator_fun()  # use when return on functions

print("----------------------------------------")
## another way to do it using @ 
# def disply_info(func):  # heare func value is assingned to printer function
#     def inner():
#         print("executing",func.__name__,"function")
#         func()    # heare it calls the printer funstions
#         print("finished execution")
#     return inner   
# @disply_info       #@ means we are passing below function as inupt to the disply_info functions
# def printer():
#     print("hello world")
# printer()

print("----------------------------------------")

# def printer():
#     print("hello world")
# def monitor():
#     print("hello welcome to the graphical world ")
# def game():
#     print(" hello welcome to the gaming world")
# def disply_info(func1,func2,func3):
#     def inner():
#         print("executing",func1.__name__,"function")
#         print("executing",func2.__name__,"function")
#         print("executing",func3.__name__,"function")
#         func1()
#         func2()
#         func3()
#         print("finished execution")
#     return inner         # must be remove ()
# decorator_fun=disply_info(printer,monitor,game)
# decorator_fun()  
print("----------------------------------------")

# def disply_info(func1,func2,func3):  
#     def inner():
#         print("executing",func1.__name__,"function")
#         print("executing",func2.__name__,"function")
#         print("executing",func3.__name__,"function")
#         func1()
#         func2()
#         func3()
#         print("finished execution")
#     return inner   
# @disply_info       #@ means we are passing below function as inupt to the disply_info functions
# def printer():
#     print("hello world")
# def monitor():
#     print("hello welcome to the graphical world ")
# def game():
#     print(" hello welcome to the gaming world")
# printer(func1)
# monitor(func2)
# game(func3)

print("---------------------------")

# def order(handlerequest):
#     def takeorder():
#         print("your order is saved in DB")
#         handlerequest(2345)
#         print("your order is placed")
#     return takeorder

# @order
# def handlerequest(id):
#     if id==2345:
#         print("sucsessful")
#     else:
#         print("order is failed")

# handlerequest()

# print("-----------------------------------------")

# def handlerequest(id):
#     print("handled reduest id ..")
#     if id==12345:
#         print("sucessfull")
#     else:
#         print("failed")

# def order(handlerequest):
#     def takeorder():
#         print("order details added sucessfully to the data base ")
# #         handlerequest(12345)
# #         print("your oder is placed")
# #     return takeorder
# # output=order(handlerequest)
# # output()

# """decorating functions with parameters """

# def decorate(devide):   # we can use same name (devide ) in side of decorator or may change to our convienve
#     def inner(m,n):
#         print("deviding",m,"by",n)
#         if n==0:
#             print("number 0 cann't  used devision ")
#             return
#         return devide(m,n)      # must call with what name that you are passing in to decorato
#         # in which possition that we are calling it at that place only we got o/p i mean we decorate it 
#     return inner
# @decorate
# def devide(m,n):
#     return m/n

# val=devide(5,3)
# print(val)
# val2=devide(5,5)
# print(val2)
# va3=devide(5,0)
# print(va3)

# def mult():
#     print("hi")

# def sample_div(func):
#     def inner():
#         print("dont multiply with zero")
#         func()
#         print("we got o/p")
#     return inner

# result=sample_div(mult)
# result()

"""CHANGING DECORATORS IN PYTHON"""
# in py function can decorate multiple times with different or the same decorator
def star (func):
    def inner(args):
        print("*"*30)
        func(args)
        print("*"*30)
    return inner
def percent (func):
    def inner(args):
        print("%"*30)
        func(args)
        print("%"*30)
    return inner
@star
@percent
def printer(msg):
    print(msg)

printer("decorators are wounderful")