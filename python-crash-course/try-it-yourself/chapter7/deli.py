sandwich_orders = ['burger', 'ham', 'bacon', 'tuna', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print()
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich is completed.")
