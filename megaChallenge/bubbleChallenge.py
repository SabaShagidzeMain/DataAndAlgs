# Scenario: You habe a list of students: (name, score, age). three sorting operations required:
# data = [("Ana", 85, 22), ("Gio", 92, 20), ("Nino", 85, 23), ("Dato", 78, 21) ("Mari", 92, 22)]

# Bubble sort by age ascending
# Use the optimised version with swapped flag
# How many passes does it execute? Does early exit trigger?
# Count total comparisons and swaps? near best or worst case?

data = [
    ("Ana", 85, 22),
    ("Gio", 92, 20),
    ("Nino", 85, 23),
    ("Dato", 78, 21),
    ("Mari", 92, 22)
]

def bubble_sort_by_age(arr):

    n = len(arr)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n - 1):

        swapped = False
        passes += 1

        for j in range(n - i - 1):

            comparisons += 1

            if arr[j][2] > arr[j + 1][2]:   # AGE comparison

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break   # early exit triggered

    return arr, passes, comparisons, swaps


sorted_data, passes, comp, swaps = bubble_sort_by_age(data.copy())

print("Sorted:", sorted_data)
print("Passes:", passes)
print("Comparisons:", comp)
print("Swaps:", swaps)