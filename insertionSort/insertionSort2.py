# Rewrite insertion_sort() so the correct insert position is found with bisect.bisect_left()
# use arr.insert(pos, key) to place th eelement (import bisect)
# Benchmark both versions with timeit on 1,0000 random integers, explain the result

import bisect
import random
import timeit
from typing import List

def insertion_sort_original(arr: List[int]) -> List[int]:
    """Original insertion sort with while loop shifting"""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_bisect(arr: List[int]) -> List[int]:
    """Insertion sort using bisect to find insertion position"""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        pos = bisect.bisect_left(arr, key, 0, i)
        # Shift elements manually (faster than arr.insert)
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = key
    return arr

# Benchmark
def benchmark(n_elements=10000, n_runs=10):
    test_array = [random.randint(0, 10000) for _ in range(n_elements)]
    
    original_time = timeit.timeit(
        lambda: insertion_sort_original(test_array),
        number=n_runs
    )
    
    bisect_time = timeit.timeit(
        lambda: insertion_sort_bisect(test_array),
        number=n_runs
    )
    
    print(f"Sorting {n_elements:,} random integers ({n_runs} runs each)")
    print(f"{'Original:':<15} {original_time:.4f}s total, {original_time/n_runs:.6f}s avg")
    print(f"{'Bisect:':<15} {bisect_time:.4f}s total, {bisect_time/n_runs:.6f}s avg")
    print(f"{'Speed difference:':<15} {bisect_time/original_time:.2f}x slower with bisect")

# Just run the benchmark
benchmark(n_elements=10000, n_runs=10)