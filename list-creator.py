import random
import json
import os

print("WARNING: Please, before running this script make sure there is no \"db.json\" file in the same directory as this script")
print("")
print("Input a list following Python's format, with its elements encoded in Base64, here you have an example: ")
print("[\"S3Jpcw==\", \"U3VzaWU=\", \"UmFsc2Vp\", \"Tm9lbGxl\", \"QmVyZGx5\"]")
print("")
print("Send a single \"0\" to finish appending elements to the list ")
print("")

people = []
continue_var = True

while continue_var == True:
    input_var = input()
    if input_var == "0" :
        continue_var = False
        print("Stopping!")
    else:
        people.append(input_var)
        print("Got it!")

print(people) #debugging only
random.shuffle(people)
print(people) #debugging only

if os.path.exists("db.json"):
    print("A db.json file already exists, please, first remove it, then run this program again")
else:
    with open("db.json", "w") as f:
        json.dump(people, f)