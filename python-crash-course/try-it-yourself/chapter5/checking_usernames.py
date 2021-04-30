current_users = ['abu', 'john', 'jack', 'jane', 'jenny', 'mike', 'bucky', 'jaden']
new_users = ['johnny', 'jackue', 'michael', 'mike', 'jaden']

for user in new_users:
    if user.lower() in current_users:
        print("Username is not available.")
    else:
        print("Username is available.")
