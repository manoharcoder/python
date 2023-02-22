'''*ARGS'''


def addnum(*args):
    # total=0
    # total=sum(args)
    # print(total)
    for i in args:
        print(i)
        print(type(mlist))
    print(type(args))
    print("---------------------------")
# addnum()
# addnum(1,2,3)
# addnum(5,6,7,8,9)
# addnum(10,20,30,40,50,60,70,80,90)
mlist=[10,20,30,40,50,60,70,80,90]

addnum(mlist)


# def addnum(name,age,*args):
#     # total=0
#     # total=sum(args)
#     # print(total)
#     print(args)
#     print(type(args))
#     print("name",name,"age",age)
# # # addnum()
# # addnum(1,2,3)
# # addnum(5,6,7,8,9)
# # addnum(10,20,30,40,50,60,70,80,90)
# args=[10,20,30,40,50,60,70,80,90]
# addnum("ark",20,args)

'''**KWARGS'''

def addnum(**kwargs):
    for x,y in kwargs.items():
        print(f"{x}---{y}")
addnum(name='manu',age=23,height=5.4)

