filename = 'programming.txt'
message = ''

while message != 'quit':
    message = input('Why do you like programming? ')

    with open(filename, "a") as file_object:
        file_object.write(f"{message}\n")