#
# Example file for variables

# Declare a variable and initialize it
f = 0;
print f

# re-declaring the variable works
f = "abc"
print f

# ERROR: variables of different types cannot be combined
#print "string type " + 123
print "string type" + str(123)

# Global vs. local variables in functions
def somefunction():
    #global f
    f ="def"
    print f

somefunction()
print f

#del f
#print f