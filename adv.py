"""magic = ['alice', 'bob', 'carol']
for i in magic:
    print(f"Hello, {i.title()}!")

animals = ['tiger', 'lion', 'bear']
for i  in animals:
    print(f"A {i.title()} would make a great pet.")

print("Any of these animals would make a great pet!")"""
"""
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range (0, len(array), 2):
    print(array[i])
"""
square = []

for i in range(1, 11, 2):
    s = i**2
    square.append(s)

print(square)
print(min(square))
print(max(square))
print(sum(square))

square = [s**i for s in range (1, 11)]
print(square) #list comprehension