username = input("What is your name? ")
password = input("Enter a password? ")
hidden_password = '*' * len(password)

print(f"Hey {username}, Your password {hidden_password} is {len(password)} characters long.")
