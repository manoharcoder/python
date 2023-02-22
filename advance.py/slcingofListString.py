# slicing the lists string

numb=[1,2,3,4,5,6,7,8,9]
print(numb[0])
print(numb[1])
print(numb[(len(numb)-1)])
print(numb[-1])
print(numb[-3])

#slicing allows us to create a new lists from the excisting list

n1=[11,22,33,44,55,66,77,88,99]
new_list=n1[2:6]
print(new_list)
new2_list=n1[-3:-1]
print(new2_list)

#step used to skiping some elements based on condition

n1=[11,22,33,44,55,66,77,88,99]
new1_list=n1[1::2]
print(new1_list)
new2_list=n1[0::2]
print(new2_list)

# reversing a list
n1=[11,22,33,44,55,66,77,88,99]
print(n1[::-1])

# change mutiple elements at once by using the slicing notations
n1=[11,22,33,44,55,66,77,88,99]
print(len(n1))
n1[1:3]=[1,2,3,4,5,6]
print(n1,len(n1))
