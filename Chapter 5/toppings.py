requested_toppings = ['mushrooms', 'extra cheese']

if requested_toppings:
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")

    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")