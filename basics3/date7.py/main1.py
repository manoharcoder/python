"""IF __NAME__==__MAIN__"""
# __main__ method is used to restric the data of a file while importing it in another file 
# it cann't intrupt the program execution in the same file 
# but it is usefull to restric some of data usage in another file by using if(__name__=='__main__') in the original file
# we place the useful information in namemain method

print("hi hello i am good person",__name__)
#o/p hi hello i am good person __main__
def sqr(a):
    return a**2
def greeting():
    print("hello manu")


#if __name__=='__main__':
square=sqr(5)
print(square)
greeting()
