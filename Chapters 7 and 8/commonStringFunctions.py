# Create a string of all uppercase letters

testString = "I am YELLING!"

# Create a string to check if the variable only contains letters

firstName = "James8"

# Create a string to check if the variable only contains numbers

userIQ = "2000"

# Create a variable to count the number of characters it holds using len()

testPassword = "MyPasswordIsPassword!"

# A series of functions are tested below



print("Is the user yelling?")

# Check to see if the value of testString consists of all uppercase letters

print(testString.isupper())

# Check to see if the value of firstName contains any numbers

print("Does your name contain any numbers?")

if firstName.isalpha() == False:
    print("What are you, a robot?")

# Check to see if the value if userIQ contains only numbers and no letters

if userIQ.isnumeric() == False:
    print("Numbers only please!")
else:
    print("Congrats, you know the difference between a number and a letter!")

# Check to see if the value of UserIQ contains all spaces or whitespace chatacters

if userIQ.isspace() == True:
    print("Please enter a value other than a bunch of spaces you boob!")

# Count the number of characters in a password

print("Let's see how many characters are in testPassword!")

print("I count: ")

print(len(testPassword))


    
