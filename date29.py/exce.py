'''#1) USING FOR LOOPS 
# write a program to print even numbers from 1 to 10
for i in range(0,11,2):
    print(i)

print("-----------------------------------------")
# write a program to print odd numbers from 1 to 10
for i in range(1,10,2):
    print(i)

print("-----------------------------------------")
# write a program to print 20 40 60 80 100 using for loop
for i in range(0,101,20):
    print(i)

print("-----------------------------------------")

#2) USING WHILE LOOPS 
# print numbers from 1 to 10
i=1
while(i<=10):
    print(i)
    i=i+1

print("-----------------------------------------")
#print numbers from 1 to 100 it should only even numbers 
i=0
while(i<=100):
    print(i)
    i=i+2         #i+=2

print("-----------------------------------------")
#print numbers from 1 to 100 it should only odd numbers 
i=1
while(i<=100):
    print(i)
    i=i+2         #i+=2

print("-----------------------------------------")
#print numbers from 1 to 100 it should only odd numbers  it should break at 51
i=1
while(i<=100):
    print(i)
    i=i+2 
    if (i==51):
        break 

print("-----------------------------------------")
#print numbers from 1 to 100 it should only even numbers  it should continue  at 56
i=1
while(i<=100):
    if (i==56):
        break
    print(i)
    i=i+1 '''

print("-----------------------------------------")
#print numbers from 1 to 100 it should only odd numbers  it should continue at 51
i=1
while(i<=100):
    i=i+1 
    if (i==51):
        continue
    print(i)
'''print("-----------------------------------------")
#print numbers from 1 to 100 it should only even numbers  it should continue  at 56
i=0
while(i<=100):
    if (i==56):
        continue
    print(i)
    i=i+2 

i=0
while(i<=10):
    i=i+1
    if(i==5):
        continue
    print(i) 


i=0
while(i<=10):
    print(i)
    if(i==5):
        continue
    i=i+1
    #if(i==5):
      #  continue '''