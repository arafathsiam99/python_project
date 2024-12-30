print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "Graphics Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "Power Supply Unit":
    print("Correct!")
else:
    print("Incorrect!")
