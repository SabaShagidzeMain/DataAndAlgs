# Trace basic bubble sort on [3, 1, 2]: record every comparison, every swap, array after each pass
# Trace optimized bubble sort on [1, 2, 3, 4]: wich pass triggers break? comparisons total?
# Compare: how many comparisons does basic vs optimized perform on [1, 2, 3, 4]

def bubble_sort_trace(arr):

    n = len(arr)

    print("=== BASIC BUBBLE SORT TRACE ===")
    print("Initial:", arr)

    comparisons = 0
    swaps = 0

    for i in range(n - 1):

        print(f"\nPass {i + 1}")

        for j in range(n - 1):

            comparisons += 1

            print(f"Compare {arr[j]} and {arr[j + 1]}")

            if arr[j] > arr[j + 1]:

                print("Swap!")

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

            print("Array:", arr)

        print("After pass:", arr)

    print("\nTotal comparisons:", comparisons)
    print("Total swaps:", swaps)

def optimized_bubble_sort(arr):

    n = len(arr)

    print("\n=== OPTIMIZED BUBBLE SORT ===")
    print("Initial:", arr)

    comparisons = 0

    for i in range(n - 1):

        swapped = False

        print(f"\nPass {i + 1}")

        for j in range(n - 1 - i):

            comparisons += 1

            print(f"Compare {arr[j]} and {arr[j + 1]}")

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                print("Swap!")
                print("Array:", arr)

        if not swapped:
            print("No swaps -> break triggered")
            break

    print("\nTotal comparisons:", comparisons)


bubble_sort_trace([3, 1, 2])

optimized_bubble_sort([1, 2, 3, 4])