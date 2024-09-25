def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a = b
        b = a + b
    print()

x = int(input("Enter the Fibonacci range: "))
if x < 0:
    print("Please enter a positive number")
else:
    print("The Fibonacci series is: ")
    fibo(x)