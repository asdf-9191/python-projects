import random

while True:
    user_input = input("Rock, Paper, or Scissors? (or 'exit' to quit) ")
    if user_input.lower() == 'exit':
        break

    moveset = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(moveset)

    if user_input.lower() == "rock":
        if computer_choice == moveset[0]:
            print("It was a tie! The computer also chose rock.")
        elif computer_choice == moveset[1]:
            print("You lose! The computer chose paper.")
        elif computer_choice == moveset[2]:
            print("You win! The computer chose scissors!")
    elif user_input.lower() == "paper":
        if computer_choice == moveset[1]:
            print("It was a tie! The computer chose paper!")
        elif computer_choice == moveset[2]:
            print("You lose! The computer chose scissors!")
        elif computer_choice == moveset[0]:
            print("You win! The computer chose rock!")
    elif user_input.lower() == "scissors":
        if computer_choice == moveset[2]:
            print("It was a tie! The computer chose scissors!")
        elif computer_choice == moveset[0]:
            print("You lose! The computer chose rock!")
        elif computer_choice == moveset[1]:
            print("You win! The computer chose paper!")
    else:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")