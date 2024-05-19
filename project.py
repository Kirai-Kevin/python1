def main():
    print("Welcome to the Quiz!")

    total_marks = 0

    total_marks += ask_question("What is 100 * 0.5?", "50", 10)
    total_marks += ask_question("What is 2 + 2?", "4", 10)
    total_marks += ask_question("What is 99 / 3?", "33", 10)
    total_marks += ask_question("What is 100 - 11?", "89", 10)

    print(f"Total Marks: {total_marks}")

    remarks(total_marks)

def ask_question(question, correct_answer, marks):
    answer = input(question + " ")
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        return marks
    else:
        print("Incorrect.")
        return 0

def remarks(total_marks):
    if total_marks >= 40:
        print("Excellent job! You got an A")
    elif total_marks >= 30:
        print("Great job! You got a B")
    elif total_marks >= 20:
        print("Good job! You got a C")
    elif total_marks >= 10:
        print("You got a D! Work harder")
    else:
        print("You failed! Try again")

    retake_quiz()

def retake_quiz():
    response = input("Do you want to retake the quiz? Y/N: ")
    if response.strip().upper() == "Y":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
