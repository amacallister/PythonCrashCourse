rivers = {'nile': 'egypt', 'guadalupe': 'united states', 'rhine': 'france', 'chicago': 'united states'}
for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}")

print("\nHere are all the rivers in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nHere are all the countries in the dictionary:")
for country in set(rivers.values()):
    print(country.title())