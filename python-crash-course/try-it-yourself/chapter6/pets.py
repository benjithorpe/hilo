pets = [
    {'animal': 'dog', 'owner': 'jack'},
    {'animal': 'cat', 'owner': 'joe'},
    {'animal': 'horse', 'owner': 'patrick'},
    {'animal': 'monkey', 'owner': 'martin'},
    {'animal': 'sea horse', 'owner': 'lewis'},
]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']}")
