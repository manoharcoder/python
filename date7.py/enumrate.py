# '''enumarate'''
# enumarate is used to print list values with their indexes we can also modify index positions

# mylist=[10,20,30,40,50]
# for i,index in mylist:
#     print(i)                   #TypeError: cannot unpack non-iterable int object     
  
print("--------------------------------------")

mylist=[10,20,30,40,50]
for index in range(len(mylist)):
    print(index,mylist[index])                   #TypeError: cannot unpack non-iterable int object     
  
print("--------------------------------------")

mylist=[10,20,30,40,50]
for i,index in enumerate (mylist):   # default enumrate starts from 0 index
    print(i,index)

print("--------------------------------------")

mylist=[10,20,30,40,50]
for i,index in enumerate (mylist,1):    # default enumrate starting index can change for our convience
    print(i,index)

print("--------------------------------------")
mylist=[10,20,30,40,50]
enm=enumerate(mylist,100)     # in this case we need to enumrate list first we get 
                                #TypeError: 'enumerate' object is not subscriptable
enmlist=list(enm)               # we need to store them in list format  
for i in enmlist:
    print(enmlist[1:3])           # if we pass i value in enumrate[i] TypeError: list indices must be integers or slices, not tuple
    print(enmlist[3])