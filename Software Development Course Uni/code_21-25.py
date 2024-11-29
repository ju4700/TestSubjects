# 21. Sort a list in ascending / descending order
def sort_list(lst, ascending=True):
    return sorted(lst, reverse=not ascending)

# 22. Merge two lists
def merge_lists(lst1, lst2):
    return lst1 + lst2

# 23. Sum of all elements in a list
def sum_elements(lst):
    return sum(lst)

# 24. Common elements of two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 25. Count occurrences of each element in a list
from collections import Counter
def count_occurrences(lst):
    return dict(Counter(lst))