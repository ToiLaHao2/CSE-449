# Q8. Python program to Convert Decimal to Binary, Octal and Hexadecimal 
def convert_decimal(number):
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)
    return binary, octal, hexadecimal


def main():
    number = int(input("Enter a decimal number: "))
    binary, octal, hexadecimal = convert_decimal(number)
    print(f"Binary: {binary[2:]}")
    print(f"Octal: {octal[2:]}")
    print(f"Hexadecimal: {hexadecimal[2:].upper()}")
    return binary, octal, hexadecimal

main()
