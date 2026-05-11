def optimized_bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        # if no swaps happened, array is already sorted
        if not swapped:
            break

    return arr


# Test
numbers = [1, 2, 3, 4, 5]

print("Before:", numbers)

optimized_bubble_sort(numbers)

print("After :", numbers)