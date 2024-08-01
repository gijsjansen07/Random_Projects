'''Generate list with random numbers and sort it'''

import random

arrayNON : list = random.sample(range(1, 101), 100)
left_index = 0
right_index = len(arrayNON) - 1


print (arrayNON)

def bubblesort(array:list):
    length = len(array)

    for items in range (length):
        swap = False
        for position in range (0,length-items-1):
            
            if array[position] > array[position + 1]:
                array[position], array[position+ 1] = array[position+ 1],array[position]
                swap = True
        if swap == False:
            return array; 

def merge(array, Left_index, middle_index, Right_index):
	n1 = middle_index - Left_index + 1
	n2 = Right_index - middle_index

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = array[Left_index + i]

	for j in range(0, n2):
		R[j] = array[middle_index + 1 + j]

	i = 0	
	j = 0	
	k = Left_index	 

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1
		k += 1


	while i < n1:
		array[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		array[k] = R[j]
		j += 1
		k += 1
	

def mergesort(array, Left_index, Right_index):
	if Left_index < Right_index:

		middle_index = Left_index+(Right_index-Left_index)//2

		mergesort(array, Left_index, middle_index)
		mergesort(array, middle_index+1, Right_index)
		merge(array, Left_index, middle_index, Right_index)
	return array



print (f'Bubblesort Results: {bubblesort(arrayNON)}')
print (f"Merrgesort Results: {mergesort(arrayNON,left_index,right_index)}")
