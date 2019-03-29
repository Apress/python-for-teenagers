import random



class Superhero():

    def __init__(self, superName, power, braun, brains, stamina, wisdom, constitution, dexterity, speed):
        superName = " "
        power = " "
        self.braun = braun
        self.brains = brains
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed

        braun = random.randint(1,20)
        brains = random.randint(1,20)
        stamina = random.randint(1,20)
        wisdom = random.randint(1,20)
        constitution = random.randint(1,20)
        dexterity = random.randint(1,20)
        speed = random.randint(1,20)

class Mutant(Superhero):
    print("Hello!")
    brains = brains + 10
    

"""
class Superhero:
    def init(self, superName, power, brains, braun, stamina, wisdom, constitution, dexterity, speed):
        self.power = power
        self.braun = braun
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed
        self.brains = brains

    def stats(self):
        self.brains = 20
        

class Mutant(Superhero):
    print("I am a mutant!")
"""


print("Please enter your super hero name: ")
hero3 = Mutant()
hero3.superName = input()
print("Your name is %s." % (hero3.superName))
print("Your new stats are:")
print("")
print("Brains: ", hero3.brains)
print("")



        
"""        
print(help(superHero))

print(help(mutant))
"""
