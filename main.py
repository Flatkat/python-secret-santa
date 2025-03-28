import random
import json
import os

if os.path.exists("db.json"):
    with open ("db.json", "r") as f:
        people = json.load(f)

    thechosenone = random.choice(people)
    
    print("DEBUGGING: List before: "+ str(people)) # for debugging only

    print("")
    print("You are the secret santa of: "+ thechosenone)
    print("")
    print("WARNING: Giving the program any value besides a 0 or a 1 will make it crash")
    continue_var = input("If you want to proceed, press \"1\". If the name on screen is you, exit the program and try again by pressing \"0\". Then press \"ENTER\": ")

    if(continue_var=="1"):
        people.remove(thechosenone)
        with open("db.json", "w") as f:
            json.dump(people, f, indent=4)
        print("Done! " + thechosenone + " was removed from the list, now you can share the DB file with the next person!")

    print("DEBUGGING: List after: "+ str(people)) # for debugging only
else:
    print("File is missing, an example list will be created (program will close afterwards)")
    people = ["Kris", "Susie", "Ralsei", "Noelle", "Berdly"]
    with open("db.json", "w") as f:
        json.dump(people, f, indent=4)