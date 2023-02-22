"""single level inheritance"""
class company:
    wfh=2
    wfo=3
    def __init__(self,name,location,salary):
        self.name=name
        self.location=location
        self.salary=salary
        print(f"name is {self.name}\nlocated at {self.location}\nsalary{self.salary}")

    @classmethod
    def change_option(cls,wfh,wfo):
        cls.wfh=wfh
        cls.wfo=wfo
    @staticmethod
    def greeting():
        print("this is good company")

class employee(company):
    def __init__(self,name,location,salary,leaves,level):
        self.name=name
        self.location=location
        self.salary=salary
        self.leaves=leaves
        self.level=level
        print(f"name is {self.name}\nlocated at {self.location}\nsalary{self.salary}\nleaves is{self.leaves}\nlevel is{self.level}")

    @staticmethod
    def greeting():
        print("he is a good employee")

emp1=employee("mahesh","bangalore",40000,3,6)
print("\n")
emp2=employee("manohar","marathalli",40000,4,7)
print("\n")
emp1.greeting()
#emp2.company.greetin()
emp2=company("manohar","marathalli",40000)
emp2.greeting()
print("brfore changig")
print(company.wfh)
print(company.wfo)
emp2.change_option=7,8
print("after changig")
print(company.wfh)
print(company.wfo)
