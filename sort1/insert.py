def insert_sort(array, n):
    for i in n:
        target = array[i]
        j = i - 1
        while j >= 0 and target < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = target

def bubble_sort(array, n):
    for i in n:
        for j in reversed(range(i, n-1)):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]

def selection_sort(array, n):
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]