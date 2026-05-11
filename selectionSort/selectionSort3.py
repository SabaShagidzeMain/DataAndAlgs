# Standard selection sort is not stable. make it stable without extra arrays:
# Instead of swapping, rotate: remove minimum, shift all elements between i and min_idx one position right, place minimum at i
# Converts O(n) swaps -> O(n2) moves but preserves stability
# Verify with [(3, "a"), (1, "b"), (3, "c")] -> [(1, "b"), (3, "a"), (3, "c")]

def stable_selection_sort(arr, key=lambda x: x):

    n = len(arr)

    for i in range(n):

        # find minimum index
        min_idx = i

        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j

        # store minimum element
        min_elem = arr[min_idx]

        # shift elements right (instead of swapping)
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1

        # place minimum at correct position
        arr[i] = min_elem

    return arr

data = [(3, "a"), (1, "b"), (3, "c")]
print(stable_selection_sort(data, key=lambda x: x[0]))