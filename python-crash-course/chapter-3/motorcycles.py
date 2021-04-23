motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifies the first item in the list
motorcycles[0] = 'ducati'
print(motorcycles)

# adding new item to the list
motorcycles.append('tvs')
print(motorcycles)

# adding items to an empty list
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')

print(motorcycles2)


# insert elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list

## using del keyword
del motorcycles[1]
print(motorcycles)

## using the pop method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

## remove an item by value
motorcycles.remove('ducati')
print(motorcycles)
