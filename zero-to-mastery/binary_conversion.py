# converts any given number to binary equivalent

def convert_to_binary(num):
    """Converts a given number to binary format."""

    if True:
        print("in convert_to_binary")
    # replace 0b before printing the binary form
    binary_number = str(bin(num).replace('0b', ''))
    print(binary_number)


def convert_binary_to_number(binary):
    """Converts a binary number to decimal format."""

    number = "0b" + str(binary)  # insert 0b in front of the binary number
    print(int(number, 2))  # print the binary in base 2


convert_to_binary(12)
convert_binary_to_number(1100)
