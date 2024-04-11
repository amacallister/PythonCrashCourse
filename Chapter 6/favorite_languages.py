favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#print(f"Sarah's favorite language is {favorite_languages['sarah']}.")

# Loop through all key value pairs:
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite langugage is {language.title()}.")

# Loop through all keys:
print()
for name in favorite_languages.keys():
    print(name.title())

# Loop through dictionary looking for specific values:
print()
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Check if a person was polled:
print()
if 'erin' not in favorite_languages.keys():
    print('Erin, please take out poll!')

# Sort the dictionary keys before listing them:
print()
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Loop through all values in a dictionary:
print()
print(f"The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

new_favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
print()
for name, languages in new_favorite_languages.items():
    print(len(languages))
    if len(languages) != 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        print(languages[0].title())


