sandwich_orders = ['tomato', 'pb&j', 'cheese']
finished_sandwiches = []

for order in sandwich_orders:
    print(f"You're order is {order.title()}.")
    finished_sandwiches.append(order)

print("List of sandwiches made:")
print(finished_sandwiches)