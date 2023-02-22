"""LAMBDA FUNCTIONS"""
def double(n):
    return n*2
print(double(10))

# using lambda functions code makes easer to understand
# syntax of lambda function is
# lambda argument:expression  --->it can take any n umber of arguments but only one expression
# lambda functions dosnt have any name thtas why we can call it as annonymus functions
bouble=lambda n:n*2 
print(double(2))


larger=lambda a,b: a if a>b else b
print(larger(10,11))

#lambda function as key to sort()

# sort based on alpha bets
names=["Alan","Greodry","Zltan","Jonas","Tom","Augustine"]
names.sort()  #['Alan', 'Augustine', 'Greodry', 'Jonas', 'Tom', 'Zltan']
print(names)

# sort based on the lits length
names=["Alan","Greodry","Zltan","Jonas","Tom","Augustine"]
names.sort(key=lambda x:len(x))  #['Tom', 'Alan', 'Zltan', 'Jonas', 'Greodry', 'Augustine']
print(names)
