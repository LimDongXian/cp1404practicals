MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

EXCELLENT_SCORE = 90
PASSING_SCORE = 50


def main():
    score = 0  # added to prevent error when printing result without getting score
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(0, 100, "Enter yours score(0~100): ")
        elif choice == "P":
            grade = identify_grade(score)
            print(f"Your score is {score} and it's {grade}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score(low, high, prompt):
    score = int(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = int(input(prompt))
    return score


def identify_grade(score):
    """Identify the grade based on the score."""
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSING_SCORE:
        return "Passable"
    else:
        return "Bad"


main()
