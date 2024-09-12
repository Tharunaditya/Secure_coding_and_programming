# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
name=str(input("Please enter your name:"))
message= f"Greetings ! {name}"
print(message)
while True:
    door=int(input("Please choose a door left(1) & right(2):"))
    if door==1:
        print("You chose Left room it is empty here !!")
        option=int(input("Do you want to go back and see there in you need to enter 1 if not 2 :"))
        if option==1:
            break
        else:
            print("Ok you are still here !")
            option2=int(input("Okay do you want to look arround here atleast enter 1 to choose this option: "))
            if option2==1:
                option3=int(input("Hurray you found a sword in here Enter 1 to take, 2 to ignore:"))
                if option3==1:
                    print("You have the sword you can fight with dragon")
                else:
                    print("You do not have sword you can't go back to the other room")
                    option4=int(input("To go back choose 1, if not 2"))
                    if option4==1:
                        break
                    else:
                        print("Your are still here with your sword")
    elif door==2:
        print("You chose Right room, You have encounter a dragon")
        if option3
        option=int(input("Do you want to go back and see there in you need to enter 1 if not 2 :"))
        if option==1:
            break
        else:
            print("Ok you are still here !")