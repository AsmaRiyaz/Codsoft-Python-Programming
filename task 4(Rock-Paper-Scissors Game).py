import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    print("\nWelcome to Rock-Paper-Scissors!")
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

    return winner

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    while True:
        winner = play_game()

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScores: You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Rock-Paper-Scissors! Goodbye!")
            break

if __name__ == "__main__":
    main()
