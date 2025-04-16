# Q15. Python program to create a dictionary
telephone_directory = {
    "John": "123-456-7890",
    "Jane": "987-654-3210",
    "Alice": "555-555-5555",
    "Bob": "444-444-4444"
}

def print_telephone_directory(directory):
    for name, number in directory.items():
        print(f"{name}: {number}")

print_telephone_directory(telephone_directory)