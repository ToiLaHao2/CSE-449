# Q20. Linear Search in Python
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
    return result

main()