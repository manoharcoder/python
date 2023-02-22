animals=["tiger","lion","liger","tigon","elephant","crocodail"]

for animal in animals:
    if animal=="tiger":
        print("item found")
    # else:
    #     print("item not found")


# now use flags 
animals=["tiger","lion","liger","tigon","elephant","crocodail"]

flag=False
for animal in animals:
    if animal=="tiger":
        flag=True

if flag:
    print("item found")
else:
    print("item not found")

# it is better than using flag

for animal in animals:
    if animal=="monkey":
       print("item  found")
       break
else:
    print("item not found")


# while else
# check prime numbers using while

num=int(input("enter a number"))
i=2
while i<num:
    if(num%i==0):
       print(num,"is not a prime number as it is ",num//i,"times",i) 
       break
    i+=1
else:
    print(num,"is a prime number")




