def insertion_sort(arr):
    """
    Sorts a list using the insertion sort algorithm.

    Args:
        arr: List to be sorted

    Returns:
        The sorted list
    """
    # Make a copy to avoid modifying the original
    sorted_arr = arr.copy()

    # Iterate through the array starting from the second element
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1

        # Place key in its correct position
        sorted_arr[j + 1] = key

    return sorted_arr


if __name__ == "__main__":
    # Test with a sample list
    original_list = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:")
    print(original_list)

    sorted_list = insertion_sort(original_list)

    print("\nSorted list after insertion sort:")
    print(sorted_list)
