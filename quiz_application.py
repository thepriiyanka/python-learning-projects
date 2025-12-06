def run_quiz():
    print("===== QUIZ APPLICATION =====\n")

    questions = {
    "1. What is the output of print(2 * 3 + 4)?\n(a) 10\n(b) 14\n(c) 12": "a",

    "2. Which of the following is a valid variable name?\n(a) 2name\n(b) name_1\n(c) name-1": "b",

    "3. What is the data type of 5.0?\n(a) int\n(b) float\n(c) string": "b",

    "4. What will this print: print('Hello' * 2)?\n(a) HelloHello\n(b) Hello Hello\n(c) Error": "a",

    "5. What does len('Python') return?\n(a) 5\n(b) 6\n(c) 7": "b",

    "6. What is the output of [1,2,3][::-1]?\n(a) [3,2,1]\n(b) [1,2,3]\n(c) Error": "a",

    "7. Which method adds an item to a list?\n(a) push()\n(b) append()\n(c) add()": "b",

    "8. What is the output: print(bool(0))?\n(a) True\n(b) False\n(c) None": "b",

    "9. What will print('hello'.upper()) output?\n(a) HELLO\n(b) hello\n(c) Error": "a",

    "10. Which operator is used for exponentiation?\n(a) ^\n(b) **\n(c) //": "b"
}


    score = 0

    for question, correct_answer in questions.items():
        print("\n" + question)
        answer = input("Your answer (a/b/c): ").lower()

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is '{correct_answer}'.")

    print("\n===== QUIZ COMPLETED =====")
    print(f"Your Final Score: {score} / {len(questions)}")

    if score == len(questions):
        print("Excellent! Perfect score!")
    elif score >= len(questions) // 2:
        print("Good job!")
    else:
        print("Keep practicing!")

if __name__ == "__main__":
    run_quiz()
