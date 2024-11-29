# 1. Hello World
print("Hello, World!")

# 2. Sum of two numbers
def sum_two_numbers(a, b):
    return a + b

# 3. Square root of a number
import math
def sqrt_number(num):
    return math.sqrt(num)

# 4. Triangle area (Heron's formula)
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# 5. Even or Odd
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"