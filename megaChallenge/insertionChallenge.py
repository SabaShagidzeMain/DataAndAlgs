# Scenario: You habe a list of students: (name, score, age). three sorting operations required:
# data = [("Ana", 85, 22), ("Gio", 92, 20), ("Nino", 85, 23), ("Dato", 78, 21) ("Mari", 92, 22)]

# Insertion sort by name alphabetical (ascending)
# Must be stable. Use string comparison in the while condition directly
# Verify stability: Gio < Nino alphabetically - does gio appear first?
# What is the exact key comparison expression?

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


print("Original order:")

for student in data:
    print(student)


sorted_data = insertion_sort_by_name(data.copy())


print("\nSorted by name:")

for student in sorted_data:
    print(student)


print("\nStability Verification:")

gio_index = None
nino_index = None

for i, student in enumerate(sorted_data):

    if student[0] == "Gio":
        gio_index = i

    if student[0] == "Nino":
        nino_index = i

print("Gio index :", gio_index)
print("Nino index:", nino_index)

if gio_index < nino_index:
    print("Gio appears first -> stable ordering preserved")
else:
    print("Order changed")


print("\nExact key comparison expression:")
print("arr[j][0] > key[0]")