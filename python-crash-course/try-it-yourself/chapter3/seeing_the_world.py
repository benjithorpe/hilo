places = ['Scotland', 'UK', 'Madagascar', 'Alaska', 'Schyelles']

print("Original Order:\n", places)

print("\nSorted:\n", sorted(places))
print(places)

print("\nSorted in Reverse:\n", sorted(places, reverse=True))
print(places)

places.reverse()
print("\nAfter Reverse:\n", places)

places.reverse()
print("\nReverse to Original:\n", places)

places.sort()
print("\nSort Permanently:\n", places)

places.sort(reverse=True)
print("\nSort Permanently in Reverse:\n", places)
