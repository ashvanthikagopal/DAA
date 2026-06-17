# linear_search.py

def linear_search(arr, target):
    """
    Searches for target in the list using Linear Search.
    Returns the index if found, otherwise returns -1.
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# Main Program
numbers = [10, 25, 35, 40, 55, 70]

target = int(input("Enter number to search: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")