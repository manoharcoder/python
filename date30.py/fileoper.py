# f=open("ria.txt")
# print(f.read())   # read is used to read entire content in the file 
# f.close()

# f=open("ria.txt")
# print(f.readline())
# # print(f.readlines())
# print(f.readline())   # read line method is used to read one line 
# f.close 

# f=open("ria.txt")
# data=f.readlines()     #to get store the data inthe form of list  that from file in to new variable 
# print(data[:])            #['Ria is a institute \n', 'It teaches more cources \n', 'Cources includes python , java ,c,datascience\n', 'We are developers ']
# print(data[:-1])
# print(data[:])
# f.close()

# f=open("ria.txt")    #in read mode we get as it is in file
# data=f.read()             #Ria is a institute
# print(data[:])            #It teaches more cources
# # print(data[:-1])            #Cources includes python , java ,c,datascience
# # print(data[:])              #We are developers


# for i in data:            # used to read data charecter by character 
#     print(i)     

# f.close()

# f=open("sample.txt","x")             #open(filename,mode
# )
# f.write("manohar")
# f.writelines("\ndeveloper")
# f.writelines("\ngood human")       
# f.close()

# f=open("sample.txt","")                      #r=read only;w=for write only,if file not exists it will create new one;
# #print(f.read())                              #r+=this mode for both reading and writing ; a=output of program append to previous out put of the file
# f.append("\n do it ")                          #b=accessing binary files
# f.close()

# f=open("sample.txt","a")
# mylist=[]
# for i in range (1,3):
#     print("enter line of data")
#     line=input()
#     mylist.append(line)
# f.writelines(mylist)
# f.close
with open("ria1.txt","r+") as f:
    print(f.read())
    print(f.tell())        # tells cursor position
    print(f.seek(0))       #bring file cursor to its initial position
    print(f.readlines())
    print(f.tell())        # tells cursor position
    print(f.seek(0))       #bring file cursor to its initial position
    print(f.read(10))      #reads first 10 data in file
    print(f.read(20))      #reads next 20 data in file
    print(f.read(60))       #reads next 60 data in file
    print(f.read())         #reads reaminig data in file