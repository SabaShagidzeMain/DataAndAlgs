# Standard bubble only goes left to right. cocktail shaker alternate:
# -> forward pass: largest element sinks to the end
# <- Backward pass: smallest element rises to the front, repeat
# Implement cocktail_sort(arr), this reduces the "turtle problem" - small elements at the end move faster

def cocktail_sort(arr):

    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:

        swapped = False

        for i in range(start, end):

            if arr[i] > arr[i + 1]:

                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        print("Forward :", arr)

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start, -1):

            if arr[i] < arr[i - 1]:

                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        print("Backward:", arr)

        start += 1

    return arr

arr = [5, 1, 4, 2, 8, 0, 3]

print("Original:", arr)

sorted_arr = cocktail_sort(arr)

print("Sorted:", sorted_arr)