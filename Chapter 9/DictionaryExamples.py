
# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename': 'Algebro', 'power': 'Mathemagics', 'real-name': 'Al. G. Bro.'}

# Print out the algebro dictionary
print(algebro)

# Print out just the real-name key's value
print(algebro['real-name'])

# Print just the keys in the algebro dictionary
print(algebro.keys())

# Print just the values in the algebro dictionary
print(algebro.values())

# Print the key-value pairs
print(algebro.items())

# Using a for loop to iterate through and print out our dictionary

for key, value in algebro.items():
    print("The key is: ", key, " and the value is: ", value)


# Add the key 'age' to the dictionary 'algebro' and assign it the value '42'
algebro['age'] = '42'

# Print out algebro to show the newly added key-value pair
print(algebro)

# Updating a the value for our 'age' key
algebro['age'] = 43

# Printing the algebro dictionary to see the updated value of the 'age' key
print(algebro)

# Using dict.update() to add a key-pair value to our 'algebro' dictionary
# Note the use of curly braces {}, mixed with parentheses ()
algebro.update({'villainType': 'mutate'})

# Printing out the results
print(algebro)

# Using the del keyword to delete a key-value pair
del algebro['power']

# Printing algebro to verify that we properly removed the key-value pair
print(algebro)

########################################################
# This section of code is commented out because it will cause everything error
# Deleting the algebro dictionary using the del keyword
# del algebro

# Printing the deleted algebro, which results in an error
# This occurs because algebro no longer exists
#print(algebro)
################################################


# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename': 'Algebro', 'power': 'Mathemagics', 'real-name': 'Al. G. Bro.'}

algebro.clear()
print(algebro)




