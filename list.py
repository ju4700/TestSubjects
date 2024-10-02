#find secondlargest number in a list
def second_largest(l):
	l = list(set(l))
	l.sort()
	return l[-2]
#sort list in ascending order and descending order
def sort_list(l):
	l.sort()
	print(l)
	l.sort(reverse=True)
	print(l)
#find the smallest
def smallest(l):
	l.sort()
	return l[0]
#take input from user and print the list
def print_list():
	l = []
	n = int(input("Enter the number of elements: "))
	for i in range(n):
		l.append(int(input()))
	print(l)
	#or
	""" l = [int(input()) for i in range(n)]
		l = list(map(int, input().split()))  """
#merge two lists and sort them
def merge_sort(l1, l2):
	l = l1 + l2
	l.sort()
	return l
#find the common elements in two lists
def common_elements(l1, l2):
	return list(set(l1) & set(l2))
#find the elements that are not common in two lists
def not_common(l1, l2):
	return list(set(l1) ^ set(l2))
#remove duplicates from a list
def remove_duplicates(l):
	return list(set(l))
#find the sum of all elements in a list
def sum_elements(l):
	return sum(l)
#find the average of all elements in a
def average_elements(l):
	return sum(l)/len(l)
#find the median of all elements in a list
def median_elements(l):
	l.sort()
	n = len(l)
	if n%2 == 0:
		return (l[n//2] + l[n//2 - 1])/2
	else:
		return l[n//2]
#find the mode of all elements in a list
def mode_elements(l):
	d = {}
	for i in l:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	return max(d, key=d.get)
