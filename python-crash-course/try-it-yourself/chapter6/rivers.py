rivers = {
    'nile': 'egypt',
    'mano': 'africa',
    'jordan': 'isreal'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers in the dictionary:")
[print(river.title()) for river in rivers.keys()]

print("\nCountries in the dictionary:")
[print(country.title()) for country in rivers.values()]
