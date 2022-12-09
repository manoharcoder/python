#1)write a py to order the food in zomato
#a) disply the manu for the user
#1:pastha,2:fish,3:pannerbutter,4:icecream,5:mocktail,6:placeorder

items=[]
totalamount=[]

def pastha():
    item,price="pastha",150
    items.append(item)
    totalamount.append(price)
    print("added to cart",item,"and is price",price)
    zomato()

def fish():
    item,price="fish",200
    items.append(item)
    totalamount.append(price)
    print("added to cart",item,"and it's price",price)
    zomato()

def pannerbutter():
    item,price="pannerbutter",100
    items.append(item)
    totalamount.append(price)
    print("added to cart",item,"and it's price",price)
    zomato()

def icecream():
    item,price="icecream",70
    items.append(item)
    totalamount.append(price)
    print("added to cart",item,"and it's price",price)
    zomato()

def mocktail():
    item,price="mocktail",120
    items.append(item)
    totalamount.append(price)
    print("added to cart",item,"and it's price",price)
    zomato()

def placeorder():
    count=list(range(1,len(items)+1))
    print("your order is placed:")
    print("orderd items and their prices")
    for i,item,amount in zip(count,items,totalamount):
       print(f"{i}.{item} = RS {amount}/-")
    print("total amount to be paid : ",sum(totalamount),"/-only")
    print("------------------------------------------------------")
    print("do you want to taste more dishes  ")
    i=input("type yes if you need forther more :")
    if("yes"==i):
        zomato()
#dishes_prices={"pastha":150,"fish":200,"pannerbutter":100,"icecream":70,"mocktail":120}
items_dict={1:pastha,2:fish,3:pannerbutter,4:icecream,5:mocktail,6:placeorder}

def zomato():   
    value=int(input("select items with their respective numbers::"))
    for item in items_dict:
        if (value==item):
            items_dict[value]()
            break
    else:
        print("enter valid number to order  dishes ::")
print("------------------------------------------------------")
print("welcome to the zomato to order your favorite dishes")
print('''select the items\n1.pastha :Rs 150\n2.fish :Rs 200 \n3.pannerbutter :Rs 100
4.icecream :Rs 70\n5.mocktail :Rs 120\n6.placeorder''')
print("------------------------------------------------------")
zomato()



