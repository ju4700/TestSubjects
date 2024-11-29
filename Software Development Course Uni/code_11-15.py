# 11. Find the maximum and minimum in a list
def max_min(numbers):
    return max(numbers), min(numbers)

# 12. GCD and LCM
import math
def gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return gcd, lcm

# 13. Temperature conversion (Celsius to Fahrenheit and vice versa)
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# 14. Generate a random number
import random
def random_number(start, end):
    return random.randint(start, end)

# 15. Sum of a list
def sum_list(lst):
    return sum(lst)