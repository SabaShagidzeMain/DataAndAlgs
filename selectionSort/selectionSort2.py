# Modify selection_sort() to sort in descending order (largest first)
# Input: [5, 3, 8, 1, 9] -> Output: [9, 8, 5, 3, 1]
# Bonus: add a key = parameter mirroring python's sorted(): selection_sort(words, key=len) sorts by length

def selection_sort(arr, reverse=False, key=lambda x: x):

    n = len(arr)

    for i in range(n):

        selected_idx = i

        for j in range(i + 1, n):

            # normal ascending comparison using key
            if not reverse:
                if key(arr[j]) < key(arr[selected_idx]):
                    selected_idx = j

            # descending comparison using key
            else:
                if key(arr[j]) > key(arr[selected_idx]):
                    selected_idx = j

        # swap
        arr[i], arr[selected_idx] = arr[selected_idx], arr[i]

    return arr

print(selection_sort([5, 3, 8, 1, 9]))

names = ["Saba", "Giorgi", "Shahabazi"]
print(selection_sort(names, key=len))