guests = ['Mr. Dorian', 'Mr. David', 'Mr. Moen', 'Mr. Roberts']

print("Hello, " + guests[0] + ". I would like to invite you to dinner.")
print("Hello, " + guests[1] + ". I would like to invite you to dinner.")
print("Hello, " + guests[2] + ". I would like to invite you to dinner.")
print("Hello, " + guests[3] + ". I would like to invite you to dinner.")

print("I found a bigger dinner table!!!")

guests.insert(0, 'Mr. Depp')
guests.insert(3, 'Mr. Andrei')
guests.append('Mr. Schafer')

print("Hello, " + guests[0] + ". I would like to invite you to dinner.")
print("Hello, " + guests[1] + ". I would like to invite you to dinner.")
print("Hello, " + guests[2] + ". I would like to invite you to dinner.")
print("Hello, " + guests[3] + ". I would like to invite you to dinner.")
print("Hello, " + guests[4] + ". I would like to invite you to dinner.")
print("Hello, " + guests[5] + ". I would like to invite you to dinner.")
print("Hello, " + guests[6] + ". I would like to invite you to dinner.")

print("I'm sorry, I can only invite two people for dinner!")
print("Sorry, " + guests.pop() + ". I can't invite you to dinner")
print("Sorry, " + guests.pop() + ". I can't invite you to dinner")
print("Sorry, " + guests.pop() + ". I can't invite you to dinner")
print("Sorry, " + guests.pop() + ". I can't invite you to dinner")
print("Sorry, " + guests.pop() + ". I can't invite you to dinner")
# print("Sorry, " + guests.pop() + ". I can't invite you to dinner")

print("You are still invited, " + guests[0])
print("You are still invited, " + guests[1])

del guests[0]
del guests[0]
print(guests)
