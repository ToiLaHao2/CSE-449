# Q4. Python program to generate a random number
import random
import time

def generate_random_number():
    return random.randint(1, 100)

def main():
    print("Welcome to the Random Number Generator!")
    time.sleep(1)
    print("Generating a random number between 1 and 100...")
    time.sleep(2)
    random_number = generate_random_number()
    print(f"The generated random number is: {random_number}")
    time.sleep(1)
    print("Thank you for using the Random Number Generator!")
    time.sleep(1)

if __name__ == "__main__":
    main()