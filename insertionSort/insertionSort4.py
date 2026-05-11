# Design class SortedStream with add(x) -> inserts maintaining sorted order, get_sorted() -> O(1)
# V1: use bisect.insort() - analyse amortized cost per insertion
# V2 use sortedcontainers.SortedList for O(log n) insertions
# Bencmark V1 vs V2 at n = 10000 insertions

import bisect
import timeit
import random
from sortedcontainers import SortedList

class SortedStreamV1:
    """Uses bisect.insort() - O(n) per insertion"""
    def __init__(self):
        self.data = []
    
    def add(self, x):
        bisect.insort(self.data, x)
    
    def get_sorted(self):
        return self.data

class SortedStreamV2:
    """Uses SortedList - O(log n) per insertion"""
    def __init__(self):
        self.data = SortedList()
    
    def add(self, x):
        self.data.add(x)
    
    def get_sorted(self):
        return list(self.data)

# Verify correctness
test_data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
v1, v2 = SortedStreamV1(), SortedStreamV2()

for x in test_data:
    v1.add(x)
    v2.add(x)

print(f"Input: {test_data}")
print(f"V1 sorted: {v1.get_sorted()}")
print(f"V2 sorted: {v2.get_sorted()}")
print(f"Correct: {v1.get_sorted() == v2.get_sorted() == sorted(test_data)}\n")

# Benchmark
n = 10000
random.seed(42)
test_data = [random.randint(0, n*10) for _ in range(n)]

v1 = SortedStreamV1()
time_v1 = timeit.timeit(lambda: [v1.add(x) for x in test_data], number=1)

v2 = SortedStreamV2()
time_v2 = timeit.timeit(lambda: [v2.add(x) for x in test_data], number=1)

print(f"Benchmark ({n:,} insertions):")
print(f"  V1 (bisect): {time_v1:.4f}s (O(n) per insert)")
print(f"  V2 (SortedList): {time_v2:.4f}s (O(log n) per insert)")
print(f"  V2 is {time_v1/time_v2:.1f}x faster")