requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'french fries']
available_toppings = ['mushrooms', 'pineapple', 'olives', 'green peppers', 'pepperoni', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
