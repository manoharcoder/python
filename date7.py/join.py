"""JOIN METHOD"""
# # it is afunction it can iterate a list,tuple and dictionary using join
# # using a  saparater value like ! @ # $ % ^ & * () bust shoud of same data type 
# mylist={"hi","hello","good","morning","manu"}
# seprator="-"
# result=seprator.join(mylist)
# print(result)        # output varying    hello-morning-manu-good-hi
# print(type(result))
print("---------------------------------------")
# mylist=("hi","hello","good","morning","manu")
# seprator="-"
# result=seprator.join(mylist)
# print(result)           #output cames frome tuple so o/p not varying   hi-hello-good-morning-manu
# print(type(result))
print("---------------------------------------")
# numlist=(1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9) # numbers not axcepted,float
# seprator="-"
# result=seprator.join(numlist)  # TypeError: sequence item 0: expected str instance, int found
# print(result)           #  
# print(type(result))
print("---------------------------------------")
#dictionaries
dict={"x":1,"Y":2,"Z":3}      #values in the form of int so it should not axcepted 
print(" ".join(dict))
print(" ".join(dict.keys()))
#print(" ".join(dict.values()))  #thats why it not works
#print(" ".join(dict.items()))    #thats why it not works TypeError: sequence item 0: expected str instance, tuple found
print("---------------------------------------")
dict={"x":"1","Y":"2","Z":"3"}
print("@".join(dict))
print("$".join(dict.keys()))
print("&".join(dict.values()))
#print(" ".join(dict.items()))     # TypeError: sequence item 0: expected str instance, tuple found