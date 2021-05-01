john = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 25,
    'city': 'panama'
}

jane = {
    'first_name': 'jane',
    'last_name': 'smith',
    'age': 20,
    'city': 'cuba'
}

danny = {
    'first_name': 'danny',
    'last_name': 'cole',
    'age': 10,
    'city': 'rio'
}

people = [john, jane, danny]

for person in people:
    print(f"First Name: {person.get('first_name').title()}")
    print(f"Last Name: {person.get('last_name').title()}")
    print(f"Age: {person.get('age')}")
    print(f"City: {person.get('city').title()}")
    print()
