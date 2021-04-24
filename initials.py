name = input("Enter a name to get the Initials: ").strip()

def get_initials(name):
    initials = ''
    for letter in name:
        if letter.isupper():
            initials += letter
    return initials

print("Your Initials is:", get_initials(name))
