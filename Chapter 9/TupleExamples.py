
# Defining our tuple

villains = ('Eyebrow Raiser', 'Angry Heckler', 'Not So Happy Man', 'The Heck Raiser')

# Printing the items in a tuple
print(villains)

# Printing single items in a tuple

print(villains[0])
print(villains[1])
print(villains[2])
print(villains[3])

# Ways to append tuple items to sentences

print("The first villain is the sinister", villains[0])
print("The second villain is the terrifying " + villains[1])

# Slicing starting at index 0 and ending before the item at index 3
print(villains[0:3])

# Slicing starting at index 1 and ending before the item at index 4
print(villains[1:4]) 

# Creating a tuple of my purple capes
purpleCapes = ('Purple Frilly Cape', 'Purple Short Cape', 'Purple Cape with Holes In It')
# Creating a tuple of my Polka Dot capes
polkaCapes = ('Black and White Polka Dot Cape', 'White and Beige Polka Dot Cape', 'Blue Polka Dot Cape Missing the Blue Polka Dots')

# Concatenating - or adding - my two tuples of capes together into a new tuple
allMyCapes = (purpleCapes + polkaCapes)

# Printing out the values of the newly created tuple
print(allMyCapes)

# Print the item listed at index 1, 3 times
print(allMyCapes[1] * 3)


# Create a tuple containing a set of numbers
lowest_value = (1, 5, 10, 15, 20, 50, 100, 1000)

# Use the minimum function to return the lowest value item in the tuple
print(min(lowest_value))

# Create a tuple containing a set of numbers
highest_value = (1, 5, 10, 15, 20, 50, 100, 1000)

# Use the maximum function to return the highest value item in the tuple
print(min(highest_value))

# Create a tuple with some items

super_hair = ('Super Stache', 'Macho Beard', 'Gargantuan Goat-tee', 'Villainous Toupee', 'Unfortunate Baldness')

# Print out the number of items in our tuple
print(len(super_hair))

# A tuple of Villains Locked Away in the Villainous Vault of Bad Guys
villains = ('Naughty Man ', 'Skid Mark ', 'Mister Millenial ', 'Jack Hammer ', 'The Spelling Bee ', 'Drank All The Milk Man ', 'Wonder Wedgie ', 'Escape Goat')

# Print out a sorted list of our villains tuple

print(sorted(villains))

# A tuple of numbers we are going to sort
numbers_sort = (10, 20, 5, 2, 18)

# Sorting numbers in our tuple
print(sorted(numbers_sort))

# A tuple of numbers we are going to sum
numbers_sum = (10, 20, 5, 2, 18)

# Summing items in a tuple
print(sum(numbers_sum))

# A list we will convert to a tuple
villainList = ['Naughty Man ', 'Skid Mark ', 'Mister Millenial ', 'Jack Hammer ', 'The Spelling Bee ', 'Drank All The Milk Man ', 'Wonder Wedgie ', 'Escape Goat']

# Using tuple() to convert villainList to a tuple

tuple(villainList)

# A string we will convert to a tuple
villain1 = "Mustached Menace!"
tuple(villain1)

# A tuple full of facial hair styles for villains and heroes
facial_hair = ('Super Stache', 'Macho Beard', 'Gargantuan Goat-tee', 'Face Mullet',)

# Printing out facial hair
print(facial_hair)

# Using del to delete a tuple entirely
del facial_hair

# Printing out facial_hair to show that it is now empty
# print(facial_hair)

# Tuple containing all of the letters used to spell Missisisippi
state = ('M', "i", "s", "s", "i", "s", "i", "s", "i", "p", "p", "i")

# Count the number of times "i" appears in our tuple and print out the result
print("There are this many of the letter i in Missisisippi: ")
print(state.count('i'))

# Count the number of times "s" appears in Missisisippi
print("There are this many of the letter s in Missisisippi: ")
print(state.count('s'))

# Checking to see if "z" or "i" appears in our state tuple
print('z' in state)
print('i' in state)

# Looping through the previouisly created villainList tuple and printing out each item
for var in villainList:
    print(var)





