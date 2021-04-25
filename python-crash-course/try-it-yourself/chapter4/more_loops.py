my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # copying a list by slicing

# adding new values to the list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for friend_food in friend_foods:
    print(friend_food)
