vacations = {}

while True:
    name = input("\nWhat is your name? ")
    vacation_place = input("Where would you like to go for vacation? ")

    vacations[name] = vacation_place

    quit = input("Want to enter more response? (yes/no) ")
    if quit == 'no':
        break

print()
for name, vacation in vacations.items():
    print(f"{name.title()} wants to visit {vacation.title()} on a vacation.")
