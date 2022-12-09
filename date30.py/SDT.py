'''# TOUPLES
#toples same as lists but the difference is that it is immutable 
numbers =(1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[1:])          #we can perform slicing
#we can itterate throw it 
for i in numbers :
    print(i)

print('-------------------------------------------------')
# numbers[2]=10
# print(numbers)

# DICTIONARYS
#dictionarys are collection of  key and value pairs  
# items must be in pair forms ex {'age':23}
# it is unodred
# it is indexed
# it is mutable
# cannt contain deplicate keyes 
# used methods  items(),keyes(),update(),get()   popular methods for dictionaries 

mydict={"name":"manohar","age":23,"height":5.3,"address":"andhrapradesh","village":"polireddy palli"}

print(mydict)
# axcessing values using their keyes that nearly equal to index accessing in list
print(mydict["age"])
print(mydict["village"])
print(mydict["address"])
print(mydict["height"])
#importent methods for dict
print(mydict.items())
print(mydict.keys())
print(mydict.values())
 # ellements can add using update and can also do update their elements 
mydict.update({"name":"mohan"})
print(mydict)
mydict.update({"pincode":2340})
print(mydict)
mydict["name"]="manu"

#to remove elements 
mydict.pop("pincode")
print(mydict)
newdict=mydict.copy()
mydict.clear()
print(mydict)

# copy and get method and deafult get method 
print(newdict)
print(newdict.get("name"))
print(newdict.get("village"))
print(newdict.get("pincode"))
print(newdict.get("hobbies","playing games"))

'''
print('-------------------------------------------------')

# SETS IN PYTHON
#    MUTABLE                IMMUTABLE 
#    LIST                   STRINGNUMERS
#    DICTIONARIES           TUPLES

# items in a sets not in order 
# no duplicate elements are allowed
# items must be immutabe 
 # methods = add(),update(),dicard(), remove(),clear(), union(),intersection()
  
# animals={"dog","cat","tiger","elephant","dog"}
# print(animals)
# print(animals)
# print(type(animals))
# print(len(animals))
# birds={}
# print(birds)

#convet lists ,tuples, dict in to sets 
# animals= set (["dog","cat","tiger","elephant","dog"])
# print(animals)
# print(type(animals))
# newset=set({"name":"manohar","age":23,"height":5.3,"address":"andhrapradesh","village":"polireddy palli"})
# print(newset)
# print(type(newset))

#add update
# animals= set (["dog","cat","tiger","elephant","dog"])
# animals.add("monkey")
# print(animals)

# wild_fishes={"shark","bluewale","gold fish"}
# animals.update(wild_fishes,{"toutaels"})   # normal passing devides them as like individual charcters "t","o".....
# print(animals)

# #remove and dicard  and clear# removes throws an error if item not in set so we use dicard at that point
# animals= set (["dog","cat","tiger","elephant","donkey","dog"])
# animals.discard("cat")
# print(animals)
# animals.discard("cat")    # not throws error
# print(animals)
# animals.remove("donkey")
# print(animals) 
# animals.clear()
# print(animals)

#union and intersection
# set1={1,2,3,4,5,6,7,2,3,4,8,9}
# set2={1,22,33,44,55,2,3,4,8,6,9,0}
# set3=set1.union(set2)     #union also can replace with its symbol is |
# print(set3)

# set1={1,2,3,4,5,6,7,2,3,4,8,9}
# set2={1,22,33,44,55,2,3,4,8,6,9,0}
# set3=set1.intersection(set2)     #intersection also can replace with its symbol is &
# print(set3)