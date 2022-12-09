#5 write aprogram to print tables from 1 to 10 take input from user
number=int(input("enter the number :\t"))
for i in range (1,11):
    print(f"{number} X {i}={number*i}")
    #print("{} X {} = {}".format(number,i,number*i))
    #print(number," X ",i," = ",number*i)