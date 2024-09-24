MINIMUM_LENGTH = 6


def main():
    """Get password and print out by start"""
    password = get_password()
    print(len(password) * "*")


def get_password():
    """Get password input with error check"""
    password = input('Enter password: ')
    while len(password) < MINIMUM_LENGTH:
        print(f"Password should be at least {MINIMUM_LENGTH} characters long.")
        password = input('Enter password: ')
    return password


main()
