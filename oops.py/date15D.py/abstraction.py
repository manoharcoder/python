from abc import ABC,abstractmethod
class Ria(ABC):
    location="marthahalli"
    @abstractmethod
    def java_course (self):
        pass
    @abstractmethod
    def python_course (self):
        pass
    @abstractmethod
    def devops_course (self):
        pass
    @abstractmethod
    def c_course (self):
        pass
    @abstractmethod
    def spoken_english_course (self):
        pass

class Candidate(Ria):
    def __init__(self,name,email,course,duration,fees):
        self.name=name
        self.email=email
        self.course=course
        self.duration=duration
        self.fees=fees


    def java_course(self):
        print(f"candidate name {self.name} email is {self.email}")
        print(f"your course is {self.course} and fee is {self.fees} and duration is {self.duration}")
        return super().java_course() 

    def python_course(self):
        print(f"candidate name {self.name} email is {self.email}")
        print(f"your course is {self.course} and fee is {self.fees} and duration is {self.duration}")
        return super().python_course()    

    def devops_course(self):
        print(f"candidate name {self.name} email is {self.email}")
        print(f"your course is {self.course} and fee is {self.fees} and duration is {self.duration}")
        return super().devops_course() 

    def c_course(self):
        print(f"candidate name {self.name} email is {self.email}")
        print(f"your course is {self.course} and fee is {self.fees} and duration is {self.duration}")
        return super().c_course() 

    def spoken_english_course(self):
        print(f"candidate name {self.name} email is {self.email}")
        print(f"your course is {self.course} and fee is {self.fees} and duration is {self.duration}")
        return super().spoken_english_course() 

    def __add__(self,other):
        return self.fees+other.fees

obj1=Candidate("mahesh","y.mahesh@gmail","python",4,29500)
obj1.python_course()
obj2=Candidate("manohar","manohar@gmail","java","4months",30000)
obj2.java_course()
print(obj1+obj2)