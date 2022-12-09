'''try ---catch---finally'''

#exceptions                     cause of error
#File not found error          file when that doest exist is accessed 
#Indexerror                    when the index of the sequance is out of range
#Floating point error          when a floating point operator fails

'''try:
     #code that may cause exception
   exception:
     #code to run when exception occures '''
# N=int(input("enter numerator::"))
# D=int(input("enter denominator::"))    # if it is 0 it gives a zero devision error
# print(N/D) 

# try:
#     N=int(input("enter numerator::"))
#     D=int(input("enter denominator::"))    # if it is 0 it gives a zero devision error
#     print(N/D) 
# except:
#     print("denominator cannot be zero .please try again")
# finally:
#     print("program ends")

# ''' print different error messages  like Zero devision error, index error'''

# try:
#     N=int(input("enter numerator::"))
#     D=int(input("enter denominator::"))    # if it is 0 it gives a zero devision error
#     print(N/D) 
# except Exception as error:
#     print("error is occured",error)
# finally:
#     print("program ends")

''' print different error messages  like Zero devision error, index error'''


# try:
#     N=int(input("enter numerator::"))
#     D=int(input("enter denominator::"))    # if it is 0 it gives a zero devision error
#     print(N/D) 
#     mlist=[1,2,3,4,5]
#     print(mlist)
#     i=int(input("enter Index:"))
#     print(mlist[i])
# except ZeroDivisionError:
#     print("denominator cannot be zero .please try again")
# except IndexError:
#     print("index cant be grater than sige of its list",len(mlist))
# finally:
#     print("program ends")

''' finally '''
#finally block will always executes irespective of its try exception blocks 
# try:
#     print(1/0)
# except:
#     print("wrong denotation ")
# finally:
#     print("always printed")