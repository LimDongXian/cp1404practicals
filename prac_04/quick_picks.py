import random

MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1
NUMBERS_PER_PICK = 6

number_pick = int(input("How many quick picks? "))
for i in range(number_pick):
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if random_number not in numbers:
            numbers.append(random_number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
