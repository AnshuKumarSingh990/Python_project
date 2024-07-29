import random

def game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(f"\nComputer chose {computer_choice}.")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win this round!")
                user_score += 1
            else:
                print("Paper covers rock! You lose this round.")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win this round!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose this round.")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win this round!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose this round.")
                computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter yes or no: ").lower()
        if play_again != "yes":
            break

    print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("You lose the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    game()
