def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n): # i = 0 is already sorted
        key = arr[i] # save element before shifts
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # shift right
            j -= 1
        arr[j + 1] = key # insert at correct position
    return arr

# Best case: while loop body never runs!
print(insertion_sort([1, 2, 3, 4, 5]))