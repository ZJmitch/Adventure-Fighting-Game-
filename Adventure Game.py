#Fighting Adventure Game
#Intro
name = input("What is your name? ")


start = input("Are you ready to start playing(Y or N)? ")
if start == "Y":
        print("Okay lets begin")
else:
        print("Restart the game when you are ready to play.")
        exit()
#Chapter 1
        
print("It was a blistering hot summer day, the humidity makes it hard to breathe")
print("You are interesting in your local fighting gym and you start heading that direction")



answer = input("would you like to continue playing(Y or N)? ")
if answer == "Y":
        print("Okay, lets continue")
else:
        print("The game has ended, goodbye!")
        exit()


#Chapter 2

print("Entering the new fighting gym you are greeted with open arms and wide smiles")
print("You walk into the new fighting Gym and feel at home")

print("A fighter has approached you and asks if you would like to fight.")

fight = input("would you like to fight him(Y or N)? ")
if fight == "Y":
        print("You did well in your first fight, but you have a lot to improve on")
else:
        print("Come back when you are ready to fight.")
        exit()

answer = input("would you like to continue playing(Y or N)? ")
if answer == "Y":
        print("Okay, lets continue")
else:
        print("The game has ended, goodbye!")
        exit()



#Chapter 3


print("Training in the new gym you can hear pads being struck by thunder, and loud music blasts as a class is in session")

print("You begin training with your new fighting team")

print("It is time to sharpen your fighting skills again")


fight = input("would you like to fight(Y or N)? ")
if fight == "Y":
        print("You are improving and almost ready to fight in a professional fight!")
else:
        print("Come back when you are ready to fight.")
        exit()


answer = input("would you like to continue playing(Y or N)? ")
if answer == "Y":
        print("Okay, lets continue")
else:
        print("The game has ended, goodbye!")
        exit()

#Chapter 4
print("Bright lights, a booming loud crowd, and cheers that shake the stadium")
print(name,"welcome to the fighting arena for the first time")

print("This is your first professional fight")

fight = input("Are you ready to fight(Y or N)? ")
if fight == "Y":
        print("You knocked out your opponent and won your first fight!")
else:
        print("Come back when you are ready to fight.")
        exit()

answer = input("would you like to continue playing(Y or N)? ")
if answer == "Y":
        print("Okay, lets continue")
else:
        print("The game has ended, goodbye!")
        exit()


#Chapter 5

print(name,"You finally made it to the Championship Title fight!")
        
print("Thousands of people are cheering your name, all eyes are focused on you, the intensity sucks the air out of the room")

fight = input("This fight is for the championship, are you ready to fight(Y or N)? ")
if fight == "Y":
        print("It was a close fight but you won, congratulations!", name)
else:
        print("Come back when you are ready to fight.")
        exit()


print("The game has ended, thank you for playing!", name)



