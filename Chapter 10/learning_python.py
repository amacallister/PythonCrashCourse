with open('learning_python.txt') as file_object:
        
    # Print the whole file at once.
    print("\nPrint the whole file at once:")
    contents = file_object.read()
    print(contents.rstrip())
    
    # Loop through the lines inside the with block.
    print("\nLoop through the lines inside the with block:")
    for line in file_object:
        print(line.rstrip())

    lines = file_object.readlines()

# Add all the lines to a list and loop through them later.
print("\nAdd all the lines to a list and loop through them later:")
for line in lines:
    print(line.rstrip())