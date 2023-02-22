"""OS MODULE """
# folder or directory is a location in a computer to store and organize multiple files and sub directories 
#  py has a module name """OS""" that makes it easy to work with directories and files management

# """getting current working directory"""
# #  getcwd  #  -- returns the current directory path

# import os 
# print("-------------------------")
# current_dir =os.getcwd()     #c:/Users/Bala/Desktop/python.py/osmodule.py/osoperations.py
# print(current_dir)
# print("-------------------------")
# """changing directory"""
# # # in py we can change the current working directory by using the #  chdir()  # function of the os module
# os.chdir("c:/Users/Bala/Desktop/python.py")
# print(os.getcwd())
# print("-------------------------")

# # normally we can change the directories as bellow  like this

# #c:/Users/Bala/Desktop/python.py/osmodule.py/osoperations.py
# #c:/Users/Bala/Desktop/python.py/date01.py/quest01.py

# # with open("test1.txt","w") as fp:
# #     fp.write("this is test1 file")


# """ listing all directries and files"""
# ##  listdir()  ## lists the all the deirecties with their files

# import os 
# print(os.listdir())        #['.git', 'date01.py', 'date08.py', 'date09.py', 'date29.py', 'date30.py',
#                            # 'date6.py', 'date7.py', 'exercise1.py','osmodule.py', 'revsion.py',
#                            # 'ria.txt', 'ria1.txt', 'sample.txt', 'swiggyproblem.py', 'test.txt', 'test1.txt']

# print(os.listdir("swiggyproblem.py"))              #['swiggy.py', 'zomato.py']

# """ making new directorie"""
# ## mkdir() used to create a new directorie

# # import os 
# # os.mkdir("test2")             ## >test2
# # os.mkdir("swiggyproblem.py/test2")   ## > swiggyproblem.py  # creating on secific path also possible 
#  #                                         >test2

# """renaming adirectory or a file"""
# #  rename()  is used torename the directry name or a file name 

# import os
# #os.rename("test1.txt","testtest.txt")  # rename takes two args existedname new name 

# """removing directries or file"""
# ## we use remove()  if for files also dir 
# print(os.listdir())
# os.remove("testtest.txt")
# print(os.listdir())

# ## rmdir() used to remove empty directry else exception rise 
# # 

print("-------------------------------")
"""coding of os """

import os 
print(os.getcwd())
print("-------------------------------")
#os.chdir()
print(os.listdir())
print("-------------------------------")
#os.mkdir("samp.py")
print(os.listdir())
print("-------------------------------")
os.rename("samp.py","samp1.py")
os.remove("samp1.py")
# os.mkdir("test2")
#os.rmdir("test2") 