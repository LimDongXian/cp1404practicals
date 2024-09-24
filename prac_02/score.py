import random


def main():
    score = get_valid_score()
    grade = identify_grade(score)
    print(f"Your score is {score} and it's {grade}")
    random_score = random_number()
    random_grade = identify_grade(random_score)
    print(f"The random score is {random_score} and it's {random_grade}")


def get_valid_score():
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def identify_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def random_number():
    return random.randint(1, 100)


main()
