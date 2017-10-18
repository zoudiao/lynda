
#define a function
def func1():
    print ("I'm a function")

#define a function with argument
def func2(arg1,arg2):
    print arg1,arg2

# function taht reurns a value
def cube(x):
    return x*x*x

#function with default value for an argument
def power(num,x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result =0;
    for x in args:
        result = result + x
    return result

func1()
#call func1(), but no return value
print func1()
#function object
print func1

func2(10,20)
print func2(10,20)

print cube(3)
print power(2)
#x=2,num=3
print power(2,3)
#python knows x=3,num=2
print power(x=3,num=2)
#add all values
print multi_add(4,5,10,4)
