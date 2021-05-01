favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}.")

'''
# prints the names (keys) in the dictionary
for name in favorite_languages.keys():
    print(name.title())
'''

'''
# checks for values in another list
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
'''

'''
# sort the list before looping and printing the key
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
'''

print("The following languages have been mentioned:")
# removes duplicate items from the dictionary keys
for language in set(favorite_languages.values()):
    print(language.title())
