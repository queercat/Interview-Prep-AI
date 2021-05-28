import random

def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]

def partition(arr, left, right):
	orig_pivot = right
	pivot = arr[right]

	right -= 1

	while (True):
		if arr[left] < pivot:
			left += 1

		if arr[right] > pivot:
			right -= 1

		if (left > right):
			swap(arr, left, orig_pivot)
			break

		if arr[left] > pivot and arr[right] < pivot:
			swap(arr, left, right)

	return left

def quicksort(arr, left, right):
	if len(arr) < 2:
		return arr

	if (left < right):
		pivot = partition(arr, left, right)
		
		quicksort(arr, left, pivot - 1)
		quicksort(arr, pivot + 1, right)

random.seed()

arr = []

for i in range(10 ** 4):
	num = random.randint(0, 10 ** 10)

	while (num in arr):
		num = random.randint(0, 10 ** 10)

	arr.append(num)

quicksort(arr, 0, len(arr) - 1)