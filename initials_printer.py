name = input("Enter a name to get the Initials: ").strip()
initials = ''

for letter in name:
    if letter.isupper():
        initials += letter

print("Your Initials is:", initials)
