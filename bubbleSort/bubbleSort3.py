# Bubble sort weakness: small elements far from their target move too slowly ("turtle problem")
# Comb sort: isntead of comparing adjacent pairs, use a shrinking gap (gap = len * 0.8 each round)
# Implement comb_sort(arr). benchmark against bubble_Sort on 10000 random integers
# Comb sort approaches O9n log n) average - why?

import random
import timeit

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

def comb_sort(arr):

    gap = len(arr)
    shrink = 0.8
    swapped = True

    while gap > 1 or swapped:

        # shrink gap
        gap = int(gap * shrink)

        if gap < 1:
            gap = 1

        swapped = False

        # compare elements gap apart
        for i in range(len(arr) - gap):

            if arr[i] > arr[i + gap]:

                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr


# 10,000 random integers
data = [random.randint(1, 100000) for _ in range(10000)]


def test_bubble():
    bubble_sort(data.copy())


def test_comb():
    comb_sort(data.copy())


bubble_time = timeit.timeit(test_bubble, number=1)
comb_time = timeit.timeit(test_comb, number=1)

print("Bubble Sort Time:", bubble_time)
print("Comb Sort Time:", comb_time)


print("\nWhy Comb Sort is faster:")
print("- Bubble sort only compares adjacent elements")
print("- Small values near the end move very slowly ('turtle problem')")
print("- Comb sort compares far-apart elements using a shrinking gap")
print("- Large disorder gets removed early")
print("- Final passes behave like optimized bubble sort")
print("- Average performance approaches O(n log n)")