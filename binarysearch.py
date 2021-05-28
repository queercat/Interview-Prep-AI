import math

def search_n(arr, value):
	index = -1

	for i, element in enumerate(arr):
		if element == value:
			return i

	return index

def search_divide(arr, value):
	begin = 0
	end = len(arr) - 1

	while(begin <= end):
		middle_index = math.floor((begin + end) / 2)

		if arr[middle_index] < value:
			begin = middle_index + 1

		elif arr[middle_index] > value:
			end = middle_index - 1

		else:
			return middle_index

	return -1

arr = []

for i in range(1000000):
	arr.append(i)

print(search_divide(arr, 5))