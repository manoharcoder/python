import math
def circle():
   r=int(input("enter radious of circle  :"))
   area=math.pi*r**2
   print("area of circle is :",area)

def rectangle():
   l=int(input("enter length of rectangle :"))
   b=int(input("enter breath of rectangle  :"))
   area=l*b
   print("area of rectangle is :",area)
   
def square():
   a=int(input("enter side of  square  :"))
   arsquare=a*a
   print("area of square is :",arsquare)

def triangle():
   B=int(input("enter breath of triangle:"))
   h=int(input("enter height of triangle  :"))
   area=0.5*B*h
   print("area of circle is :",area)

def exit():
   print("good bye")


print('''chose number to find out their respective areas\n1:circle\n2:rectangle\n3:square\n4:triangle\n5:exit ''')
num=int(input("enter number:"))
aplication_set={1:circle,2:rectangle,3:square,4:triangle,5:exit}
for digit in aplication_set:
   if num==digit:
      aplication_set[digit]()
      break
else:
   print("enter valid number to get their respective operation")  

