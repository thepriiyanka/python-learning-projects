import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid Choice! Please enter rock, paper or scissors.")

def find_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    game_rule = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if game_rule[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def play_game():
    print("===== Rock–Paper–Scissors Game =====")
    print("Game Rules:\n\tRock beats Scissors\n\tScissors beats Paper\n\tPaper beats Rock\n")

    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYour choice: {user}")
        print(f"Computer's choice: {computer}")

        result = find_winner(user, computer)

        if result == "user":
            user_score += 1
            print("Result: You Win!")
        elif result == "computer":
            computer_score += 1
            print("Result: Computer Wins!")
        else:
            print("Result: It's a Tie!")

        print(f"Your Score: {user_score}   |   Computer Score: {computer_score}")

        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("\nFinal Scores:")
            print(f"You: {user_score}  |  Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
