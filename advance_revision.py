print('*************************list**************************')
a=[1,2,3]
b=[i*i for i in a]
print(a)
print(b)

print('*************************Tuple**************************')
my_tuple="prabesh","raj",26
name, midname,age=my_tuple
print(name,midname,age)

#tuple additional code
my_tup=(1,2,3,4,5)
i1, *i2, i3=my_tup       # *i2 will make a list here     
print(i1)
print(i3)
print(i2)

print('*************************Dictionary**************************')

mydict={"name":"prabesh","age":26,"height":"5.3ft"}
print(mydict)

# can be done by using dict function also
mydict2=dict(name="prabesh",age=26,height=5.3)
print(mydict2)
mydict['Email']='xyz@gmail.com'
print(mydict)
del mydict['Email']
print(mydict)

for key in mydict:
    print(key,end=" ")
print()
for value in mydict.values():
    print(value,end=" ")

# print()
for key,value in mydict.items():
    print(key,value)


mydict_cpy=mydict.copy()  # if not written this original dictionary will be affected
mydict_cpy['address']='Sukedhara'
print(mydict_cpy)
print(mydict)
print(),print()


print('******************************set*****************************')

myset=set('Hello')
print(myset)

my_num=[1,2,3,2,2,5,'hello']
new=set(my_num)
print(new)
print(new.pop()) # this will erase/delete the arbitray value from the list 
print(new)

set1={1,2,3,4,4,5}
set2={0,2,4,6,8,10}
set3={2,3,5,7,9,11}

uni=set1.union(set2)
print(uni)

inter=set1.intersection(set2)
print(inter)

print('*********strings***********')

my_string="""hello
world"""
print(my_string)
mystring='Prabesh'
mystring[2]='c'
print(mystring)      # string does not support assignment

mynam='Hello world'
print(mynam[::-1])

my_string='Praaaaaaaabeshrajojha'
my_string=my_string.strip() # this will clear the white space of the string
print(my_string)
if my_string.startswith('P'):
    print('True')
else:
    print('False')

print(my_string.find('r'))  # find the index of the string 
print(my_string.find('raj'))
print(my_string.replace('raj','lal'))

print(my_string.split())  # this will search for the space and convert into the list
new_string='this,is,the,new,text'
print(new_string.split(',')) # is there is an immediate comma then delimeter should be comma as shown

# # to join the string

splitted_string=my_string.split(" ")
print(splitted_string)
joined=' '.join(splitted_string) # '' is indication of empty string ( join nothing before the initial string)
print(joined)        # if space is typed in the '' then space is printed



print('***********collection**************')

from collections import Counter  # this is the counter import to count the strings variables or 
my_counter=Counter(my_string)
print(my_counter)
print(my_counter.most_common(1)[0][0])  # (1)-- most common element,, (1)[0]= gives list with tuple,, (1)[0][0]--element of tuple


print('**********************Named Tuple********************')
from collections import namedtuple
Car=namedtuple('Car','color,model')    # it is similar to class and its object creation
obj=Car('Red','Ford')
print(obj.color,obj.model) # just like calling class variables through class object

print('**********************Iter Tools*****************')

from itertools import product
a=[1,2]                      
b=[2,4]        # most straight forward method to multiply two list is to multiply index wise but it would be frustrating
myprod=product(a,b) # ,so that product function can multiply two list element wise 
print(list(myprod))

from itertools import permutations
list1=[1,2,3,'hello']
per=permutations(list1,2) # this will give the possible number of permutation of the list
print(list(per))          # 2 is how many permutation should it take at once

from itertools import combinations
list1=[1,2,3,'hello']
comb=combinations(list1,2) # this will give the possible number of combination of the list
print(list(comb))  # note that combination output is less as repeation is not taken into account here

from itertools import accumulate
a=[1,2,3,4]
acc=accumulate(a)         # result the sequential sum of the list item
print(a)
print(list(acc))






print()
print()
print()
print()