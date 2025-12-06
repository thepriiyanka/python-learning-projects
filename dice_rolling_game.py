import random

def roll_dice():
    return random.randint(1, 6)

def multiplayer_dice():
    print("=== Multiplayer Dice Rolling Game ===")
    print("Two players will roll the dice. Highest number wins!\n")

    while True:
        input("Player 1, press Enter to roll the dice...")
        p1 = roll_dice()
        print(f"Player 1 rolled: {p1}")

        input("Player 2, press Enter to roll the dice...")
        p2 = roll_dice()
        print(f"Player 2 rolled: {p2}")

        
        if p1 > p2:
            print("\nPlayer 1 Wins!")
        elif p2 > p1:
            print("\nPlayer 2 Wins!")
        else:
            print("\nIt's a Tie!")

        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! Goodbye")
            break

if __name__ == "__main__":
    multiplayer_dice()
