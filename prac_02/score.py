import random

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_SCORE = 90
PASSING_SCORE = 50


def main():
    """Main function to get and display score and grade."""
    score = get_valid_score()
    grade = identify_grade(score)
    print(f"Your score is {score} and it's {grade}")
    random_score = random_number()
    random_grade = identify_grade(random_score)
    print(f"The random score is {random_score} and it's {random_grade}")


def get_valid_score():
    """Get a valid score from user input."""
    score = float(input("Enter score: "))
    while score > MAXIMUM_SCORE or score < MINIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def identify_grade(score):
    """Identify the grade based on the score."""
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSING_SCORE:
        return "Passable"
    else:
        return "Bad"


def random_number():
    """Generate a random score between 0 and 100."""
    return random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)


main()
