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
    return email[:email.index("@")]



main()
