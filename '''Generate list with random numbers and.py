'''Generate list with random numbers and sort it'''

import random

arrayNON : list = random.sample(range(1, 101), 100)
left_index = 0
right_index = len(arrayNON) - 1
middle_index = round(right_index// 2)

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

def merge(array:list, L:int, R:int, M:int):
    
    pass


def mergesort(array, L, R):
    middle_index = R// 2

    if L > R:
        mergesort(array,L,middle_index)
        mergesort(array,middle_index+1,R)
        merge(array,L,R,middle_index)




print (bubblesort(arrayNON))
