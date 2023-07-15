print(),print()
# def calldecorators(func):

#     def wrapper():
#         print('This is the first call through decorators')
#         func()
#         print('This is the last call')
#     return wrapper
    
# @calldecorators
# def start():
#     print('This is second call through exchange of function= func()=start()')
# start()
print('============================*args==========================')
def sum(*a):
    sum=0
    print(a)
    for i in a:
        sum+=i
    return sum
print(sum(5,5,4)) # with this, any number of arguments can be passed to a single variable *a ( as tuple)

print()
print('============================**kwargs==========================')
print()
def find(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f'{key}:{value}')

find(age=26,name='prabesh',height=5.3)

print(),print()