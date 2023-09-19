"""Password checking program"""

MINIMUM_PASSWORD_LENGTH = 5


def main():
    """Print asterisks equal to password length."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password length too short, needs to be at least {MINIMUM_PASSWORD_LENGTH} characters long.")
        password = input("Enter password: ")
    return password


main()
