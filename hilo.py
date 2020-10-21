import random


def guess_taken(number_of_guess):
    if number_of_guess > 1:
        print(f'You took {number_of_guess} guesses to win')
    else:
        print(f'You took {number_of_guess} guess to win')


def guess_result():
    guesses = 0

    while True:
        try:
            guess_number = int(input('Guess the number: '))
            guesses += 1

            if guess_number > secret_number:
                print(f'{guess_number} is too high')
            elif guess_number < secret_number:
                print(f'{guess_number} is too low')
            else:
                print(f'{guess_number} is the correct number!')
                break
        except ValueError:
            print('please enter a number')

    guess_taken(guesses)


secret_number = random.randint(1, 100)
print("I'm guessing of a number between 1 and 100")
guess_result()

