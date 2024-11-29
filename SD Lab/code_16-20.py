# 16. Count vowels in a string
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

# 17. Remove punctuation from a string
import string
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# 18. ASCII value of a character
def ascii_value(char):
    return ord(char)

# 19. Reverse a number
def reverse_number(num):
    return int(str(num)[::-1])

# 20. Find the second largest number in a list
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None