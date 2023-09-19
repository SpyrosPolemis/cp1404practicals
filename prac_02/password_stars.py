password = input("Enter password: ")
minimum_password_length = 5
while len(password) < minimum_password_length:
    print(f"Password length too short, needs to be at least {minimum_password_length} characters long.")
    password = input("Enter password: ")
for i in range(len(password)):
    print("*", end="")
