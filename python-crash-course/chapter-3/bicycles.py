bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)  # prints the whole list

print(bicycles[1])  # prints the second item in the list 
print(bicycles[3])  # prints the fourth item in the list

print(bicycles[-1])  # prints the last item in the list


# == Using values in the list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
