import random

def number_guessing_game():
    print("\n===== ADVANCED NUMBER GUESSING GAME =====")

    score = 0  # total score for the session

    while True:
        print("\nChoose Difficulty Level:")
        print("1. Easy   (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard   (1-200, 5 attempts)")

        choice = input("Enter 1/2/3: ")

        if choice == "1":
            limit = 50
            attempts_allowed = 10
        elif choice == "2":
            limit = 100
            attempts_allowed = 7
        elif choice == "3":
            limit = 200
            attempts_allowed = 5
        else:
            print("Invalid choice! Please select again.\n")
            continue

        secret_number = random.randint(1, limit)
        attempts_used = 0

        print(f"\nI have selected a number between 1 and {limit}.")
        print(f"You have {attempts_allowed} attempts to guess it.")

        while attempts_used < attempts_allowed:
            try:
                guess = int(input(f"\nAttempt {attempts_used+1}: Enter your guess: "))
                attempts_used += 1

                if guess < secret_number:
                    print("⬇ Too Low!")
                elif guess > secret_number:
                    print("⬆ Too High!")
                else:
                    print(f"🎉 Correct! You guessed it in {attempts_used} attempts.")
                    earned = (attempts_allowed - attempts_used + 1) * 10  # scoring logic
                    score += earned
                    print(f"🏆 You earned {earned} points! Total Score: {score}")
                    break

            except ValueError:
                print("Invalid input! Please enter a number only.")

        else:
            print("\n❌ Out of attempts!")
            print(f"The correct number was: {secret_number}")
        
        play_more = input("\nPlay again? (yes/no): ").lower()
        if play_more != "yes":
            print(f"\nThank you for playing! 🎮 Final Score: {score}")
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    number_guessing_game()
