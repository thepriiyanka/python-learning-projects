import random

def play_madlib():
    print("\n=== Mad Libs Game ===")

    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    stories = [

        f"One day, a {adjective} {noun} decided to {verb} at the {place}. "
        "Everyone laughed very loudly!",

        f"In the middle of the {place}, a {noun} started to {verb}. "
        f"It was the most {adjective} thing anyone had ever seen!",

        f"A {adjective} {noun} went to the {place} to learn how to {verb}. "
        "But things did NOT go as planned!",

        f"Yesterday, a {noun} was spotted at the {place}. "
        f"People said it looked very {adjective} while trying to {verb}.",

        f"At the {place}, a {adjective} {noun} tried to {verb}, "
        "but slipped and everyone started clapping!"
    ]

    final_story = random.choice(stories)

    print("\n--- Your Story ---")
    print(final_story)


def main():
    while True:
        play_madlib()

        again = input("\nDo you want to play again? (yes/no): ").lower()
        
        if again != "yes":
            print("\nThanks for playing! Goodbye")
            break


if __name__ == "__main__":
    main()
