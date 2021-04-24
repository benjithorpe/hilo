cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()  # sorts the list permanently
print(cars)

cars.sort(reverse=True)  # sorts the list in reverse order
print(cars)

cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars2)

print("\nHere is the sorted list:")
print(sorted(cars2))  # sorted() sorts the list temporarily

print("\nHere is the original list again:")
print(cars2)

cars2.reverse() # reverse the order of the list !(it does not sort the list)!
print(cars2)

print(len(cars2)) # prints the length of the list




