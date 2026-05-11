def bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Test
numbers = [5, 2, 8, 1, 3]

print("Before:", numbers)

bubble_sort(numbers)

print("After :", numbers)