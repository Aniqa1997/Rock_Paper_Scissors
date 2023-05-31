import random

options = ["Rock", "Paper", "Scissors"] #putting in the options

#then we need to add players choice
player_choice = input("Pick between rock, paper or scissors: ")

#now adding computers choice
computers_choice = random.choice(options)

#now creating the solution
if player_choice == computers_choice:
    print("It's a tie")
elif (
    (player_choice == "Rock" and computers_choice == "Scissors") or 
    (player_choice == "Scissors" and computers_choice == "Paper") or 
    (player_choice == "Paper" and computers_choice == "Rock")
    ):
    print("You win!")
else:
    print("Computer wins!")
    