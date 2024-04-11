dinner_guests = ['Tina Fey', 'Amy Poehler', 'Kristen Wiig']
invites_intro = 'Current guest list invites:'
print(invites_intro)
for guest in dinner_guests:
    print(f"\t{guest}, you are cordially invited to dinner.")
print()

ex_guest = dinner_guests.pop()
new_guest = 'Julia Louis-Dreyfus'
print(f"{ex_guest} can no longer attend the dinner.")
dinner_guests.append(new_guest)
print(invites_intro)
for guest in dinner_guests:
    print(f"\t{guest}, you are cordially invited to dinner.")

print()

print("We found a bigger dinner table!")
print()

dinner_guests.append("Will Ferrel")
dinner_guests.append("Steve Carrel")
dinner_guests.append('Paul Newman')
print(invites_intro)
for guest in dinner_guests:
    print(f"\t{guest}, you are cordially invited to dinner.")
print()

print("The table won't arrive in time so we only have room for two dinner guests.")
print()

ex_guest = dinner_guests.pop()
print(f"{ex_guest} you are no longer invited to dinner.")
ex_guest = dinner_guests.pop()
print(f"{ex_guest} you are no longer invited to dinner.")
ex_guest = dinner_guests.pop()
print(f"{ex_guest} you are no longer invited to dinner.")
ex_guest = dinner_guests.pop()
print(f"{ex_guest} you are no longer invited to dinner.")
print()

for guest in dinner_guests:
    print(f"{guest}, you are still invited to dinner.")
print()

del dinner_guests[1]
del dinner_guests[0]
print(dinner_guests)