# Q17. Python program to sort a dictionary
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def main():
    d = {'a': 5, 'b': 1, 'c': 9, 'd': 3}
    sorted_dict = sort_dict_by_value(d)
    print("Original Dictionary:", d)
    print("Sorted Dictionary:", sorted_dict)
    return sorted_dict

main()