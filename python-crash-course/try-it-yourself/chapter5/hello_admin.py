usernames = ['abu', 'john', 'jack', 'jane', 'jenny', 'mike', 'bucky', 'admin', 'jaden']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
