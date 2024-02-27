# -*- coding: utf-8 -*-
"""A1-Sorting Algorithms

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sPb1dZbAJaBhVNHJr3_vuHR8tIjwpLmC
"""

# Define a function to distribute chocolates to students iteratively.
def distribute_chocolates_iteratively(chocolates, students):
    # Check if there are enough chocolates for all students. If not, raise an error.
    if len(students) > len(chocolates):
        raise ValueError("Not enough chocolates for all students")

    # Initialize an empty dictionary to hold the distribution of chocolates to students.
    distribution = {}
    # Iterate over the students list with their index.
    for i, student in enumerate(students):
        # Assign a chocolate to each student based on their index.
        distribution[student] = chocolates[i]
    # Return the final distribution dictionary.
    return distribution

# Define a function to distribute chocolates to students recursively.
def distribute_chocolates_recursively(chocolates, students, distribution=None):
    # If the distribution dictionary is not provided, initialize it as an empty dictionary.
    if distribution is None:
        distribution = {}

    # Check if there are enough chocolates for all students. If not, raise an error.
    if len(students) > len(chocolates):
        raise ValueError("Not enough chocolates for all students")

    # Base case: if there are no students left to distribute chocolates to, return the distribution.
    if not students:
        return distribution

    # Recursive case: assign the first chocolate to the first student in the list.
    student = students[0]
    distribution[student] = chocolates[0]

    # Recursively call the function with the remaining chocolates and students, passing the updated distribution.
    return distribute_chocolates_recursively(chocolates[1:], students[1:], distribution)

# Define a list of chocolates, each represented as a dictionary with weight, price, and type.
chocolates = [
    {'weight': 50, 'price': 2, 'type': 'milk'},
    {'weight': 30, 'price': 1.5, 'type': 'dark'},
    {'weight': 45, 'price': 2.5, 'type': 'white'},
    {'weight': 30, "price":1.5, "type": 'pistachio'},
    {'weight': 50, 'price': 2, 'type': 'milk'},
]

# Define a list of students.
students = ['Hessa', 'Hind', 'Noora',"Aisha","Saeed"]

# Test the iterative function to distribute chocolates.
iterative_distribution = distribute_chocolates_iteratively(chocolates, students)
print("Iterative Distribution:", iterative_distribution)

# Test the recursive function to distribute chocolates.
recursive_distribution = distribute_chocolates_recursively(chocolates, students)
print("Recursive Distribution:", recursive_distribution)

# Define a list of dictionaries, each representing a chocolate with attributes: name, weight, and price.
chocolates = [
    {'type': 'KitKat', 'weight': 100, 'price': 2.50},
    {'type': 'Bounty', 'weight': 150, 'price': 3.00},
    {'type': 'Smarties', 'weight': 200, 'price': 4.00},
    {'type': 'Maltesers', 'weight': 90, 'price': 2.00},
    {'type': 'Snickers', 'weight': 50, 'price': 1.50},
    {'type': 'Mars', 'weight': 120, 'price': 2.80}
]

# Define a function to perform merge sort on a list of dictionaries based on a specified key.
def merge_sort(arr, key):
    # If the array is more than one element, split it into halves to start the sort.
    if len(arr) > 1:
        # Find the midpoint of the array.
        mid = len(arr) // 2
        # Split the array into left and right halves.
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves.
        merge_sort(left_half, key)
        merge_sort(right_half, key)

        # Initialize pointers for traversing the left half, right half, and the main array.
        i = j = k = 0

        # Merge the sorted halves back together, overwriting the original array.
        while i < len(left_half) and j < len(right_half):
            # Compare elements based on the specified key and arrange them in the main array.
            if left_half[i][key] < right_half[j][key]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left half into the main array.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right half into the main array.
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Create a copy of the original chocolates list to sort by weight.
chocolates_by_weight = chocolates[:]
# Sort the copied list by weight.
merge_sort(chocolates_by_weight, 'weight')

# Create another copy of the original chocolates list to sort by price.
chocolates_by_price = chocolates[:]
# Sort the copied list by price.
merge_sort(chocolates_by_price, 'price')

# Print the sorted lists to verify the sorting.
print("Chocolates sorted by weight:")
for chocolate in chocolates_by_weight:
    print(chocolate)

print("\nChocolates sorted by price:")
for chocolate in chocolates_by_price:
    print(chocolate)

# Defines a function that uses binary search to find a student based on the weight of a chocolate.
def binary_search_by_weight(chocolates, students, target_weight):
    # Initializes left and right pointers for the binary search.
    left, right = 0, len(chocolates) - 1

    # Continues the search as long as the left pointer is less than or equal to the right pointer.
    while left <= right:
        # Calculates the middle index.
        mid = (left + right) // 2

        # Checks if the chocolate at the middle index matches the target weight.
        if chocolates[mid]['weight'] == target_weight:
            # If the mid index is within the range of the students list, returns the corresponding student.
            if mid < len(students):
                return students[mid]
            # If the mid index is out of the students list's range, indicates no student is found for this chocolate.
            else:
                return "No student found for this chocolate."
        # If the target weight is greater than the weight at mid, narrows the search to the right half.
        elif chocolates[mid]['weight'] < target_weight:
            left = mid + 1
        # If the target weight is less than the weight at mid, narrows the search to the left half.
        else:
            right = mid - 1

    # If the loop exits without returning, indicates no chocolate matches the specified weight.
    return "No chocolate matches the specified weight."

# Defines a list of chocolates sorted by weight, each represented as a dictionary.
chocolates = [
    {'type': 'Snickers', 'weight': 50, 'price': 1.5},
    {'type': 'Maltesers', 'weight': 90, 'price': 2.0},
    {'type': 'KitKat', 'weight': 100, 'price': 2.5},
    {'type': 'Mars', 'weight': 120, 'price': 2.8},
    {'type': 'Bounty', 'weight': 150, 'price': 3.0},
    {'type': 'Smarties', 'weight': 200, 'price': 4.0}
]

# Defines a list of students.
students = ['Hessa', 'Hind', 'Noora', "Aisha", "Saeed", "maryam"]

# Demonstrates how to use the function to find the student associated with a chocolate of a specific weight.
# In this case, it searches for a chocolate weighing 150 grams.
print(binary_search_by_weight(chocolates, students, 150))