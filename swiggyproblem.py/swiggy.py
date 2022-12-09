import time
items=[]
totalAmount=[]

def dosa(item,price):
    items.append(item)
    totalAmount.append(price)
    print("added to the cart",item)
    time.sleep(2)
    swiggy()

def burgur(item,price):
    items.append(item)
    totalAmount.append(price)
    print("added to the cart",item)
    time.sleep(2)
    swiggy()

def pizza(item,price):
    items.append(item)
    totalAmount.append(price)
    print("added to the cart",item)
    time.sleep(2)
    swiggy()
    
def chicken(item,price):
    items.append(item)
    totalAmount.append(price)
    print("added to the cart",item)
    time.sleep(2)
    swiggy()
    
def placeorder():
    print("your oder is placed")
    print("orderred items are ")
    for item,price in zip(items,totalAmount):
        print(item,price)
    print("total amount should paid :",sum(totalAmount))
    time.sleep(2)
    swiggy()

def swiggy():
    n=int(input("select the number::"))
    if(n>0 and n<6):
        if(n==1):
            dosa("dosa",50)
        elif(n==2):
           burgur("burgur",150)
        elif(n==3):
            pizza("pizza",250)
        elif(n==4):
            chicken("chicken",350)
        elif(n==5):
            placeorder()
        else:
            print("enter valid number that should in between 1 to 5 only")

print("welcome to swiggy")
print("slect the items menu\n1.dosa\n2.burgur\n3.pizza\n4.chicken\n5.placeorder")
swiggy()