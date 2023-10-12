"""
emails
Estimated: 30
Actual: 30m 9 seconds

get email
while email != blank
    extract_name
    get name correct
    if name correct
        dict[name] = name
    else
        get name
        dictname = name
print dict
"""


def main():
    """Program to extract users' names from email"""
    email = input("Email: ")
    name_to_email = {}
    while email != "":
        name = extract_name(email)
        is_actual_name = input(f"Is your name {name}? [Y/n] ").lower()
        if is_actual_name != "y" and is_actual_name != "":  # Prac instruction say enters "Y" but sample is diff
            name = input("Name: ")
        name_to_email[name] = email
        email = input("Email: ")
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def extract_name(email):
    names = email[:email.index("@")].split(".")  # takes everything before the @ and turns it into a list split by .
    full_name = " ".join(names).title()
    return full_name


def test_functions():
    print(f"Should return Spyros Polemis: {extract_name('spyros.polemis@gmail.com')}")


# test_functions()
main()
