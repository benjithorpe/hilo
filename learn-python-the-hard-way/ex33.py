numbers = []

def add_to_list(num, increment=1):
    i = 0
    while i < num:
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

add_to_list(7)
print("The numbers: ")

for num in numbers:
    print(num)
