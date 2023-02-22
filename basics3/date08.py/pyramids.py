# 0
# 01
# 012
# 0123
# 01234

for i in range(6):         # i defines no.of rows
    for j in range(i):       # j defines no.of coloumns
        print(j,end=" ")
    print()

print("-------------------------------")


# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n") # after for loop it gives an one line gap

print("-------------------------------")

# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print("\n")

print("-------------------------------")

#*****
#****
#***
#**
#*

for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("-------------------------------")
#*
#**
#***
#****
#*****

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()