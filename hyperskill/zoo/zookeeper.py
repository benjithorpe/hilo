# A program that helps the zookeeper check
# on the animals and see that they're well.
from animals import animals

while True:
    print('\n0.Camel, 1.Lion, 2.Deer, 3.Goose, 4.Bat, 5.Rabbit')
    try:
        habitat = input('Which habitat # do you need? (e to exit) ')
        if habitat.lower() == 'e':
            break

        habitat = int(habitat)  # convert habitat to int
        print(animals[habitat])
    except ValueError:
        print('please enter a number!')
    except IndexError:
        print('number is not available')


print('Good Bye! See you later!')
input('press enter to exit...')
