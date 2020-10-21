# A basic chatbot
def username():
    while True:
        name = input('Please, what is your name.\n')

        if name.isalpha():
            print(f'What a great name you have, {name.capitalize()}!')
            break


def guess_age():
    print('\nLet me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    while True:
        try:
            rem3 = int(input('remainder of your age divide by 3: '))
            rem5 = int(input('remainder of your age divide by 5: '))
            rem7 = int(input('remainder of your age divide by 7: '))
            break
        except ValueError:
            print('please enter a number')

    # formula to calculate and guess the age
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"You are {age} years old, a good age to start programming")


def count():
    print('\nI can count to any number you want.')
    while True:
        try:
            number = int(input('Enter any number: '))
            for i in range(number + 1):
                print(f'\t{i} !')
            break
        except ValueError:
            print("I can't count letters")


def test():
    print("""
Let's test your programming knowledge.
Why do we use methods/functions?

    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
    """)

    while True:
        try:
            answer = int(input('> '))
            if answer == 2:
                break
            print('wrong answer, try again')
        except ValueError:
            print('enter a number')


print("""
Hello! My name is Orion.
I was created in 2020.
""")

username()
guess_age()
count()
test()

input('Completed, have a nice day!')
