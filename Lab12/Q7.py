# Q7. Python program to Find HCF
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = hcf(num1, num2)
    print(f"The HCF of {num1} and {num2} is: {result}")
    return result

if __name__ == "__main__":
    main()