cities = {
    'moscow': {
        'country': 'russia',
        'population': 35_000_975,
        'fact': 'A cool country with a lot of fun stuff and ice.',
    },
    'cuba': {
        'country': 'mexico',
        'population': 10_595_000,
        'fact': 'A beautiful city with lots of flowers.',
    },
    'freetown': {
        'country': 'sierra leone',
        'population': 2_000_834,
        'fact': 'A small city with cool people and music.'
    }
}

for city in cities.keys():
    print(city.title())
    print(f"\tCountry: {cities[city]['country'].title()}")
    print(f"\tPopulation: {cities[city]['population']} people.")
    print(f"\tFact: {cities[city]['fact']}")
    print()
