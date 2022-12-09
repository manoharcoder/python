"""FUNCTION"""
#function is group  of a reapeted statements that performs a group of reapted statements 
# help us devide a large program in to smaller chunks
#s/y =function_name():

''' function without any arguments'''

# def greet():             #need to create a function before call it 
#     print("hello")
#     print("hi")
# greet()                   # we must need to call function 
# print("---------")
# greet()
# print("---------")
# greet()                  # we can call no.of times same function
# print("---------")       

''' function with arguments''' 
# passing values to the function  are called it as argument to tehe function

''' passing one argument'''

# def greet(name):             # function with one argument
#     print("hello",name)
#     print("hi",name)
# greet("manu")                   # we must need to call function 
# print("---------")
# greet("mohan")
# print("---------")
# greet("madhu")                  # we can call no.of times same function
# print("---------")       

"""passing multiple arguments"""
# def addnum(n1,n2):
#     sum=n1+n2
#     print("summof the two nubers ",sum)

# num1=2
# num2=5.5
# addnum(num1,num2)

"""return value or using return statement in function"""

# def addnum(n1,n2):
#     sum=n1+n2
#     return sum

# num1=2
# num2=5.5
# total=addnum(num1,num2)
# print("summof the two nubers is :: ",total)

#return use case
# def greet(name):
#     print("hello",name)
#     return                 # return terminate function entirly
#     print(hi,name)
# greet("jack")

'''using yield case and next()'''

    # yield pauses function save ourprevous progress
 

# def addnum():
#     num1=2
#     num2=5.5
#     sum=num1+num2
#     yield sum
#     n1=10
#     n2=10
#     sum2=n1+n2
#     yield sum2

# total=addnum()
# print("summof the two nubers is :: ",next(total))
# print("summof the two nubers is :: ",next(total))







'''#program13.py #aneesh sir  '''
 
# def greeting(name,salary):
#     print("hello good morning your salary is credited ",name,"\nyour salary is credited ",salary)
# greeting("manu", 20000)
# greeting("balagopal",23000)
# greeting("mohan", 20000)
# greeting("vanugopal",23000)

# def grossamount(name,slary,bonus):
#     print("hi",name)
#     gross=slary+bonus
#     return gross

# for i in range(5):
#     name=input("enter name of the employe;;")
#     salary=int(input("enter salaryof the employe;;"))
#     bonus=int(input("enter bonus amount of the employe;;"))
#     totalgross=grossamount(name,salary,bonus)
#     print(f"gross amount is{totalgross}")

# #len() and sum()functions
# marks=[1,2,3,4,5,6,7,8,9,10]
# print(len(marks))
# total=sum(marks)
# print("sum of list items is ::",total)

# function to find out average marks and grade them 

def find_avg_marks(marks):
    sum_of_marks=sum(marks)
    length_subjects=len(marks)
    avg_marks=sum_of_marks/length_subjects
    return avg_marks
def compute_grades(avg_marks):
    if avg_marks>=80:
        grade="A"
    if avg_marks>=60:
        grade="B"
    if avg_marks>580:
        grade="C"
    else:
        grade="F"        
    return grade


marks=[55,64,75,80,34]
average_marks=find_avg_marks(marks)
print("your average marks is ::",average_marks)
your_grade=compute_grades(average_marks)
print("your grade is ::",your_grade)
