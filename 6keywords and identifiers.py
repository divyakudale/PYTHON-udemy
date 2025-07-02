#True False
print(5==5)
print(5<5)

#None
print(None == 0)
print(None == False)
print(None == True)
print(None == None)

def a_void_function():
    a=1
    b=2
    c=a+b
x = a_void_function()
print(x)

#and, or, not
print(True and False)
print(True or  False)
print(not False)

#as, math
import math as mymath
print(mymath.cos(mymath.pi))

#assert
assert 5 > 4 
assert 5 == 5

#break
for i in range (1, 11):
    if i == 5:
        break
    print(i)
    
#countinue
for i in range (1, 11):
    if i == 5:
        continue
    print(i)
    
#class



#def, pass
def function_name(parameters):
    pass
function_name(12)

#del 
a = 10
print(a)
del a
#print(a)

#if elif else
num = 2
if num == 1:
    print('one')
elif num == 2:
    print('two')
else:
    print('something else')
    
#try raise catch finally
try:
    x=10
    #raise ZeroDivisionError
except ZeroDivisionError:
    print("division cannot be performed")
finally:
    print("Execuiton Successfully")
    
#for
for i in range(1,10,2):
    print(i)
    
#global
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globavar =15
read1()
write1()
write1()
read1()
    
#in not in
a = [1,2 ,3, 4]
print(4 in a)
print(8 in a)
print(2 not in a)

#is
print(True is True)

#lambda
a = lambda x: x*2
for i in range (1,6):
    print(a(i))

#nonlocal
def outer_fun():
    a = 5
    def inner_fun():
        nonlocal a
        a = 10
        print("innner_function: " , a)
        inner_fun()
        print("Outer function: ", a)
outer_fun()

#return
def func_return():
    a = 100 
    return a 
print(func_return())

#while
i = 5
while(i>0):
    print(i)
    i-=1

#with
with open ('example.txt', 'w') as my_file:
    my_file.write('hello world!!')

#yield
def generator():
    for i in range (6):
        yield i*i
g = generator()
for i in g:
    print(i)