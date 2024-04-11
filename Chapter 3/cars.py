cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print()
print(cars)
print(len(cars))