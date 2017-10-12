# Declare a variable and initialize it

f = 0;
print f


# re-declaring the variable works
f = 'abc'
print f

# Error: different types can't be cobined
# print ("string type") +123

print ("string type") + str(123)

# Glable vs. local variable in functions
def someFunction():
    #global f
    f = "def"
    print f

someFunction()
print f


#del f
#print f
