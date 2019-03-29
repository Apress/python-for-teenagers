superPowers = ['flight', 'cool cape', '20/20 vision', 'Coding Skillz']
superWeaknesses = ['bologna', 'lactose intolerance', 'social settings', 'tight trunks']

print("Behold our fledgling hero/sidekick, \"Wonder Boy!")
print("His super powers include:", *superPowers)
print("And his weaknesses are:", *superWeaknesses)

del superWeaknesses[1]

superWeaknesses.insert(1,'Taco Meat')

print(*superWeaknesses)
