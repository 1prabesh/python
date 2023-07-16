# this is lamda function in python
print(),print()
def sqr(x):
    return x*x

print(sqr(5))


# doing same thing with lamda function 
# syantax(could be variable as well)= lamda parameter:expression
sqr=lambda x:x*x
print(sqr(5))



mul=lambda x,y,z,w:x*y*z*w
print(mul(4,5,6,7))

valid_check=lambda age: True if age>=18 else False
print(valid_check(17))


myl_t=[(1,2),(3,4),(5,6)]
print(myl_t[2])
for item in myl_t:
    print(item)



mylist=[1,2,8,4,6]
update=sorted(mylist,key=lambda x:x>x+1)
print(update)


print('*********************Random**********************')
import random
print(random.randint(5,9))
print(random.randrange(1,10))
print(random.normalvariate(0,1))  # return the normal value from probabiloty density ,bell curve -1 to 1

# using random sampling method with list
new_list=[1,2,4,5]
val=random.sample(new_list,3) # no repetion is allowed
print(val)
# if repetion is need we need choice function
val2=random.choices(new_list,k=3)
print(val2)






print(),print(),print()