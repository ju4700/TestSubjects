print("Hello World!")
x = 10
y = 21.4

strin_1 = "kjdsfigasdl"
print(f"This is the string {strin_1.title()}")

lis_1 = ['a', 's', 'c', 'd']
lis_1.insert(0, 'x')
print(lis_1)
print(sorted(lis_1))
print(lis_1)
print(sorted(lis_1, reverse=True))
print(lis_1)
lis_1.sort()
print(lis_1)
lis_1.reverse()
print(lis_1)

lis_2 = [1, 2, 34, 5, 4, 65]
del lis_2[3]
n_S = lis_2.pop()
print(lis_2)

for i in lis_2:
	print(i)

new_ls = [i for i in range(1, 11)]
new_l = [i**2 for i in range (3, 31)]
print(new_ls) # a list of integers from 1 to 10

emp_lis = []
for i in range(1, 21, 2):
	emp_lis.append(i)
print(emp_lis) #list of odd numbers

emp_l = []
for i in range(50, 101, 2):
	s = i*3
	if(s == 180):
		break
	emp_l.append(s)
print(emp_l)
print(min(emp_l), max(emp_l), sum(emp_l))

players = ['alice', 'bob', 'mof', 'cob', 'fed', 'mol']
print(players[0:2])
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-3:])

for i in players[:3]:
	print(i)

newplayers = players[0:3]
print(newplayers)