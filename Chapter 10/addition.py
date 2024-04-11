message = ''

while message != 'q':
    print('Input q to quit')
    num1 = input("Please provide a number: ")
    if num1 == 'q':
        break
    num2 = input("Please provide another number: ")
    if num2 == 'q':
        break
    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("\nPlease provide actual numbers next time!\n")
    else:
        print(result)