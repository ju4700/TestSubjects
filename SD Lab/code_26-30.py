# 26. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 27. Flatten a nested list
def flatten(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

# 28. Check if a list is empty
def is_empty(lst):
    return len(lst) == 0

# 29. Intersections of two sets
def intersection(set1, set2):
    return set1 & set2

# 30. Print dictionary
def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")