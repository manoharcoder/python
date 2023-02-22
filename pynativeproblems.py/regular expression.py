"""RegEx or RegularExpression"""
# a RegEx or RegularExpression it is a sequence of characters that forms a serch pattren 
# regula expression is used to check if a string contains the specified search pattren
# we use bulit in moduel "re" to work with it we need to import it 
# ^   or "^hello" = matching at starting position
# $   or "india$" = matching at ending position
# .   or "he..o"  = single character matching
# .*  or "h.*o"   = zero or no.of matching character
# []  or "[a-n]"  = return a set of chr
# \   or   "\d"   = escape sepcial characters 
#  {} or "he.{2}o"= exactly the specified no.of characters
#  | or "falls|stays"= either or 
# ?  or or "he.?o"=zero or more occurences
# +  or "he.+o"  = one or more occurence


#regula expression functions
# findall = returan a list containing match all
# search = return a match objects if there is a match anywhare in string
# split  = return a string where the string hase been split at each match
# sub = replace one or many matches with a string 

import re
str="the rain in india"
x=re.search("^the",str)       #<re.Match object; span=(0, 3), match='the'>  for false it None     
y=re.search("india$",str)     #<re.Match object; span=(12, 17), match='india'> for flase it None
z=re.search("^the......*india$",str)
a=re.search("\s",str)

print(x)
print(y)
print(z)
print(a)

txt="the rain in spain"
x=re.findall("spain",txt)    #  ['spain']    or   []
y=re.findall("[a-m]",txt)   #['h', 'e', 'a', 'i', 'i', 'a', 'i']
print(x)
print(y)

txt="the rain in spain"
x=re.split("spain",txt)    # ['the rain in ', '']
y=re.split("[a-m]",txt)     ##['t', '', ' r', '', 'n ', 'n sp', '', 'n']
z=re.split("\s",txt)        #['the', 'rain', 'in', 'spain']
a=re.split("\s",txt,1)       #['the', 'rain', 'in spain']
b=re.split("\s",txt,2)     #['the', 'rain in spain']
print(a)   
print(z)  
print(x)
print(b)
print(y)

txt="the rain in spain"
x=re.sub("\s","9",txt)    # the9rain9in9spain
y=re.sub("i","m",txt)   #  the ramn mn spamn

z=re.sub("i","m",txt,2)   #  adding count  the ramn mn spain
print(x)
print(y)
print(z)
# print(y)





