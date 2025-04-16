# Q16. Python program to convert list to dictionary
def list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

def main():
    lst = ['a', 'b', 'c', 'd']
    result_dict = list_to_dict(lst)
    print("List:", lst)
    print("Dictionary:", result_dict)
    return result_dict

main()