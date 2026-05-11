# Prove the comparison count is always exactly n(n-1)/2, regardless of input order
# Why is the swap count always <= n-1? hint: permutation cycle decomposition
# Flash memory: a write costs 1000x more than a read. Compare seelction sort vs insertion sort write counts on [5, 4, 3, 2, 1] Which wins?

# 1. Selection Sort Analysis
def selection_sort_analysis(arr):
    n = len(arr)

    comparisons = 0
    swaps = 0

    for i in range(n - 1):

        min_idx = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, comparisons, swaps

# 2. Insertion Sort (write tracking)
def insertion_sort_write_analysis(arr):
    n = len(arr)

    comparisons = 0
    writes = 0

    for i in range(1, n):
        key = arr[i]
        writes += 1  # storing key

        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            writes += 1  # shift write
            j -= 1

        arr[j + 1] = key
        writes += 1

    return arr, comparisons, writes

# 3. Run on worst-case input
arr = [5, 4, 3, 2, 1]

sel_sorted, sel_comp, sel_swaps = selection_sort_analysis(arr.copy())
ins_sorted, ins_comp, ins_writes = insertion_sort_write_analysis(arr.copy())

n = len(arr)
formula_comparisons = n * (n - 1) // 2

# 4. Results
print("=== Selection Sort ===")
print("Sorted:", sel_sorted)
print("Comparisons:", sel_comp)
print("Swaps:", sel_swaps)
print("Formula n(n-1)/2:", formula_comparisons)

print("\n=== Insertion Sort ===")
print("Sorted:", ins_sorted)
print("Comparisons:", ins_comp)
print("Writes:", ins_writes)

print("\n=== Flash Memory Model (Writes matter most) ===")
print("Selection writes (swaps):", sel_swaps * 3)  # each swap ~ 3 writes
print("Insertion writes:", ins_writes)

if sel_swaps * 3 < ins_writes:
    print("Winner: Selection Sort (fewer writes)")
else:
    print("Winner: Insertion Sort")