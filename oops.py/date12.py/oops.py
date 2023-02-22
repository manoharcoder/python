'''class Employee:
    company="WIPRO"
    age=50
    def __init__(self,name,age,salary,role):
        self.name=name
        self.age=age
        self.salary=salary
        self.role=role
    def detail(self):
        
        print(f'employee name is{self.name}\nemployee age is{self.age}\nemployee salary is{self.salary},\nemployee role is{self.role}\ncompany name is {self.company}')
        #print(f"their experience is ::{self.exp}")
emp1=Employee("mahesh",23,2345,"coder")
emp2=Employee("manohar",22,2345,"programmer")
emp1.exp=1
emp1.detail()
print("\n")
emp2.detail()
print(emp1.exp)
print(emp1.age)
print(Employee.age)
print(Employee.__dict__)'''

# #2)

class friends():
    stars=5
    
manohar=friends()
mahesh=friends()

manohar.name="MANOHAR"
mahesh.name="MAHESH"
manohar.age=23
mahesh.age=22

print(manohar.name,mahesh.name)
print(manohar.age,mahesh.age)
print(friends.__dict__)           #{'__module__': '__main__', 'stars': 5, '__dict__': <attribute '__dict__' of 'friends' objects>, '__weakref__': <attribute '__weakref__' of 'friends' objects>,
print(manohar.__dict__)           #{'name': 'MANOHAR', 'age': 23}
print(mahesh.__dict__)            #{'name': 'MAHESH', 'age': 22}