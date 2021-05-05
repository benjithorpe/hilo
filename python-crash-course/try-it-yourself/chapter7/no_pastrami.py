sandwich_orders = ['burger', 'pastrami', 'ham', 'pastrami', 'bacon', 'pastrami', 'tuna']
finished_sandwiches = []

print("Deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print()
# copy the remaining sandwiches to finished sandwiches
finished_sandwiches = sandwich_orders[:]
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")
