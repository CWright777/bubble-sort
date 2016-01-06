import random

sample_list = []

number = 0

while number < 100:
	sample_list.append(random.randint(0,10000))
	number += 1

def bubbleSort(arr):
	arr_sorted = False
	while arr_sorted == False:
		arr_sorted = True
		for i in range(0,len(arr) - 1):
			if arr[i] > arr[i + 1]:
				temp = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = temp
				arr_sorted = False
	print arr

bubbleSort(sample_list)