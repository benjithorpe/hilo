def sandwich_items(*items):
    print("\nThese items should be added on the sandwich:")
    for item in items:
        print(f"- {item}")

sandwich_items('mushrooms', 'pepperoni')
sandwich_items('mushrooms', 'pepperoni', 'onions')
sandwich_items('mushrooms')
