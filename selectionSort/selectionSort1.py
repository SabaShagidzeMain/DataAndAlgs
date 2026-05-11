# Trace Selection Sort by hand on [29, 10, 14, 37, 13]
# For each pass record: (i) min_idx found (ii) the swap made (iii) array state after swap
# Count total comparisons and total swaps. Verify: comparisons = n(n-1)/2

def selection_sort_trace(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):

        min_idx = i

        print(f"\nPass {i + 1}")
        print("Starting array:", arr)

        # find minimum
        for j in range(i + 1, n):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j

        print("Min index found:", min_idx, "value:", arr[min_idx])

        # swap if needed
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            print(f"Swapped arr[{i}] and arr[{min_idx}]")
        else:
            print("No swap needed")

        print("Array after pass:", arr)

    print("\n--- Summary ---")
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


arr = [29, 10, 14, 37, 13]
selection_sort_trace(arr)