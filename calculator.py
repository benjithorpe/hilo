def calculate(first=0, operator='+', second=0):
    if operator == '+':
        return (first + second)
    elif operator == '-':
        return (first - second)
    elif operator == '*':
        return (first * second)
    elif operator == '/':
        return (first / second)
    else:
        return (f"'{operator}' is an Invalid Operator")


while True:
    try:
        first_num = float(input('Enter first number: '))
        operator = input('Enter arithmetic operator: ')
        second_num = float(input('Enter second number: '))
        break
    except ValueError:
        print('please enter a number')

answer = calculate(first_num, operator, second_num)
print(f'Answer: {answer}')

