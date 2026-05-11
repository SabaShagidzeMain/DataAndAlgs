# Trace [8, 4, 3, 7, 6, 5] - for each i record: key, shifts made, array after insertion
# For [1, 2, 3, 4, 5]: Best/Worst/average? Does the while loop execute? Exact comparison count?
# For [5, 4, 3, 2, 1]: Best/Worst/Average? Count total comparisons and total element shift

import bisect
import random
import timeit

def insertion_sort_trace(arr):
    """Insertion sort with minimal tracing"""
    print(f"Original: {arr}")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        shifts = 0
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        
        arr[j + 1] = key
        print(f"i={i}, key={key}, shifts={shifts} -> {arr}")
    return arr

def analyze_sort(arr, name):
    """Count comparisons and shifts without verbose printing"""
    comparisons = 0
    shifts = 0
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key
    
    return comparisons, shifts

# Part 1: Trace
print("=" * 50)
print("TRACING [8, 4, 3, 7, 6, 5]")
print("=" * 50)
insertion_sort_trace([8, 4, 3, 7, 6, 5])

# Part 2 & 3: Analysis
print("\n" + "=" * 50)
print("ANALYSIS")
print("=" * 50)

# Test cases
cases = [
    ([1, 2, 3, 4, 5], "Best case"),
    ([5, 4, 3, 2, 1], "Worst case")
]

for arr, case_type in cases:
    comp, shifts = analyze_sort(arr, case_type)
    expected_comp = len(arr) - 1 if case_type == "Best case" else len(arr) * (len(arr) - 1) // 2
    print(f"\n{case_type}: {arr}")
    print(f"  Comparisons: {comp} (expected: {expected_comp})")
    print(f"  Shifts: {shifts} (expected: {expected_comp if case_type == 'Worst case' else 0})")
    print(f"  {'[PASS]' if comp == expected_comp else '[FAIL]'}")

print("\n" + "=" * 50)
print("CONCLUSION")
print("=" * 50)
print("Best case (sorted): O(n) - n-1 comparisons, 0 shifts")
print("Worst case (reverse): O(n^2) - n(n-1)/2 comparisons and shifts")
print("Average case: O(n^2) - ~n^2/4 comparisons")