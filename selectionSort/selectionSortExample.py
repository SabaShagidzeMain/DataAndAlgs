def selection_sort(arr):
    n = len(arr)

    # i is the target position
    for i in range(n - 1):
        min_idx = i # assume i is minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum into position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))