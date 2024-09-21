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
"""square = []

for i in range(1, 11, 2):
    s = i**2
    square.append(s)

print(square)
print(min(square))
print(max(square))
print(sum(square))

square = [s**i for s in range (1, 11)]
print(square) #list comprehension

arr =[i for i in range (1, 11)]
print(arr)"""

"""for i in range(1, 21):
    print(i)

lis = [i for i in range (1, 1_00_00_001)]
print(sum(lis))"""

"""odd_num = [i for i in range(1, 20, 2)]
print(odd_num)

odd = []

for i in range (1, 20, 2):
    odd.append(i)
print(odd)

mul_3 = [i*3 for i in range(3, 11)]
print(mul_3)

mul_3 = []
for i in range (3, 31):
    s = i*3
    if s > 30:
        break
    mul_3.append(s)
print(mul_3)"""

cubes = [i**3 for i in range(1, 11)]
print(cubes)

cube_1 = []
for i in range (1, 11):
    s = i**3
    cube_1.append(s)
print(cube_1)