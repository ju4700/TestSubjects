# 31. Merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

my_d = dict1.copy()
md.update(dict2)

# 32. Remove item from dictionary
def remove_item(d, key):
    d.pop(key, None)
    return d

# 33. Lambda function example (square of a number)
square = lambda x: x ** 2

# 34. Sort dictionary by value
def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# 35. Character frequency counter
def char_frequency(s):
    return dict(Counter(s))