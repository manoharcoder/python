#1)create two lists and pick an odd indexed item from list1 and even indexted item from list and the print them in new list
# list1=[3,6,9,12,15,18,21]
# list2=[4,8,12,16,20,24,28]
# then o/p is [list1,list2]===[6,12,18,4,12,20,28] 

# list1=[3,6,9,12,15,18,21]
# list2=[4,8,12,16,20,24,28]
# list3=[]
# for idx,value in enumerate(list1):
#     if(idx%2!=0):
#         list3.append(value)
# for idx,value in enumerate(list2):
#     if(idx%2==0):
#         list3.append(value)

# print(list3)

# list1=[3,6,9,12,15,18,21]
# list2=[4,8,12,16,20,24,28]
# # list3=[]
# list3=[list1[1::2],list2[0::2]]
# print(list3)

# list1=[3,6,9,12,15,18,21]
# list2=[4,8,12,16,20,24,28]
# list3=[]
# odd_elements=list1[1::2]
# even_elements=list2[0::2]
# list3.extend(odd_elements)
# list3.extend(even_elements)
# print(list3)

print("----------------------------------------------------------------------------")

#2) remove and add items in a list
#write py to remove the items present at index 4 and add it to the 2nd position and at the end of the list
#list1=[34,54,67,89,11,43,94]

# list1=[34,54,67,89,11,43,94]
# print("before doning any poerations on list",list1)
# elemet=list1.pop(4)
# print("after removing element at index 4 in  list the output is ",list1)
# list1.insert(2,elemet)
# print("after same  element at index 2 in  list the output is ",list1)
# list1.append(elemet)
# print("after append element at the last place in  list the output is ",list1)

#3) slice the list into the 3 equal chunks and reverse each chunk
# list1=[11,45,8,23,14,12,78,45,89]
# count=len(list1)
# lst1=list1[0:int(count/3)]
# print("chunk 1",lst1)
# print("after reversing the chunk 1",lst1[::-1])
# lst2=list1[int(count/3):int((count/3)+3)]
# print("chunk 2",lst2)
# print("after reversing the chunk 2",lst2[::-1])
# lst3=list1[int((count/3)+3):]
# print("chunk 3",lst3)
# print("after reversing the chunk 3",lst3[::-1])

#
# list1=[11,45,8,23,14,12,78,45,89]
# count=int(len(list1))
# chunk_size=int(count/3)
# start=0
# end=chunk_size
# for i in range(1,4):
#     list_chunk=list1[start:end]
#     print("chunk ",i,list_chunk)
#     print("after reversing it ",list_chunk[::-1])
#     print("after reversing it ",list(reversed(list_chunk)))
#     print(start,end)
#     start=end
#     end+=chunk_size


#4) count the occuence of each  lememt  from the list
# sample_list=[11,45,8,11,23,45,23,45,89]
# my_dict=dict()
# for i in sample_list:
#     count1=sample_list.count(i)
#     my_dict.update(i)

# print("printing cout of each item ",my_dict)

# sample_list=[11,45,8,11,23,45,23,45,89]
# print("original list is ",sample_list)
# count_dict=dict()
# for item in sample_list:
    
#     print("for loop item is :",item)
#     print("")
#     if item in count_dict:
#         print("if loop item is ::",item)
#         print("")
#         count_dict[item]+=1
#     else:
#         count_dict[item]=1
# print("printing cout of each item ",count_dict)

#5) create a pythonset thet it shows the elemnt from both list in a pair
# f_list=[2,3,4,5,6,7,8]
# s_list=[4,9,16,25,36,49,64]
# r_dict={(6,36),(8,64),(2,4),(3,9),(5,25)(7,49)}


# use zip() function takes a two or more iterables(lisy,dict,string) and aggregates them in a tuple,and return it  
# f_list=[2,3,4,5,6,7,8]
# s_list=[4,9,16,25,36,49,64]
# print("first list is ::",f_list)
# print("second list is ::",s_list)
# r_dict=set(zip(f_list,s_list))
# print("resluted  dict is ",r_dict)

#6)find the intersection  of tw0 sets and remove those elementfeom the  frist set
#f_set={233,42,65,57,78,83,29}
#s_set={57,83,29,67,73,43,48}
#intersection is {57,83,29}
# frists set after removing the commmon elements is {65,42,78,23}

# f_set={233,42,65,57,78,83,29}
# s_set={57,83,29,67,73,43,48}
# common_elements=f_set.intersection(s_set) 
# print("common elements is ",common_elements)

# for i in common_elements:
#     f_set.remove(i)
# print("frists set after removing the commmon elements is ",f_set)

#7)chunks if one set is a subset or superset of another set. if found,delete all elements from that set
f_set={27,43,34}
s_set={34,93,22,27,43,53,48}
# print("frist set is ",f_set)
# print("second set is ",s_set)

# print("frist set is a subset of second set -",f_set.issubset(s_set))
# print("second set is a subset of first set -",s_set.issubset(f_set))

# print("frist set is a superst of second set -",f_set.issuperset(s_set))
# print("second set is a superset of first set -",s_set.issuperset(f_set))
# if f_set.issubset(s_set):
#     f_set.clear()
# else:
#     s_set.clear()


# print("frist set is ",f_set)
# print("second set is ",s_set)

#8) iterate a given list and chunk if a given element exists as a key's values ina dictionary.if not delete it from the list
roll_num=[47,64,69,37,76,83,85,97]
sample_dict={"jhon":47,"emma":69,"kelly":76,"joson":97}
print("roll_num",roll_num)
print("sample_dict",sample_dict)
f_roll_num=roll_num.copy()
print("before :::",f_roll_num)
f_roll_num[:]=[item for item in roll_num if item in sample_dict.values()]
print("after removind unwanted roll num ::",f_roll_num)

# for item in roll_num:
#     print("for loop item is :",item)
#     print("")
#     if item in sample_dict.values():
#         print("if loop item is ::",item)
#         print("")
#     else:
#        roll_num.remove(item)
# else:
    
#    roll_num.remove(item)
# print("after removing the unwanted  elements from a listt",roll_num)

# new_rollnum=list()
# for item in roll_num:
#     print("for loop item is :",item)
#     print("")
#     if item in sample_dict.values():
#         print("if loop item is ::",item)
#         print("")
#         new_rollnum.append(item)
# print("after removing the unwanted  elements from a listt",new_rollnum)






