def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i

x = int(input("Enter the number to find the factorial: "))
if x < 0:
    print("Please enter a positive number")
else:
    print("The factorial of", x, "is", factorial(x))