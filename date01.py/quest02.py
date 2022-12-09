import math
def circle():
   r=int(input("enter radious of circle  :"))
   area=math.pi*r**2
   print("area of circle is :",area)
   operations()

def rectangle():
   l=int(input("enter length of rectangle :"))
   b=int(input("enter breath of rectangle  :"))
   area=l*b
   print("area of rectangle is :",area)
   operations()

def square():
   a=int(input("enter side of  square  :"))
   arsquare=a*a
   print("area of square is :",arsquare)
   operations()

def triangle():
   B=int(input("enter breath of triangle:"))
   h=int(input("enter height of triangle  :"))
   area=0.5*B*h
   print("area of circle is :",area)
   operations()

def exit():
   print("good bye")

def operations():
   print("choose the fallowing numbers to get their respective areas  \n1):circle\n2):rectangle\n3):square\n4):triangle\n5):exit")
   n=int(input())
   if(n>0 and n<6):
      if(n==1):
         circle()
      if(n==2):
         rectangle()
      if(n==3):
         square()
      if(n==4):
         triangle()
      if(n==5):
         exit()
   else:
      print("give the valid input ")
      operations()     

operations()