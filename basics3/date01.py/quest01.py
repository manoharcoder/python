import math

def circle(r):
    area=math.pi*r**2
    return area

def rectangle(l,b):
    area=l*b
    return area

def square(a):
    area=a**2
    return area

def triangle(B,h):
    area=0.5*B*h
    return area

r=int(input("enter radious of circle  :"))
arcircle=circle(r)
print("area of circle is :",arcircle)
l=int(input("enter length of rectangle :"))
b=int(input("enter breath of rectangle  :"))
arectangle=rectangle(l,b)
print("area of rectangle is :",arectangle)
a=int(input("enter side of  square  :"))
arsquare=square(a)
print("area of square is :",arsquare)
B=int(input("enter breath of triangle:"))
h=int(input("enter height of triangle  :"))
artriangle=triangle(B,h)
print("area of circle is :",artriangle)
