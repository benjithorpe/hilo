def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2  # same as number = round(number / 2)
        else:
            number = number * 3 + 1
        print(number)


while True:
    try:
        user_input = int(input("Enter number:\n"))
        collatz(user_input)
        break
    except ValueError:
        print("Enter a number!!")

