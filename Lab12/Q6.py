# Q6. Python program to Find LCM
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is: {result}")
    
if __name__ == "__main__":
    main()