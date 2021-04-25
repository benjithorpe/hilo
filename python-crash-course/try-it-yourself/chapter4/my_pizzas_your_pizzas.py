pizzas = ['cheese pizza', 'small pizza', 'pepperoni pizza', 'butter pizza']
friend_pizzas = pizzas[:]

pizzas.append("mushroom pizza")
friend_pizzas.append('medium pizza')

print("My favoutite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favoutite pizzas are:")
for freind_pizza in friend_pizzas:
    print(freind_pizza)
