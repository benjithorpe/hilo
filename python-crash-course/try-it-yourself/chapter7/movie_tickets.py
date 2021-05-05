while True:
    age = input("what is you age? ")
    
    if age < 3:
        print("Ticket is free")
    elif age < 12:
        print("Ticket price is $10")
    else:
        print("Ticket price is $15")
