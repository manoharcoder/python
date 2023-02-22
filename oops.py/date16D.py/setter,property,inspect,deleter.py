import inspect
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{self.fname}.{self.lname}@gmail.com"

    def printDetails(self):
        return f"the person first name&last name{self.fname}.{self.lname}"
    
    @property
    def email(self):
        if self.fname==None and self.lname==None:
            print("email is not set,pls set the email details")
        else:
            print("im setting email")
            return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,email):
        print("setting the propertys of email")
        fullname=email.split("@")[0]
        self.fname=fullname.split(".")[0]
        self.lname=fullname.split(".")[1]
        print("email is set")

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        print("email was susessfully deleted")

obj1=person("manu","1234")
print(obj1.printDetails())
print(obj1.email)
del obj1.email
print(obj1)    
person.email="manohar.1999@gmail.com"
print(person.email)
print(obj1.lname)
print(obj1.fname)
print(inspect.getmembers(obj1))