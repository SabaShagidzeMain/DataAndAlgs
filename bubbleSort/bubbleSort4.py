# parallel variant: in each round all comparisons run simultaneously on separate threads
# Odd rounds: compare/swap pairs (0, 1), (2, 3) (4, 5) - all independently in parallel
# Even rounds: compare/swap pairs (1, 2) (3, 4) (5, 6) - all in parallel
# After n rounds the array is sorted: O(n) parallel steps vs O(n^2) sequential
# Simulate with python threads on n=9, identify required synchronisation

import threading
import random

def compare_swap(arr, i):

    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

def parallel_odd_even_sort(arr):

    n = len(arr)

    print("Initial:", arr)

    for round_num in range(n):

        threads = []

        if round_num % 2 == 0:

            start = 0

        else:

            start = 1

        # create threads
        for i in range(start, n - 1, 2):

            t = threading.Thread(target=compare_swap, args=(arr, i))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"Round {round_num + 1}: {arr}")

    return arr

arr = [random.randint(1, 99) for _ in range(9)]

sorted_arr = parallel_odd_even_sort(arr)

print("\nSorted:", sorted_arr)