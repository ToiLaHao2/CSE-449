# Q19. Binary Search in Python
def binary_search(arr, target):
   low, high = 0, len(arr) - 1
   while low <= high:
       mid = (low + high) // 2
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           low = mid + 1
       else:
           high = mid - 1
   return -1
        
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 71
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
    return result

main()