filename = 'guest_book.txt'
name = ''

while name != 'quit':

    name = input("What is your name? ")

    if name == 'quit':
        break

    print(f"Hello {name.title()}!")
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{name.title()}\n")