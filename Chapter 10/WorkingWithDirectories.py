# Import the module os
# This is used to work with operating system information
import os

# Use the getcwd() method of the os module
# To see what directory we are in
os.getcwd()

# Create a new directory or folder
# We commented this out because we created the directory earlier
# If we don't, Python will try to create it again
# Causing an error

# os.mkdir("newDirectory")

# Using the chdir() method to change directories
print("Changing to the newDirectory folder: ")
os.chdir("C:/Users/James/AppData/Local/Programs/Python/Python36-32/newDirectory")

# Print out the current directory to verify it changed
print(os.getcwd())

# Switching back to the original directory
# Remember to use your own directory, not mine!
os.chdir("C:/Users/James/AppData/Local/Programs/Python/Python36-32")

# Verifying that we are back to the original directory
print("Back to the original directory: " )
print(os.getcwd())

# Deleting the newDirectory directory
# Using the rmdir() method

os.rmdir('newDirectory')

