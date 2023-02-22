class Dunderexamples():
    def __init__(self,n1,n2,n3,n4):
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.n4=n4
    def __repr__(self):
        return (f"1:{self.n1}\n2:{self.n2}\n3:{self.n3}\n4:{self.n4}")
    def __str__(self):
        return (f"1:{self.n1}\n2:{self.n2}\n3:{self.n3}\n4:{self.n4}")
    def __int__(self):
        return self.n4
    # def __float__(self):
    #     return self.n1
    # def __complex__(self):
    #     return self.n2
    # def __round__(self):
    #     return self.n4
    # def __trunc__(self):
    #     return self.n1
    # def __ceil__(self):
    #     return self.n2
    # def __floor__(self):
    #     return self.n2
obj1=Dunderexamples(30,40,"40",4.4)
print(obj1)
print(obj1.__int__())
# print(obj1.__float__())
# print(obj1.__complex__())
# print(obj1.__round__())
# print(obj1.__trunc__())
# print(obj1.__ceil__())
# print(obj1.__floor__())






















































