import random

people = ["Kris", "Susie", "Ralsei", "Noelle", "Berdly"]
thechosenone = random.choice(people)

print(people) # for debugging only
print(thechosenone)
people.remove(thechosenone)
print(people) # for debugging only