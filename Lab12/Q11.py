# Q11. Python program to print the element of an array in reverse order
def print_array_reverse(arr):
    for element in reversed(arr):
        print(element, end=" ")
    print()
    
def main():
    arr = [1, 2, 3, 4, 5]
    print("Elements of the array in reverse order:")
    print_array_reverse(arr)
    return arr

main()