'''#1) write a program to create dictionaries key value pair using input 
#employe name age number role print the keys and values only
name=input("enter employe name  :")
age=int(input("enter employe age  :"))
number=int(input("enter employe phone number : "))
role=input("enter employe role : ")
emp_dict={"name":name,"age":age,"number":number,"role":role}
print(emp_dict)
print(emp_dict.keys())
print(emp_dict.values())
print(emp_dict.items())  '''


#2) create python program to add values in to sets
# add 1 2 3 4 5 6
# union set with 7 4 5 9 0 10
# find common nelements using intersection

# my_set={1,2}
# my_set.update({3,4,5,6}) 
# print(my_set)
# print(my_set.union({7,4,5,9,0,10}))
# print(my_set.intersection({7,4,5,9,0,10}))


#3)write a python program to create new file "ria.txt"
#  a)add this using write file 
# Ria Institute of Technology
#Ria  is at marthalli benglore
# We are the developerds

#b)read the file and print it 
#c)read onlytwo lines
 #d)append developer in new line
 #e)read developer using read line 

#a)
# f=open("ria.txt","w")
# f.write("Ria Institute of Technology \nRia is at marthalli benglore \nWe are the developerds")
# f.close()
#b)
f=open("ria.txt")
print(f.read())
f.close()
#c)
f=open("ria.txt")
print(f.readline())
print(f.readline())
f.close()
#d)
f=open("ria.txt","a")
f.write("\nDeveloper")
f.close
#e)
f=open("ria.txt","r+")
data=f.readlines()
print(data[-1])
f.close()