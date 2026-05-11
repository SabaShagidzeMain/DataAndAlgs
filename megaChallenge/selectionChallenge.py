# Scenario: You habe a list of students: (name, score, age). three sorting operations required:
# data = [("Ana", 85, 22), ("Gio", 92, 20), ("Nino", 85, 23), ("Dato", 78, 21) ("Mari", 92, 22)]

# Selection sort by score descending
# Max-based selection sort. notice: Ana(86) and Nino(86) share a score
# Is the output stable print their relative order before and after
# Verify that selection sort is not stable for equal keys

data = [
    ("Ana", 85, 22),
    ("Gio", 92, 20),
    ("Nino", 85, 23),
    ("Dato", 78, 21),
    ("Mari", 92, 22)
]


# Selection Sort by score DESCENDING

def selection_sort_desc(arr):

    n = len(arr)

    for i in range(n):

        max_idx = i

        for j in range(i + 1, n):

            # compare scores
            if arr[j][1] > arr[max_idx][1]:
                max_idx = j

        # swap
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


# Before sorting

print("Original order:")
for student in data:
    print(student)

print("\nStudents with score 85 BEFORE sorting:")

for student in data:
    if student[1] == 85:
        print(student)


# Sort

sorted_data = selection_sort_desc(data.copy())


# After sorting

print("\nSorted by score descending:")
for student in sorted_data:
    print(student)

print("\nStudents with score 85 AFTER sorting:")

for student in sorted_data:
    if student[1] == 85:
        print(student)


# Stability check

print("\nStability Verification:")

print("Before sorting: Ana came before Nino")
print("After sorting: check if their order changed")

ana_index = None
nino_index = None

for i, student in enumerate(sorted_data):

    if student[0] == "Ana":
        ana_index = i

    if student[0] == "Nino":
        nino_index = i

if ana_index < nino_index:
    print("Order preserved -> stable in this run")
else:
    print("Order changed -> selection sort is NOT stable")