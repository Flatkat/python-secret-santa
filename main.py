import random
import json
import os
import base64

if os.path.exists("db.json"):
    with open ("db.json", "r") as f:
        people = json.load(f)

    thechosenone = random.choice(people)
    thechosenone_bytes = thechosenone.encode("ascii") # Chosen one as raw base64 bytes for decoding
    thechosenone_trans_bytes = base64.b64decode(thechosenone_bytes) # Chosen one, translated, as raw bytes
    thechosenone_trans = thechosenone_trans_bytes.decode("ascii") # Now, as readable text
    
    #print("DEBUGGING: List before: "+ str(people)) # for debugging only

    print("")
    print("You are the secret santa of: "+ thechosenone_trans)
    print("")
    continue_var = input("If you want to proceed, press \"1\". If the name on screen is you, exit the program and try again by pressing \"0\". Then press \"ENTER\": ")

    if(continue_var=="1"):
        print("")
        print("Okay! Here is the name of the person you will be the secret santa of in Base64: "+ thechosenone)
        print("")
        people.remove(thechosenone)
        with open("db.json", "w") as f:
            json.dump(people, f, indent=4)
        print("Done! " + thechosenone_trans + " was removed from the list, now you can share the DB file with the next person!")
        print("Remember to copy the name in Base64 before closing the program if needed!")

    #print("DEBUGGING: List after: "+ str(people)) # for debugging only
else:
    print("File is missing, an example list will be created (program will close afterwards)")
    people = ["S3Jpcw==", "U3VzaWU=", "UmFsc2Vp", "Tm9lbGxl", "QmVyZGx5"]
    with open("db.json", "w") as f:
        json.dump(people, f, indent=4)