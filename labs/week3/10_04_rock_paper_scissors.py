# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

computer_choice = random.randint(1, 3)

# Mapping integers to choices
if (computer_choice == 1):
    computer_choice='rock'
elif(computer_choice == 2):
    computer_choice='paper'
elif(computer_choice==3):
    computer_choice='scissors'
else:
    print("Invalid input")

choice=['rock','paper','scissors']
while True:
   
    # User makes a choice
    user_input = input("Enter rock, paper, or scissors: ").lower()
    if user_input not in choice:
        print("Invalid choice! Please try again")
        continue
    print(computer_choice)
    if user_input==computer_choice:
       print("It's a draw! try again")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
        break
    else:
        print("Computer wins ! Try again")
   