filename = 'programming.txt'

name = input("What is your name? ")

with open(filename, 'w') as file_object:
    file_object.write(f"{name.title()}\n")