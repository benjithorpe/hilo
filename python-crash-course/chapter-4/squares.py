squares = []

for value in range(1, 11):
    squares.append(value**2)

print(squares)

print("\n== List Comprenhension ==")
squares = [value**2 for value in range(1, 11)]
print(squares)

print("\n===== List functions for numbers =====")
print("Max:", max(squares))  # prints the maximun number in the list
print("Min:", min(squares))  # prints the minimum number in the list
print("Sum:", sum(squares))  # prints the sum of all the numbers in the list
