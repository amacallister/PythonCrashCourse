def make_sandwich(*items):
    print("\nThe sandwich will contain:")
    for item in items:
        print(f"- {item}")

make_sandwich('butter')
make_sandwich('peanut butter', 'jelly')
make_sandwich('bacon', 'lettuce', 'tomato')