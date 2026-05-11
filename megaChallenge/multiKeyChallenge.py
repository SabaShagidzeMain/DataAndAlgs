# Scenario: You habe a list of students: (name, score, age). three sorting operations required:
# data = [("Ana", 85, 22), ("Gio", 92, 20), ("Nino", 85, 23), ("Dato", 78, 21) ("Mari", 92, 22)]

# Apply two stable sorts in sequence:
# (1) sort by name asc (insertion sort), then (2) sort by score desc
# Equal-score students remain alphabetically ordered - why?
# This is the "stable sort composition" trick used in production systems

data = [
    ("Ana", 85, 22),
    ("Gio", 92, 20),
    ("Nino", 85, 23),
    ("Dato", 78, 21),
    ("Mari", 92, 22)
]

def insertion_sort_by_name(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


step1 = insertion_sort_by_name(data.copy())
print("After sorting by name:")
print(step1)

def insertion_sort_by_score_desc(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        # descending by score
        while j >= 0 and arr[j][1] < key[1]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


final = insertion_sort_by_score_desc(step1.copy())

print("\nAfter sorting by score desc:")
print(final)