import math
#from math import sqrt
def sayhelo():
    print("Hello 'World!'")
    print("Hello World")
def summation(x, y):
    return x+y
def sqroot (n):
    if(n < 0):
        print("Square root not possible!")
    else:
        return math.sqrt(n)
def tri(a, b, c):
    if a**2 == b**2+c**2:
        return 0.5*b*c
    else:
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5
def eV(n):
    if(n <= 1):
        print(f"{n} is not and Even number")
        return
    if(n % 2 == 0):
        print("It is an even number")
    else: print("It is not an even number")
    #print([i for i in range(1, 11, 2)])
def oD(n):
    if(n <= 0):
        print(f"{n} is not and Even number")
        return
    if(n % 2 != 0):
        print("It is an ODD number")
    else: print("It is not an ODD number")
    #print([i for i in range(1, 11, 2)])
def primenum(n):
    if n <= 1:
        print(f"{n} is not a prime number")
    else:
        for i in range(2, int(n**0.5)+1):
            if(n % i == 0):
                return False
            else: return True

print("Enter Choice(1-6): ")
i = int(input())
if i == 1:
    sayhelo()
elif i == 2:
    print("For summation!")
    num1 = int(input("Enter Number One: "))
    num2 = int(input("Enter Number Two: "))
    res = summation(num1, num2)
    print(f"The result is: {res:.3}")
elif i == 3:
    print("For Square root!")
    x = int(input("Enter the number "))
    res = sqroot(x)
    print(res)
elif i == 4:
    s = input("Even or ODD: ")
    if s == "even":
        print("Check EVEN!")
        x = int(input("Enter the number"))
        eV(x)
    else:
        print("Check ODD!")
        x = int(input("Enter the number"))
        oD(x)
elif i == 5:
    print("For area of triangle!")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
else:
    print("For Prime Number!")
    n = float(input("Enter a number for the test: "))
    if(primenum(n)):
        print("It is a prime number")
    else: print("It is not a prime number")