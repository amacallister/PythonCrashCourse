favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'andrew', 'perry', 'phil', 'sarah', 'amanda']
for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take the poll.")