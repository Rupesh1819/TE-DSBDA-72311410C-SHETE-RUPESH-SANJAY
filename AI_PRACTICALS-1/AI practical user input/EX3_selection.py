# Selection Sort Program using User Input

"""
Time Complexity
O(n²)

Space Complexity
O(1)
"""

# Number of elements
n = int(input("Enter number of elements: "))

# Empty list
arr = []

# Take elements from user
for i in range(n):

    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Original array
print("\nOriginal Array:")
print(arr)

# ---------------- SELECTION SORT ---------------- #

# Traverse through all array elements
for i in range(n):

    # Assume current index has minimum value
    min_index = i

    # Find minimum element in remaining array
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap minimum element with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

    # Print each pass
    print(f"\nPass {i + 1}:")
    print(arr)

# ---------------- SORTED ARRAY ---------------- #

print("\nSorted Array:")
print(arr)