MINIMUM_LENGTH = 6
password = input('Enter password: ')
while len(password) < MINIMUM_LENGTH:
    print(f"Password should be at least {MINIMUM_LENGTH} characters long.")
    password = input('Enter password: ')
print(len(password)* "*")