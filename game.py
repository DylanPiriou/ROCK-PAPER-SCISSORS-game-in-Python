import random

play = True

while play:
    game_options = ("rock", "paper", "scissors")
    computer_choice = random.choice(game_options)
    player_choice = None

    # check for valid user inputs
    while player_choice not in game_options:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Paper covers rock! You lose.")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Scissors cut paper! You lose.")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Rock break scissors! You lose.")
    else:
        print("You won! GG")

    choice = None
    choice_options = ("y", "n")
    while choice not in choice_options:
        choice = input("Do you want to continue ? (y/n): ")

        if not choice == "y":
            play = False

print("Thanks for playing! See ya")