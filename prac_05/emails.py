"""
emails
Estimated: 30
Actual:

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
    while email != "":
        name = extract_name(email)
        email = input("Email: ")


def extract_name(email):
    names = email[:email.index("@")].split(".")
    full_name = " ".join(names).title()
    return full_name


def test_functions():
    print(f"Should return Spyros Polemis: {extract_name('spyros.polemis@gmail.com')}")


# test_functions()
main()
