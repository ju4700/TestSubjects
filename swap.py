"""x = int(input("Enter: "))
y = int(input("Enter: "))

x, y = y, x
print(x, y)"""

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
s = input("Enter: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")

"""def largest(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

n1 = int(input("Enter: "))
n2 = int(input("Enter: "))
n3 = int(input("Enter: "))

l = largest(n1, n2, n3)
print("the largest number is: ", l)"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
a = int(input("Enter: "))
b = int(input("Enter: "))
print("GCD is: ", gcd(a, b))

"""def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("Enter: "))
b = int(input("Enter: "))
print("LCM is: ", lcm(a, b))"""

def cel_to_fah(c):
    return c * 9/5 + 32

c = float(input("Enter: "))
print("Fahrenheit: ", cel_to_fah(c))

"""import random

def gen_ran(x, y):
    return random.randint(x, y)

x = int(input("Enter: "))
y = int(input("Enter: "))
print("Random number: ", gen_ran(x, y))"""

def sum_of_n(n):
    return n * (n + 1) // 2

n = int(input("Enter: "))
print("Sum of n natural numbers: ", sum_of_n(n))

"""def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count

s = input("Enter: ")
print("Vowels: ", count_vowels(s))"""

import string
def remove_punc(s):
    t = s.maketrans("", "", ".,;:!?")
    return t

s = input("Enter: ")
print("Without punctuation: ", s.translate(remove_punc(s)))

"""c = input("Enter: ")
print("ASCII value: ", ord(c))"""

n = int(input("Enter: "))

r_n = 0
while n != 0:
    d = n % 10
    r_n = r_n * 10 + d
    n //= 10
print("Reverse: ", r_n)