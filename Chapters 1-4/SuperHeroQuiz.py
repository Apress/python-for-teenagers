
# Variable representing Wonder Boy's Test Score

wonderBoyScore = 100

# Introduction text

print("Congratulations on finishing your Super-Hero Quiz Intelligence/Reasoning Test.")
print("Or, S.Q.U.I.R.T. for short.")
print("Let's see if you passed or failed your exam!")
print("A passing grade means you are licensed to be a Sidekick!")

# Comparison block to see if Wonder Boy passed his S.Q.U.I.R.T. Exam

if wonderBoyScore > 60:
    print("Here are your results: ")

    if wonderBoyScore > 60 and wonderBoyScore < 70:
        print("Well, you passed by the skin of your teeth!")

    elif wonderBoyScore >= 70 and wonderBoyScore <= 80:
        print("You passed...average isn't so bad. I'm sure you'll make up for it with heart.")

    elif wonderBoyScore >= 80 and wonderBoyScore <= 90:
            print("Wow, not bad at all! You are a regular B+ Plus player!")

    elif wonderBoyScore >= 90:
            print("Look at you! Top of your class. Yer a regular little S.Q.U.I.R.T. if I ever saw one!")
        
else:
        print("Nice try fella, but I'm sorry you didn't pass.")
        print("I hear the Burger Blitz needs a security guard - you are a shoo-in!")


