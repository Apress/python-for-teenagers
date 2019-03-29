
# We first have to import our module
# We import our module by using the name of the file, minus the .py extension

import ourFirstModule

# Now we call the function to use it

ourFirstModule.firstFunction()

# print the helpfile for firstFunction()

help(ourFirstModule)

# Calling our second function

ourFirstModule.secondFunction()

# Calling and printing a variable within our module

print("The value of a is: ",ourFirstModule.a)




