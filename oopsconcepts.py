#oops 
#class is a blue print of the object
# we can create many objects(houses,students) from sinle class(its blue prints )
#think of class as blue print of the house or student it contains all the details of the house  about the floors,door,window,
#(name,marks,grade) based on the description we build the house
# when we work with the objects we call variablea as attributes and functions are called as methods
"""DEFINING CLASS ,ITS OBJECTS ,ADD ATTRIBUTES WITH OBJ INSTANCES"""
# class Student():      # class is blue print of the student 
#     pass
# student1=Student()            # we can create a n.of students from single class
# student2=Student()
# student3=Student()            # creating no.of objects from single Student class

# student1.name="harry"
# student2.name="manu"          #now adding  different attributes to the  object instances
# student3.name="manohar"

# student1.age=22               # now successfully added 2 attributes to the student class
# student2.age=23
# student3.age=24
# print(student1.name,student1.age)
# print(student2.name,student2.age)
# print(student3.name,student3.age)
print("-----------------------")
# class Employee():
#     pass
# obj1=Employee()
# print(obj1)
print("-------------------")
# class Employee():
#     stars=5
# obj1=Employee()
# obj2=Employee()
# print(obj1.stars)
# print(obj2.stars)

# obj1.employename="manu"
# obj1.salary=100000
# print(obj1.employename,obj1.salary)
# #print(obj2.employename,obj2.salary)  AttributeError: 'Employee' object has no attribute 'employename'

print("-------------------------------------------------")

"""METHODS INSIDE A CLASS & AND CREATE A PROPER WAY ATTRIBUTES"""
# class Student():                         # Class
#     def check_pass_fail (self):          # method (functions) in side a Class  and method argument is self heare 
#         if self.marks>40:                #
#             return True
#         else:
#             return False
# student1=Student()                       #student1 is object for the Student class
# student1.name="manu"                     #attributes(variables)
# student1.marks=50
# did_pass=student1.check_pass_fail()      # caling method using object & without args
# print(did_pass)
print("-----------------------------------------------------------------------")
# class Employee():   # Employee is a class name and it should starts with cpitals only 

#     star=5                      # strs,institute,locationa are be the class variables
#     institute="RIA"               # can be access by the any object if the same class only
#     location='mrathahalli'
    
    
#     def institutedetails (self):    # it is a method of the calss Employee
#         print(f"institute name is {self.institute}\ni will give {self.star} stars\nand it is located at {self.location}")
    
#      # it will having self as a default positional arguments
#      #using self we can  iterate cl
#      # ass variables 

#     #def greeting():                     #TypeError: Employee.greeting() takes 0 positional arguments but 1 was given
#       #  print("hi good morning to all")   # heare selfe acts as 1 positional argument

# akash=Employee()        # akash is a object to the employee class
# akash.institutedetails()
# # akash.greeting()
# print("")
# print("before changing location",akash.location)  
                                                 
# akash.location="banglore"                         # there we are changing the instance variable and it
#                                                    #applies only for akash obj  and ot change the class variable location
# print("after changing instance variable : location")
# print("")
# print("after changing location",akash.location)
# print("")
# akash.institutedetails()
# print("")
# print("_____________________________")

# bhanu=Employee()
# bhanu.institutedetails()
# print("")
# print("after changing instance variable : stars ")
# print("")
# bhanu.star=4
# bhanu.institutedetails()

print("------------------------------------------------------------------------")
# class friends():
#     stars=5
    
# manohar=friends()
# mahesh=friends()

# manohar.name="MANOHAR"
# mahesh.name="MAHESH"
# manohar.age=23
# mahesh.age=22

# print(manohar.name,mahesh.name)
# print(manohar.age,mahesh.age)
# print(friends.__dict__)           #{'__module__': '__main__', 'stars': 5, '__dict__': <attribute '__dict__' of 'friends' objects>, '__weakref__': <attribute '__weakref__' of 'friends' objects>,
# print(manohar.__dict__)           #{'name': 'MANOHAR', 'age': 23}
# print(mahesh.__dict__)            #{'name': 'MAHESH', 'age': 22}
print("-----------------------------------------------------------------------")
"""python class and objects"""
# class Bike:
#     name=""
#     gear=0
# bike1=Bike()

# bike1.gear=11
# bike1.name="mountain bike"

# print(f"name {bike1.name},gear:{bike1.gear}")
print("-----------------------------------------------------------------------")
"""create a multiple objects of the python class"""
# class Employee:
#   employee_id=0

# employee1=Employee()
# employee2=Employee()

# employee1.employee_id=1001
# print("employe id is ",employee1.employee_id)

# employee2.employee_id=1002
# print("employe id is ",employee2.employee_id)
print("-----------------------------------------------------------------------")

"""python methods"""
# class Room:
#   length=0
#   breadth=0
#   def room_area(self):
#     print("area of the room is ::",self.length*self.length)

# room1=Room()
# room1.length=40.5
# room1.breadth=30.5

# room1.room_area()
print("-----------------------------------------------------------------------")
"""python constructor"""
# in the first starting we assign a deafult value to the class attributes
# by using the constuctor we can also initialize values

# class Car():
#   name=""
# #create a obj
# car1=Car()

# class Car():
#   # constructor function
#   def __init__(self,name):  # it is a constuctor func that is called whenever a new obj of the class is instantiated
#     self.name=name
#     print("i am a constuctor i can intialize values first whenevr obj calls")
# car1=Car("TATA CAR")
print("-----------------------------------------------------------------------")
# check pass fail student  using class ,init methods

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print(" set the values by using the constructor ")
#     def check_pass_fail (self):
#         if self.marks>=40:
#             return "student pass"
#         else:
#             return "student fail"

# student1=Student("manu",55)
# student2=Student("madhan",35)
# print(student1.name,student1.check_pass_fail())
# print(student2.name,student2.check_pass_fail())
print("-----------------------------------------------------------------------")
# class Whatsapp():
#     appname="whatsapp"
#     mobiletype="android"
#     def __init__(self,username,usergamil,userpasword):
#         self.username=username
#         self.usergmail=usergamil
#         self.userpasword=userpasword
#         print("intialization done!")
#     def userdetails(self):
#         worning="dont share your pasword to anyone !!!"
#         print(f"username is {self.username}\nuser gamil is {self.usergmail}\nand use pasword{self.userpasword}")
#         print(worning)

# user1=Whatsapp("pavan","pavanreddy1234@gmail.com","********")
# print("\n")
# user2=Whatsapp("narsareddy","narsa.narsa@gmail.com","******")
# user1.userdetails()
# print("\n")
# user2.userdetails()
# print(user1.__dict__)  #{'username': 'pavan', 'usergmail': 'pavanreddy1234@gmail.com', 'userpasword': '********'}

print("-----------------------------------------------------------------------")

# class Employee():
#     def __init__(self,ename,eage,esalary,erole):
#         self.ename=ename
#         self.eage=eage
#         self.esalary=esalary
#         self.erole=erole
#     def employee_details(self):
#         company_name ="TATA"
#         print(f"employe name is ::{self.ename}\nemployee age is ::{self.eage}\nemployee salary is ::{self.esalary}\nemployee role is ::{self.erole}")
#         print(f"\nemployee working in the {company_name} company ")

# employee1=Employee("manohar",25,30000,"developing role")
# employee2=Employee("manoj",22,15000,"frontend developer role")

# employee1.employee_details()
# print("\n")
# employee2.employee_details()

print("-----------------------------------------------------------------------")
# class Triangle():
#     def __init__(self,sidea,sideb,sidec):
#         self.sideA=sidea
#         self.sideB=sideb
#         self.sidec=sidec
#     def find_peremeter(self):
#         perimeter=self.sideA+self.sideB+self.sidec
#         return perimeter

# triangle=Triangle(5,4,3)
# print(triangle.find_peremeter())
print("-------------------------------------------------------------------------")
# add two complex numbers manully
# class Complex():
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
#     def adding(self,number):
#         real=self.real+number.real
#         imag=self.imag+number.imag
#         result=Complex(real,imag)
#         return result

# n1=Complex(5,6)
# n2=Complex(-4,2)
# result=n1.adding(n2)
# print("real=",result.real)
# print("imag=",result.imag)

print("--------------------------------------------------------------------------")
"""@classmethod,@staticmethod"""
'''@classmethod'''
#1).classmethod is going to take cls as self argument it it can be passed other arguments as well like (cls,arg1,arg2,....)
#2).when we call @classmethod to change the class level variables .it is going to change the variables of class  as well in below program
'''@staticmethod'''
#1).staticmethod is class level methods  which is not related with obj of the class  without creating obj we can call atatic method 

# class Employee():
#     company="T C S"
#     def __init__(self,ename,eage,esalary,erole):
#         self.ename=ename
#         self.eage=eage
#         self.esalary=esalary
#         self.erole=erole

#     def employee_details(self):
#         print(f"employe name is ::{self.ename}\nemployee age is ::{self.eage}\nemployee salary is ::{self.esalary}\nemployee role is ::{self.erole}")
#         print("now he changed his working company::",self.company)

#     @staticmethod
#     def greeting():
#         print("a lot of thank for doing good work")

#     @classmethod
#     def change_company(cls,company):
#         cls.company=company

# emp1=Employee("kowsik",30,30000,"web desiging")
# emp2=Employee("jagan",33,50000,"executing manager")

# emp1.employee_details()
# print()
# emp1.greeting()
# print("\n")
# emp2.employee_details()
# print()
# emp2.greeting()

# # changing company name for emp2 it will also change for emp1 in @classmethod 
# print("before changing company name for emp2")
# emp1.employee_details()
# print()
# emp2.employee_details()
# print()
# emp2.change_company("WIPRO")
# print()
# print("after changing company name for emp2")
# print()
# emp1.employee_details()
# print()
# emp2.employee_details()
# print()

# #@staticmethod can access by classname.classvariables  or objname.itsclassvariable 
# emp1.greeting()
# Employee.greeting()

print("----------------------------------------------------------------------------------------")
# class Zoo():
#     no_of_animals=100
#     def __init__(self,name):
#         self.name=name
#     def printdetails(self):
#         print(f"zoo name is {self.name}\nand {self.no_of_animals} animals are there")
#     @classmethod
#     def changeanimalcount(cls,count):
#         cls.no_of_animals=count
#     @staticmethod
#     def totalanimalcount():
#         total_animals=120
#         print("total no.of animals in the zoo is ",total_animals)

# zoo1=Zoo("nehruzoopark")
# print(zoo1.name)
# print(zoo1.no_of_animals)
# print(zoo1.totalanimalcount())
# zoo1.printdetails()
# print()
# zoo1.changeanimalcount(150)
# zoo1.printdetails()
# print()

# zoo1=Zoo("gandhipark")
# zoo1.no_of_animals=200
# zoo1.printdetails()

print('------------------------------------------------------------------------------------------------------')
"""single level inheritance"""

# class Employee():
#     wfh=2
#     wfo=3
#     def __init__(self,name,skills,rolematch,department,salary):
#         self.ename=name
#         self.skils=skills
    #     self.rolematch=rolematch
    #     self.department=department
    #     self.salary=salary

    # def employee_details(self):
    #     print(f"employe name is ::{self.ename}\nemployee skills are ::{self.skills}\nemployee role  is ::{self.rolematch}\nemployee department  is ::{self.department}")
    #     print("\nemploye salary is ",self.salary)
    # @classmethod
    # def hybridworkinfgpays(cls,wfh,wfo):
    #     cls.wfh=wfh
    #     cls.wfo=wfo


# class Prents():
#     hair_colour="black"
#     def __init__(self,name,height,skin_colour,bloodgroup):
#         self.name=name
#         self.height=height
#         self.skin_colour=skin_colour
#         self.bloodgroup=bloodgroup

#     def parent_details(self):
#         print(f"parent  name is ::{self.name}\nparents skin colour is ::{self.skin_colour}\nparents height is ::{self.height}\nparents bloodgroup  is ::{self.bloodgroup}")
#     @staticmethod
#     def Prgreeting():
#         print(" we are parents ") 
# class Childs(Prents):
#     hair_colour="brown"
#     def __init__(self,name,height,skin_colour,bloodgroup,age):
#         self.name=name
#         self.height=height
#         self.skin_colour=skin_colour
#         self.bloodgroup=bloodgroup
#         self.age=age

#     def child_details(self):
#         print(f"child  name is ::{self.name}\nchild skin colour is ::{self.skin_colour}\nchild height is ::{self.height}\nchild bloodgroup  is ::{self.bloodgroup}\n child age is {self.age}")
#     @staticmethod
#     def Chgreeting():
#         print(" we are childs ") 

# child1=Childs("mohan",5.5,"white","B+",25)
# child1.child_details()
# child1.Chgreeting()
# child1.parent_details()
# child1.Prgreeting()

"""multilevel inheritance"""

# class A():
#     aa="AA"
#     def a(self):
#        print("i am class A")
#     pass
# class B(A):
#     bb="BB"
#     def b (self):
#        print("i am class B")
#     pass
# class C(B):
#     cc="CC"
#     def c(self):
#        print("i am class C")
#     pass
# class D(C):
#     dd="DD"
#     def d(self):
#        print("i am class D")
#     pass

# obj1=D()
# print(obj1.aa,obj1.bb,obj1.cc,obj1.dd)
# obj1.a()
# obj1.b()
# obj1.c()
# obj1.d()

# print(D.mro())      #[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# print(D.__mro__)     #(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
#                     ## mro -- method resolution order
#                      # MRO classes can be viewed as __mro__ attribute or the mro()method .thr former returns a tuple while the later returns a list

# print(issubclass(str,object))   # true
# print(isinstance(5.5,object))   # true 
# print(isinstance("hello",object))  # true 

# #demonstration of MRO
# class A:
#     pass
# class B:
#     pass
# class C:
#     pass
# class D(A,B):
#     pass
# class E(B,C):
#     pass
# class M(E,D,C):
#     pass
# print(M.mro())  #[<class '__main__.M'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]        
 
# multiple inheritance
# class India():
#     states=["karnataka","ap","up","tn","kashmir"]
#     def indiadetails(self):
#         print("india states are ::",self.states)
# class karnataka(India):
#     districts=["chickabalapur","manguluru","jamkur","banglore urban"]
#     def karnatakadetails(self):
#         print("karnataka didstricts are ::",self.districts)
# class banglore(karnataka):
#     wards=["chmrajpet","hebbal","marthahalli","devanhali"]
#     def bangloredetails(self):
#         print(" banglore wards are ::",self.wards)
# class marthahalli(banglore):
#     institutename=["ria","jspider","qspider"]
#     def institutedetails(self):
#         print("institutes in marthahalli are::",self.institutename)
# obj1=marthahalli()
# obj1.institutedetails()
# obj1.bangloredetails()
# obj1.karnatakadetails()
# obj1.indiadetails()
# print(obj1.states)

"""multiple inheritance"""
# inherit the 2 or more classes in to the one class is clalled as mutiple inheritance
#for passing the values to the init method we must create obj for inherited class 
# while assining the variables to the init method frist priority is inhirted class only next priority is frist inhirted classthen for nest one 
# class Bestfriend:
#     stars=10
#     def __init__(self,bname,bage,bheight,bhobby):
#         self.bname=bname
#         self.bage=bage
#         self.bheight=bheight
#         self.bhobby=bhobby
#         print("setting  values for bestie  was done ")
#     def bestiedetils(self):
#         print(f"my best friend name is ::{self.bname}\nand his age is ::{self.bage} \nhis height is ::{self.bheight}\nand his hobbies ::{self.bhobby}")

# class Memories:
#     place=" benguluru karnatka"
#     def __init__(self,placename,item,taste):
#         self.placename=placename
#         self.item=item
#         self.taste=taste
#         print("i have set the values for memories too")
#     def printmemories(self):
#         print(f"\nwe went to {self.place} \nrestarent name is { self.placename} \nwe ate {self.item}\ntaste as {self.taste}")
#     @staticmethod
#     def message():
#         return "hello"

# class Racing(Bestfriend,Memories):    ##priorities --->  for  a(b,c,d) is  1-->a  2--->b  3--->c  4--->d
#     place="NS HIGHIWAY"
#     def racing(self):
#         return f"\n\nwhile comming back we have a racing at{self.place}"

# rohan=Bestfriend("rohan",22,5.3,"[reading,riding]")
# rohan.bestiedetils()

# rohan_memories=Memories("courner house","cake fudge","awesome")
# rohan_memories.printmemories()

# rohan_race=Racing("rohan",22,5.3,"[reading,riding]")

# #rohan_race.printmemories()
# rohan_race.bestiedetils()
# print(rohan_race.message())
# print(rohan_race.racing())


# class Animal():
#     AAname="animal"
#     def __init__(self,Aname,Atype):
#         self.Aname=Aname
#         self.Atype=Atype
#     def Animaldetails(self):
#         print(f"animal name is {self.Aname}\nand animal type is {self.Atype}")
    
# class Bird():
#     BBname="Bird"
#     def __init__(self,Bname,Btype,Bspan):
#         self.Bname=Bname
#         self.Btype=Btype
#         self.Bspan=Bspan
#     def Birddetails(self):
#         print(f"bird name is ::{self.Bname}\nand bird type is ::{self.Btype}\nand also its span of life is ::{self.Bspan}")
#     def tell(self):
#         print(" i am telling i am belongs to Bird class only")

# class Nature(Animal,Bird):
#     NNname="Nature"
#     def __init__(self,Ntype,Nweather,Nplacename):
#         self.Ntype=Ntype
#         self.Nweather=Nweather
#         self.Nplacename=Nplacename
#     def naturedetails(self):
#         print(f"this is beautifull ::{self.NNname}\nweather is so ::{self.Nweather}\nnature type is ::{self.Ntype}\nnature place is:: {self.Nplacename}")

# class Nature1(Bird,Animal):
#     Nname1="nature1"
#     def naturedetails(self):
#         print(f'this is a beautifull {self.Nname1}')

# objn=Nature("cloudy","cool","hills")
# objn.naturedetails()

# obja=Animal("tiger","wild animals")
# obja.Animaldetails()

# objb=Nature1("parrot","herbivious",15)
# objb.Birddetails()

# # obja=Nature("tiger","wild animals")  #TypeError: Nature.__init__() missing 1 required positional argument: 'Nplacename
# # obja.Animaldetails()                  #if  we have constructor in main inherited class then it only allowes for passing variavbles of the same class only


# objaAv=Nature1("parrot","herbivious",15)
# # print(objaAv.NNname)
# print(objaAv.AAname)  ## before accesing its variables or attributes we need to intialize constructor
# print(objaAv.BBname)

"""public,private,protect variables"""
# class Family:
#     no_of_peoples=8 # public
#     _siblings=4     #protect
#     __sons=2        #private

# class Another(Family):
#     mans=3
#     _womens=2
#     __childs=4
#     pass
# print("accessing the class family variables with same class obj1")
# obj1=Family()
# print(obj1.no_of_peoples)
# print(obj1._siblings)    # for protected variables need to use singledunder variable name
# print(obj1._Family__sons) # for private variables need to use single dunder class doubble dunder variabblename
# print("accessing the another class variables with same class obj2")
# obj2=Another()
# print(obj2.mans)
# print(obj2._womens)
# print(obj2._Another__childs)
# print("accessing the family vlass variables with another class obj3")
# obj3=Another()
# print(obj3.no_of_peoples)
# print(obj3._siblings)
# print(obj3._Family__sons)

"""over_riding"""
# giving the same name for methods in a inherited clases or multilevel inherited classes i scalled method overriding
# class Employee():                               #3rd priority of methods of same name in the class
#     def printdetails(self):
#         print(" i am class employee details ::")
#     pass
# class Student(Employee):                         #2nd priority of methods of same name in the class
#     def printdetails(self):
#         print("i am belogs to class student ")
#     pass
# class Child(Student):                             #1st priority of methods of same name in the class
#     def printdetails(self):
#        print('i am belongs to child class')
#     pass
# childobj=Child()
# childobj.printdetails()
# studentobj=Student()
# studentobj.printdetails()

"""super()method"""
#super method gives its frist priority to the  parent class only those also belongs to __init__but not class variables
# class A():
#     message="hello i am class a variable"
#     def __init__(self):
#         self.title="python fulll stack"
#         self.instance="class A instances"  # creating a class instances variables
# class B(A):
#     message="hello i am class b variable"
#     def __init__(self):
#         self.title="i am a  python fulll stack developer "
#         self.instance="class B instances"
#         super().__init__()

# obj=B()
# print(obj.instance)   #class A instances  # we use super().__init__()
# print(obj.title)      #python fulll stack  #we use super().__init__()
# print(obj.message)    #hello i am class b variable

# obj1=A()
# print(obj1.instance)   
# print(obj1.title)      
# print(obj1.message)    

"""pendinig today:: overloading,dunder,abstraction oops 14,15,16"""
# class Employee():
#     no_of_leaves=14
#     def __init__(self,name,salary,role,phone,age):
#         self.name=name
#         self.salary=salary
#         self.sole=role
#         self.phone=phone
#         self.age=age

#     def printdetails(self):
#         print(f"employee name is ::{self.name}\nemployee slary is ::{self.salary}\nemployee role is ::{self.sole}\nemployee phone number is ::{self.phone}\nemployee age is ::{self.age}")

#     @classmethod
#     def changeleaves(cls,number):
#         cls.no_of_leaves=number
     
#     @staticmethod
#     def greeting():
#         print(" i am static method of employee class ")
    
#     def __add__(emp1,emp2):
#         return emp1.salary+emp2.salary,emp1.age+emp2.age

#     def __sub__(self,other):
#         return self.salary-other.salary,emp1.age-emp2.age
    
#     def __mul__(emp1,emp2):
#         return emp1.salary*emp2.salary,emp1.age*emp2.age
    
#     def __truediv__(emp1,emp2):
#         return emp1.salary/emp2.salary,emp1.age/emp2.age
    
#     def __floordiv__(emp1,emp2):
#         return emp1.salary//emp2.salary,emp1.age//emp2.age
   
#     def __str__(self):
#         return print(f"employee name is ::{self.name}\nemployee slary is ::{self.salary}\nemployee role is ::{self.sole}\nemployee phone number is ::{self.phone}\nemployee age is ::{self.age}")
    
#     def __repr__(self):
#         return print(f"employee name is ::{self.name}\nemployee slary is ::{self.salary}\nemployee role is ::{self.sole}\nemployee phone number is ::{self.phone}\nemployee age is ::{self.age}")
    
#     @staticmethod
#     def company():
#         print(" i am company accenture ")
    

# emp1=Employee("maheah",500000,"developer",9375296378,22)
# emp2=Employee("manesh",600000,"web_developer",96454965789,25)
# emp1.__str__()
# emp2.__repr__()
# emp1.printdetails()
# emp2.printdetails()

# print(emp1+emp2)
# print(emp1-emp2)
# print(emp1/emp2)
# print(emp1//emp2)
# print(emp1*emp2)

# Employee.company()
# print(Employee.no_of_leaves)
# Employee.no_of_leaves=30
# print(Employee.no_of_leaves)
# emp1.changeleaves(45)
# print(Employee.no_of_leaves)

"""magic or dunder methods"""
#magic methods in python are the special methods that starts and end with the double underscores.they also calles as magic methods
#magic methods are not meant to be invoked directly by you ,but the invocation happens internally from the class on a certain action
## __int__,float,complex,round,trunc,ceil,floor
# class Dunderexamples():
#     def __init__(self,n1,n2,n3,n4):
#         self.n1=n1
#         self.n2=n2
#         self.n3=n3
#         self.n4=n4
#     def __repr__(self):
#         return (f"1:{self.n1}\n2:{self.n2}\n3:{self.n3}\n4:{self.n4}")
#     def __str__(self):
#         return (f"1:{self.n1}\n2:{self.n2}\n3:{self.n3}\n4:{self.n4}")
#     def __int__(self):
#         return self.n4
#     def __float__(self):
#         return self.n1
#     def __complex__(self):
#         return self.n2
#     def __round__(self):
#         return self.n4
#     def __trunc__(self):
#         return self.n1
#     def __ceil__(self):
#         return self.n2
#     def __floor__(self):
#         return self.n2
# obj1=Dunderexamples(30,40,40,4.4)
# print(obj1)
# print(obj1.__int__())
# print(obj1.__float__())
# print(obj1.__complex__())
# print(obj1.__round__())
# print(obj1.__trunc__())
# print(obj1.__ceil__())
# print(obj1.__floor__())
"""abstract classes"""
# hinding the internal properties of the function or class 
# we can't create a object for obstract class  and obstract methods will be decleared with @ obstractmethod 
#if you want to work with obstract methods then inherit the proprties of obstract claases in to another class 
#we must to create methods in inheitied class that should grater than or equal to the abstract methods with same name .
print("_______________________--------------------------------------________________________________")
from abc import ABC,abstractmethod
class Smartphone(ABC):  # this is abstract method 
    mobile_name="poco"
    @abstractmethod
    def camera(self):
        pass
    @abstractmethod
    def mediaplayer(self):
        pass
    @abstractmethod
    def whatsapp(self):
        pass
    @abstractmethod
    def instagram(self):
        pass
    def weather_app(self):
        print("today the weather is so sunny::")
class Phone(Smartphone):
    def __init__(self,contacts,messages,notes):
        self.contacts=contacts
        self.messages=messages
        self.notes=notes
    def camera(self):
        print("on the camera",self.notes)
    
    def mediaplayer(self):
        print("play music")

    def whatsapp(self):
        print("send message")
    
    def instagram(self):
        print("instagram reals are so likable")
    
    def weather_app(self):
        return super().weather_app()

obj1=Phone("ria","send message to ria","fullstack")
obj1.camera()
print(obj1.contacts)
obj1.instagram()
print(obj1.mobile_name)

print("_______________________--------------------------------------________________________________")
# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def __init__(self,name="manu",age=20):
#         self.name=name
#         self.age=age
#         print(f"name is {self.name}, age is {self.age}")
#     @abstractmethod
#     def mandatory (self):
#         print(" i am abstract mandatory method")
#     @abstractmethod
#     def greeting(self):
#         print(" i am obstract greeting")
#     @abstractmethod
#     def other(self):
#         print(" i am other ")
# class B(A):
#     def __init__(self,name="maohar",age=22):
#         # super().__init__()       # first one A init excutes
#         self.name=name
#         # super().__init__()      #first one A init excutes
#         self.age=age
#         # super().__init__()   # if we declear with same variables then previous variables comes to this variables places  A,B
#         print(f"name is {self.name}, age is {self.age}")
#         super().__init__()     #  A init excecutes after B init
#     def mandatory(self):
#         #print("i am imorted abstract class mandatory methhod")
#         return super().mandatory()
#     def greeting(self):
#         print(" i am imported abstract class  greeting method ")
#         return super().greeting()
#     def other(self):
#         print(" i am imported abstract class other method ")
#         return super().other()
#     def another(self):
#         print(" i am belogs to another method in a imorted abstract class ")

# obj=B()
# obj.other()
# obj.greeting()
# obj.mandatory()
# obj.another()
print("_________-----------------_________________________________")

# from abc import ABC,abstractmethod
# class Ria(ABC):
#     location="marthahalli"
#     @abstractmethod
#     def full_stack (self):
#         print("it is a full stack details ::")
#     @abstractmethod
#     def python_course (self):
#         print("it is a python course details")
#     @abstractmethod
#     def java_course (self):
#         print("it is a java_course details ::")
#     @abstractmethod
#     def devops_course (self):
#         print("it is a devops_course details")
#     @abstractmethod
#     def sap_course (self):
#         print("it is a sap course details")
# class  Candidate(Ria):
#     def __init__(self,cname,cemail,ccourse,cduration,cfees):
#         self.cname=cname
#         self.cemail=cemail
#         self.ccourse=ccourse
#         self.cduration=cduration
#         self.cfees=cfees

#     def candidatedetils(self):
#         print(f"candidate name is ::{self.cname}\ncandidate email is ::{self.cemail}\ncandidate course is ::{self.ccourse}\ncandidate course duration is ::{self.cduration}\nand course fees is ::{self.cfees}")
    
#     def full_stack (self):
#         print(f"candidate name is ::{self.cname}\ncandidate email is ::{self.cemail}\ncandidate course is ::{self.ccourse}\ncandidate course duration is ::{self.cduration}\nand course fees is ::{self.cfees}")
#         #super().full_stack()

#     def python_course (self):
#         print(f"candidate name is ::{self.cname}\ncandidate email is ::{self.cemail}\ncandidate course is ::{self.ccourse}\ncandidate course duration is ::{self.cduration}\nand course fees is ::{self.cfees}")
#         print("it is a python course details")

#     def java_course (self):
#         print(f"candidate name is ::{self.cname}\ncandidate email is ::{self.cemail}\ncandidate course is ::{self.ccourse}\ncandidate course duration is ::{self.cduration}\nand course fees is ::{self.cfees}")
#         print("it is a java_course details ::")
   
#     def devops_course (self):
#         print(f"candidate name is ::{self.cname}\ncandidate email is ::{self.cemail}\ncandidate course is ::{self.ccourse}\ncandidate course duration is ::{self.cduration}\nand course fees is ::{self.cfees}")
#         print("it is a devops_course details")
   
#     def sap_course (self):
#         print(f"candidate name is ::{self.cname}\ncandidate email is ::{self.cemail}\ncandidate course is ::{self.ccourse}\ncandidate course duration is ::{self.cduration}\nand course fees is ::{self.cfees}")
#         print("it is a sap course details")
# student1=Candidate("manu","mANUnamsnaj@gmail.com","pythoncourse","4months",29500)
# student1.candidatedetils()
# student1.full_stack()

"""inspect,properties,setter,deleter,"""

# import inspect
# class Person:
#     pemail=""
#     def __init__(self,fname,lname):
#         print("intialization was happeneing")
#         self.fname=fname
#         print("fname was stored")
#         self.lname=lname
#         print("lname was stored")
#         self.email=f"{self.fname}.{self.lname}@gamil.com"  # before this line execute it excecutes setters will then  bz email was callable
#         self.pemail=self.email
#         print("intialization done")
    
#     def persondetails(self):
#         print(f"frist name is ::{self.fname}\nlast name is ::{self.lname}\nthe gmail is ::{self.fname}.{self.lname}@gamil.com")

#     @property
#     def email(self):
#         if self.fname==None  and self.lname==None:
#             print("fname and lname was not set at ,please set the values ")
#         else:
#             print("values are intialized in init method ")
    
#     @email.setter
#     def email(self,email):
#         print("values are setting")
#         fullname=email.split("@")[0]
#         self.fname=fullname.split(".")[0]
#         self.lname=fullname.split(".")[1]
#         print("values set")
#     # @email.getter
#     # def email(self):
#     #     print("getter values ",self.email)
    
#     @email.deleter
#     def email(self):
#         self.fname=None
#         self.lname=None
#         print("email was deleted  successfully ::")
    

# obj1=Person("manu","1999")
# obj1.persondetails()
# print(obj1.lname)
# print(obj1.fname)
# print(obj1.pemail)
# del obj1.email
# #del obj1    #NameError: name 'obj1' is not defined

# obj1.email="manohar.bogala12@email.com"
# obj1.persondetails()

# #print(inspect.getmembers_static(obj1)) # lot of data will be printed []













































