
# Variables to check

wonderBoyAllowance = 20

newCape = 20
newShoes = 50

# Checks if you can afford a new cape

if wonderBoyAllowance >= newCape:
    print("You can afford a new cape.")
    print("But how about new shoes?")

# If the check to see if you can afford the new cape passes it does this
    if wonderBoyAllowance >= newShoes:

        print("Looks like you can afford new shoes as well.")
        print("That's good, because the old ones are really stinky!")
        print("But can you afford both together?")

#If you cannot afford the shoes, but can afford the cape, it does this
    else:
        print("You can only afford the new cape, sorry.")
            

# If both of the conditionals fail, the else below triggers
# If even one of the conditionals are true, this else does not trigger

else:
    print("That's a shame, because one of them is really stanky!")

