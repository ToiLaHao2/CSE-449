# Q10. Python program to print the elements of an array
def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()
    
def main():
    arr = [1, 2, 3, 4, 5]
    print("Elements of the array:")
    print_array(arr)
    return arr

main()