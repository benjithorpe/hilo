favorite_places = {
    'sparrow': ['scotland', 'sychelles'],
    'isaac': ['england', 'scotland', 'madagascar'],
    'benji': ['silicon valley']
}

for name, places in favorite_places.items():
    if len(places) < 2:
        print(f"{name.title()}'s favorite place is:")
    else:
        print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
    print()
