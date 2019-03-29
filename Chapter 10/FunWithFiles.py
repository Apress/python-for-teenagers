
# This code is used to open a file
# However, since the file does not already exist
# Python instead creates it for us
newFile = open("CreatedFile.txt", 'w')

# This code is similar to a print() statement
# However, instead of writing text or output to a user's computer screen
# It writes it to a file instead
newFile.write("Look, we created a brand new file using Python code!\n")
newFile.write("Here is a second line of text!\n")

# The close() function closes the file we are working on and saves it
# It is important to always close a file when we are finished with it
# To ensure we do not make any additions or mess up the file in anyway
newFile.close()

# Open the file CreatedFile.txt 
read_me_seymour = open("CreatedFile.txt", 'r')

print("THE ORIGINAL TEXT IN THE FILE")
print(read_me_seymour.readline())
print(read_me_seymour.readline())

# Closing the file
read_me_seymour.close()


# Opening the file again to write some text to it
addingToFile = open("CreatedFile.txt", 'a')

# Adding some text to the file in append mode
addingToFile.write("This is new text.")

# Closing the file
addingToFile.close()

# Opening the file yet again, to read it
# Now that we have appended a line

print("THE TEXT IN THE FILE AFTER WE APPEND")
appendedFile = open("CreatedFile.txt", 'r')

# This is another way we can print from a file
# Here we are using a for loop
# And using the keywords in and line to print each line
# In the text file

for line in appendedFile:
    print(line)

# Closing the file again
appendedFile.close()
