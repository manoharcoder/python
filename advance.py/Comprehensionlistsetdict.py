"""LIST COMPREHENSIONS"""

numbers=[]
for i in range(1,6):
    numbers.append(2**i)
print(numbers)

# to get above code in to the one line
numbers=[2**i for i in range(1,6)]
print(numbers)

# conditional list comprehension
numbers=[1,4,9,16,25,36,49,64,81,100,121]
print(numbers)
even_sqt=[i for i in numbers if i%2==0]
print(even_sqt)


# to get sqrts of numbers use sqrt()
import math as m
all_sqrt=[m.sqrt(n) for n in numbers ]
print(all_sqrt)

even_sqrt=[m.sqrt(n) for n in numbers if n%2==0 ]
print(even_sqrt)

odd_sqrt=[m.sqrt(n) for n in numbers if n%2!=0 ]
print(odd_sqrt)

# multipleloops in one
team1=['janet','arya','mary']
team2=['even','jacky','randy']

my_list=[(x,y) for x in team1 for y in team2]
print(my_list)

my_list=[{x,y} for x in team1 for y in team2]
print(my_list)

"""SETS COMPREHENSIONS"""
# ex1 normal strings conv in to sets and have  a no repeat element in it
n1="procoder"
alphbet={x for x in n1}
print(alphbet)

"""DICT COMPREHENSIONS"""
numbers=[1,2,3,4,5,6]

sqr_dict=dict()

# for num in numbers:
#     sqr_dict[num]=num**2
# print(sqr_dict)

sqr_dict={num:num**2 for num in numbers}
print(sqr_dict)


# incease price for items those intial price grater than 2 only using dict comprehension

old_price={'milk':1.02,"coffe":2.5,"bred":2.5,"butter":3.0}

new_price={key:value*1.5 if value>2 else value for(key,value) in old_price.items()}
print(new_price)