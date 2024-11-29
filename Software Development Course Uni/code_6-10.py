# 6. Prime check
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 7. Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# 8. Factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# 9. Swap two variables
def swap(a, b):
    return b, a

# 10. Palindrome check
def is_palindrome(s):
    return s == s[::-1]