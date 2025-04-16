# Q18. Python program to Merge two Dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def main():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged_dict = merge_dicts(dict1, dict2)
    print("Merged Dictionary:", merged_dict)
    return merged_dict

main()