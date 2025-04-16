# Q14. Python program to append element in the list and update list with insertion of elements, removing an element, comparison of two lists, etc
def append_element(lst, element):
    lst.append(element)
    return lst
def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst
def remove_element(lst, element):
    lst.remove(element)
    return lst
def compare_lists(lst1, lst2):
    return lst1 == lst2
def main():
    lst = [1, 2, 3, 4, 5]
    print("Original List:", lst)
    lst = append_element(lst, 6)
    print("List after appending 6:", lst)
    lst = insert_element(lst, 2, 10)
    print("List after inserting 10 at index 2:", lst)
    lst = remove_element(lst, 3)
    print("List after removing 3:", lst)
    lst2 = [1, 10, 2, 4, 5, 6]
    are_equal = compare_lists(lst, lst2)
    print("Are the two lists equal?", are_equal)
    return lst, lst2, are_equal
main()